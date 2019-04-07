#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename:juhe.py

import os
import codecs, sys
import re
import time
import json
from IPy import IP, IPSet
import cgi, cgitb
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

start_time = time.time()

#获取post过来的数据
form = cgi.FieldStorage()
IPS = form.getvalue('IPS')

print("Content-type: application/json")
print()

#取条目数
IPS = json.loads(IPS)
process_before = len(IPS)

result = IPSet()
for item in IPS:
    try:
        result.add(IP(item))
    except ValueError as e:
        result_json ={}
        result_json['ips'] = ['{0}'.format(e)]
        result_json['process_before'] = '0'
        result_json['process_after'] = '0'
        result_json['elapsed']  = '0.0000'
        #生成JSON数据
        print(json.dumps(result_json))
        sys.exit()

ips = []
for item in result:
    ips.append(item.strNormal(1) + '/32' if ('/' not in item.strNormal(1)) item.strNormal(1))
        
end_time = time.time()
result_json ={}
#聚合前的条目数
result_json['process_before'] = '{0}'.format(process_before)
        
#聚合后的条目数
result_json['process_after'] = '{0}'.format(len(ips))
        
#聚合耗时
result_json['elapsed']  = '{0:.4f}s'.format(end_time - start_time)
        
#聚合结果
result_json['ips'] = ips
        
#生成JSON数据
print(json.dumps(result_json))
