#!/usr/bin/python3.10

import re

with open('/proc/meminfo') as f:
    f_string = f.read()
    f_string = re.sub(r":","",f_string)
    f_string = re.sub(r" 0"," _",f_string)
    print(f_string)
