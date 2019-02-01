#!/usr/bin/env python3
#coding:utf8
'''
将查询到的数据保存到文件中
'''
import redis,time
def countSet(key):
	return bak.scard(key)
def countString(key):
	return 1
def countHash(key):
    return bak.hlen(key)
def countZset(key):
    return bak.zcard(key)
def countList(key):
    return bak.hlen(key)
#获取各类型数据
def getCount(type,key):
    swicher = {              #定义一个map，相当于定义case：func()
        'set':countSet,
        'string':countString,
        'hash':countHash,
        'zset':countZset,
        'list':countList
    }
    func = swicher.get(type) #从map中取出方法
    return func(key)   #执行
def containAny(seq,aset):
    for c in seq:
         if c in aset:
                return True
    return False 
def containAnyStr(seq,aset):
    for c in seq:
         if c in aset:
                return c
try:
    #host is the redis host,the redis server and client are required to open, and the redis default port is 6379
    pool = redis.ConnectionPool(host='10.63.11.201', password = '123456', port=6379, db=0)
except:
    print("could not connect to redis.")
    exit("不可连接redis 退出系统")
bak = redis.Redis(connection_pool=pool)
matchSet=set({
 'RISK_ZBcnt00012*','ZBcnt00025*'
    })
with open(r'D:\GitHub\python-redis-util\v1\zb.txt', 'w') as out,open(r'D:\GitHub\python-redis-util\v1\error.txt', 'w') as error:
	for i in  bak.scan_iter(match=matchSet, count=10000):
		try:
			keyz=i.decode('utf-8')
			# if containAny(matchSet,keyz):
			keyType=bak.type(keyz).decode("utf-8")
			out.write(keyz+"======"+str(getCount(keyType,keyz))+"======"+str(bak.ttl(keyz)))
			out.write('\n')
		except:
			error.write(str(i))
			error.write('\n')
	out.write("is over")