Generic Process Exporter for Prometheus
=======================================

The aim here is to export metrics for a given list of processes defined in a yaml config. 
For example, to export run statisics for a given list of system daemons. 

*** This is still a work in progress ***

Requirements
============

* prometheus_client
* psutil

Usage
=====

* Modify config.yml
* Start the serivce

    ./generic_process_exporter.py /path/to/config.yml
    
* From a browser (or something like curl) check the metrics on the host with your chosen port.

Configuration
=============

* 

Notes
=====
 
Built on Ubuntu, for Ubuntu.
That said I expect other types of Linux will also work well. 
This will possibly even work on windows, as the library doing most of the lifting is the awesome psutil.


Todo
====

* Better validation of the check_processes list
* requirements.txt
* Move cs away from gauge to counter?


* psutils:  num_fds, io_counters, cpu_percent, cpu_times, memory_info, open_files, connections