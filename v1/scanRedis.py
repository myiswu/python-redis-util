#!/usr/bin/env python3
#coding:utf8
import redis
try:
    #host is the redis host,the redis server and client are required to open, and the redis default port is 6379
    pool = redis.ConnectionPool(host='10.63.11.201', password = '123456', port=6379, db=0)
    print("connected success.")
except:
    print("could not connect to redis.")
    exit("不可连接redis 退出系统")
r = redis.Redis(connection_pool=pool)
matchSet=set({
'RISK_ZBavg*|*|*','RISK_ZBsum*|*|* ','RISK_ZBcnt*|*|*',
'RISK_ZBmin*|*|*','RISK_ZBmax*|*|*','RISK_ZBactd*|*|*','RISK_ZBlink*|*|*'
    })
for match in matchSet:
    for i in  r.scan_iter(match=match, count=10000):
        print(i.decode('utf-8'))
exit("结束")
