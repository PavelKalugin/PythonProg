#!/usr/bin/python3.10

import re

out_f = ""

with open('/proc/meminfo') as f:
    f_string = f.read()
    f_string = re.sub(r":","",f_string)
    f_list = f_string.split('\n')
    f_dict = {}
    for i in f_list:
        try:
            x = re.search(r" \d+", i)
            f_dict[i] = int(x.group(0))
        except:
            pass
    sorted_keys = sorted(f_dict, key=f_dict.get,reverse=True)
    for i in sorted_keys:
        out_f+=re.sub(r" 0"," _",i)+'\n'
    print(out_f)

with open('result.txt','w+') as f:
    f.write(out_f)
