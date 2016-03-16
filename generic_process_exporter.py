#!/usr/bin/env python
import os
import sys
import yaml
import time
import psutil

from prometheus_client import start_http_server, Summary, Gauge

USAGE = """

./generic_process_exporter.py /path/to/config.yml

* See README.md for more information

"""

PROCESS_TIME = Summary('gpe_processing_seconds', 'Time spent processing request')

def quit_script(msg,exit_code):
    print msg
    sys.exit(exit_code)


@PROCESS_TIME.time()
def process(lc):
    for p in lc.config['check_processes']:
        num_procs = 0
        total_threads = 0
        context_switch_vol = 0
        context_switch_invol = 0
        for pid in psutil.process_iter(): # TODO - collect this first for faster performance?
            if pid.name() == p:
                num_procs += 1
                total_threads += pid.num_threads()
                context_switch_vol += pid.num_ctx_switches()[0]
                context_switch_invol += pid.num_ctx_switches()[1]
        lc.metrics[p]['num_procs'].set(num_procs)
        lc.metrics[p]['total_threads'].set(total_threads)
        lc.metrics[p]['context_switch_vol'].set(context_switch_vol)
        lc.metrics[p]['context_switch_invol'].set(context_switch_invol)

class LocalConfig:
    def __init__(self,config_file):
        try:
            with open(os.path.expanduser(config_file),'r') as cf:
                self.config = yaml.load(cf)
        except Exception as e:
            quit_script(str(e), 1)
        self.fill_defaults()
        self.metrics = {}
        self.build_metrics()   
            
    def _set_val(self,key,value):
        if not self.config.has_key(key):
            self.config[key] = value
            print "Setting Default:  {0} to {1}".format(key,value)
        else:
            if not type(self.config[key]) == type(value):
                quit_script("config option: {0} expects type {1}, but got {2}".format(key, 
                                                                                      type(value).__name__, 
                                                                                      type(self.config[key]).__name__), 1)
            
    def fill_defaults(self):
        self._set_val('check_interval_seconds', 20)
        self._set_val('http_server_port',8000)
        self._set_val('check_processes', ['rsyslogd'])
        
    def build_metrics(self):
        for p in self.config['check_processes']:
            self.metrics[p] = {}
            self.metrics[p]['num_procs'] = Gauge('{0}_num_procs'.format(p),'Number of {0} Processes'.format(p))
            self.metrics[p]['total_threads'] = Gauge('{0}_total_threads'.format(p),
                                                     'Number of threads - (all {0} processes)'.format(p))
            self.metrics[p]['context_switch_vol'] = Gauge('{0}_context_switch_vol'.format(p),
                                                          'Voluntary context switches - (all {0} processes)'.format(p))
            self.metrics[p]['context_switch_invol'] = Gauge('{0}_context_switch_invol'.format(p),
                                                            'Involuntary context switches - (all {0} processes)'.format(p))


#
#    Main Execution
#
if __name__ == '__main__':
    # Pre flight checks and config
    if len(sys.argv) != 2:
        quit_script(USAGE,1)
    lc = LocalConfig(sys.argv[1])
    print "All config and defaults loaded. \n{0}\n".format(lc.config)
    
    
    #
    #    Run HTTP server
    #
    start_http_server(lc.config['http_server_port'])
    while True:
        process(lc)
        # TODO Start and finish away from processing time.
        time.sleep(lc.config['check_interval_seconds']) 