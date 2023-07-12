#!/usr/bin/python3.10

import re

out_f = ""

with open('/proc/meminfo') as f:
    f_string = f.read()
    f_string = re.sub(r":","",f_string)
    f_string = re.sub(r" 0"," _",f_string)
    out_f = f_string

with open('result.txt','w+') as f:
    f.write(out_f)
