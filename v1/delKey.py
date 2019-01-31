#!/usr/bin/env python3
#coding:utf8
import redis
maxCount=50
def delSet(key):
    count=bak.scard(key)
    if count<maxCount:
        mast.delete(key)
    else:
        for i in range(count):
            mast.spop(key)
        mast.delete(key)
    print("set:"+key)
def delString(key):
    mast.delete(key)
    print("string:"+key)
def delHash(key):
    count=bak.hlen(key)
    if count<maxCount:
        mast.delete(key)
    else:
        for keyn in bak.hscan_iter(key):
            mast.hdel(key,keyn[0].decode("utf-8"))
        mast.delete(key)
    print("hash:"+key)
def delZset(key):
    count=bak.zcard(key)
    if count<maxCount:
        mast.delete(key)
    else:
        for keyn in bak.zscan_iter(key):
            mast.zrem(key,keyn[0].decode("utf-8"))
        mast.delete(key)
    print("zset:"+key)
def delList(key):
    count=bak.hlen(key)
    if count<maxCount:
        mast.delete(key)
    else:
        for i in  range(count):
            mast.lpop(key)
        mast.delete(key)
    print(type+":"+key)
#
def delKey(type,key):
    swicher = {              #定义一个map，相当于定义case：func()
        'set':delSet,
        'string':delString,
        'hash':delHash,
        'zset':delZset,
        'list':delList
    }
    func = swicher.get(type) #从map中取出方法
    return func(key)   #执行

try:
    #host is the redis host,the redis server and client are required to open, and the redis default port is 6379
    #从从节点上获取相关信息
    bakPool = redis.ConnectionPool(host='10.63.11.201', password = '123456', port=6379, db=0)
    #核心删除数据操作在主节点上执行
    mastPool = redis.ConnectionPool(host='10.63.11.202', password = '123456', port=6379, db=0)
except:
    print("could not connect to redis.")
    exit("不可连接redis 退出系统")
bak = redis.Redis(connection_pool=bakPool)
mast=redis.Redis(connection_pool=mastPool)
with open(r'C:\Users\wxy\Desktop\s.txt') as f:
    for line in f:
        keyz=line.strip()
        keyType=bak.type(keyz).decode("utf-8")
        if keyType  !='none':
            delKey(keyType,keyz)
        else:
            print("为空,不处理");

exit("结束")
