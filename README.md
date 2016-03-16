Generic Process Exporter for Prometheus
=======================================

Metrics exporter for a given list of processes defined by a simple yaml config. 
For example, to export run statisics for a given list of system daemons or critical processes. 

*** Still a work in progress ***

Requirements
============

* prometheus_client
* psutil
* PyYAML

Usage
=====

* Modify config.yml
* Start the serivce

    ./generic_process_exporter.py /path/to/config.yml
    
* From a browser (or something like curl) check the metrics on the host with your chosen port.

    curl http://localhost:8000

Configuration
=============

* See config.yaml

Notes
=====
 
Built on Ubuntu, for Ubuntu.
That said I expect other types of Linux will also work well. 
This will possibly even work on windows, as the library doing most of the lifting in the awesome python library psutil.


Example Output
==============

    # HELP chrome_num_procs Number of chrome Processes
    # TYPE chrome_num_procs gauge
    chrome_num_procs 28.0
    # HELP chrome_context_switch_vol Voluntary context switches - (all chrome processes)
    # TYPE chrome_context_switch_vol gauge
    chrome_context_switch_vol 4468153.0
    # HELP chrome_total_threads Number of threads - (all chrome processes)
    # TYPE chrome_total_threads gauge
    chrome_total_threads 304.0
    # HELP process_virtual_memory_bytes Virtual memory size in bytes
    # TYPE process_virtual_memory_bytes gauge
    process_virtual_memory_bytes 132816896.0
    # HELP process_resident_memory_bytes Resident memory size in bytes
    # TYPE process_resident_memory_bytes gauge
    process_resident_memory_bytes 18833408.0
    # HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
    # TYPE process_start_time_seconds gauge
    process_start_time_seconds 1458124530.01
    # HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
    # TYPE process_cpu_seconds_total counter
    process_cpu_seconds_total 0.42000000000000004
    # HELP process_open_fds Number of open file descriptors.
    # TYPE process_open_fds gauge
    process_open_fds 7.0
    # HELP process_max_fds Maximum number of open file descriptors.
    # TYPE process_max_fds gauge
    process_max_fds 1024.0
    # HELP node_exporter_context_switch_invol Involuntary context switches - (all node_exporter processes)
    # TYPE node_exporter_context_switch_invol gauge
    node_exporter_context_switch_invol 0.0
    # HELP rsyslogd_num_procs Number of rsyslogd Processes
    # TYPE rsyslogd_num_procs gauge
    rsyslogd_num_procs 1.0
    # HELP gpe_processing_seconds Time spent processing request
    # TYPE gpe_processing_seconds summary
    gpe_processing_seconds_count 6.0
    gpe_processing_seconds_sum 0.38103771209716797
    # HELP rsyslogd_total_threads Number of threads - (all rsyslogd processes)
    # TYPE rsyslogd_total_threads gauge
    rsyslogd_total_threads 4.0
    # HELP node_exporter_num_procs Number of node_exporter Processes
    # TYPE node_exporter_num_procs gauge
    node_exporter_num_procs 0.0
    # HELP node_exporter_context_switch_vol Voluntary context switches - (all node_exporter processes)
    # TYPE node_exporter_context_switch_vol gauge
    node_exporter_context_switch_vol 0.0
    # HELP rsyslogd_context_switch_vol Voluntary context switches - (all rsyslogd processes)
    # TYPE rsyslogd_context_switch_vol gauge
    rsyslogd_context_switch_vol 9.0
    # HELP rsyslogd_context_switch_invol Involuntary context switches - (all rsyslogd processes)
    # TYPE rsyslogd_context_switch_invol gauge
    rsyslogd_context_switch_invol 1.0
    # HELP node_exporter_total_threads Number of threads - (all node_exporter processes)
    # TYPE node_exporter_total_threads gauge
    node_exporter_total_threads 0.0
    # HELP chrome_context_switch_invol Involuntary context switches - (all chrome processes)
    # TYPE chrome_context_switch_invol gauge
    chrome_context_switch_invol 72492.0


Todo
====

* Better validation of the check_processes list
* Move cs away from gauge to counter?
* psutils:  num_fds, io_counters, cpu_percent, cpu_times, memory_info, open_files, connections