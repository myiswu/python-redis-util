import GetRedisConnet
class RedisUtil:
	def _init_(self,configPath):
		self.redisConnet=GetRedisConnet(configPath)