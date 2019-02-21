#!/usr/bin/env python3
#coding:utf8
import redis
def convertKeyValue(oldKey,newKey):
	'''通过此方法完成2个key之间value的转换需要自定义转化的规则'''
	mast.setnx(newKey,mast.get(oldKey).decode("utf-8"))

def getNewKey(oldKey):
	oldKeyS=oldKey.split(r"|")
	oldKeyS[0]="RISK_x"
	oldKeyS[1]="2"
	newKey= "|".join(oldKeyS)
	print("newKey="+newKey)
	return newKey

try:
     #核心删除数据操作在主节点上执行
    mastPool = redis.ConnectionPool(host='10.63.11.202', password = '123456', port=6379, db=0)
except:
    print("could not connect to redis.")
    exit("不可连接redis 退出系统")
mast=redis.Redis(connection_pool=mastPool)
match="RISK_ZBlp000011*"
for i in  mast.scan_iter(match=match, count=4000):
	keyz=i.decode("utf-8")
	print(keyz)
	try:
		convertKeyValue(keyz,getNewKey(keyz))
	except  Exception as e:
		print("赋值出现异常"+e)
print("结束")
	
	
