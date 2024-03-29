3.0.2 (2021-12-14)
------------------
Fix collect.Snmp for md5 auth protocol

3.0.1 (2019-02-06)
------------------
Add run_channels() method to Ssh class

3.0.0 (2018-11-29)
------------------
Port of python-nagios-helpers from python 2 to python 3

0.2.3 (2018-06-20)
------------------
fix priv_protocol argument for collect.Snmp

0.2.2 (2018-02-28)
------------------
Add object_identity_to_string option in Snmp class
Add ignore_errors option in Snmp.*walk methods
Add SnmpWalkError exception to get truncated result

0.2.1 (2018-02-01)
------------------
Update Winrm collect class

0.2.0 (2018-02-01)
------------------
Add Winrm collect class

0.1.23 (2017-09-08)
-------------------
Move save_host_data() in plugin run() method

0.1.22 (2017-07-07)
-------------------
Add Ssh run_script(), get() and put() methods

0.1.21 (2017-04-26)
-------------------
Add textops.logger as managed logger

0.1.20 (2017-04-26)
-------------------
moving host debug traces into load_host_data()

0.1.19 (2017-04-22)
-------------------
Cache discovered plugins in find_plugins()

0.1.18 (2017-04-07)
-------------------
add post and session handling in Http() class

0.1.17 (2017-04-05)
-------------------
do not add logger handler more than once

0.1.16 (2017-03-27)
-------------------
Now possible to instanciate a plugin with extra options

0.1.15 (2017-03-20)
-------------------
Fix case where there is no docstring for a plugin

0.1.14 (2017-01-31)
-------------------
Remove version limitation over sphinx package in setup.py

0.1.12 (2017-01-26)
-------------------
remove unusefull code

0.1.11 (2017-01-26)
-------------------
runsh* now return extended type for textops operations

0.1.10 (2016-09-05)
-------------------
add collect_* options
add timeout for collect_data()

0.1.9 (2016-08-26)
------------------
Map all options in host object (not only host__*)

0.1.8 (2016-08-04)
------------------
Perf data in plugin output are now space separated

0.1.7 (2016-04-14)
------------------
Add Execution date for active plugins in plugin informations section
Add Update date in plugin informations for Managed hosts

0.1.6 (2016-04-12)
------------------
Add HostsManager Mixin
Add collect.Http class
Create Lockfile utility
move Timeout utility in tools.py

0.1.5 (2016-03-23)
------------------
Add Gauges Mixin
Add docs
Many other improvements

0.1.4 (2016-03-08)
------------------
Better error management

0.1.3 (2016-01-13)
------------------
Add docs

0.1.1 (2016-01-08)
------------------
Add a launcher

0.1.0 (2015-12-17)
------------------
Add some docs, tests
Tune some functions

0.0.7 (2015-11-19)
------------------
First working version
