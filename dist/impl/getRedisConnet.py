import ConfigParser
class GetRedisConnet:
    '''通过此方法获取多种redis连接,暂时只支持从seninel
获取主节点以及直接配置相关节点信息直接获取'''
    def _init_(self,redisConfig):



    def __parserConf__(redisConfig):
		conf = ConfigParser.ConfigParser()
		conf.read(redisConfig)       # 文件路径
		
