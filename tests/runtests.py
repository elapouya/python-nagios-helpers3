import doctest
from naghelp import *
import os

modules = ['naghelp.host',
           'naghelp.perf',
           'naghelp.plugin',
           'naghelp.response',
           'naghelp.launcher',
           'naghelp.mixins', ]
files = ['docs/intro.rst']

failed = 0
tested = 0

print('=' * 60)

for m in modules:
    print('Testing %s ...' % m)
    mod = __import__(m, fromlist=[''])
    f_count, t_count = doctest.testmod(mod, globs=globals(),
                                       optionflags=doctest.REPORT_NDIFF)
    failed += f_count
    tested += t_count

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for f in files:
    print('Testing %s ...' % f)
    path = os.path.join(base_dir, f)
    f_count, t_count = doctest.testfile(path, False, globs=globals(),
                                        optionflags=doctest.REPORT_NDIFF)
    failed += f_count
    tested += t_count

print('=' * 60)
print('Number of tests : %s' % tested)
print('Failed : %s' % failed)
