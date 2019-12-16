from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
import time

ADDR_VISIT = {}


class TestThrottle(object):
    """自定义节流类(根据IP实现).也可简单继承BaseThrottle'"""
    def __init__(self):
        self.history = []

    def allow_request(self, request, view):
        ctime = time.time()
        # 获取IP。如果从request取某个属性取不到，则会到request._request中去取
        remote_addr = request.META.get('REMOTE_ADDR')
        if remote_addr not in ADDR_VISIT:
            ADDR_VISIT[remote_addr] = [ctime,]
            return True
        history = ADDR_VISIT.get(remote_addr)
        self.history = history
        # 最早的一个访问时间如果如果小于当前时间减60秒则移除掉此访问时间记录
        while history and history[-1] < ctime - 60:
            history.pop()
        # 多长时间内最多访问的次数
        if len(history) < 3:
            history.insert(0, ctime)
            return True

    def wait(self):
        '''还需要等多长时间才可访问'''
        ctime = time.time()
        return 60 - (ctime - self.history[-1])


class VisitThrottle(SimpleRateThrottle):
    """继承SimpleRateThrottle节流类：可简单配置访问频率"""
    # 配置文件中 DEFAULT_THROTTLE_RATES 的key名. 'THROTTLE_RATES': {'MyThrottleVIP': '10/m'} # 10/m表示每分钟访问10次
    scope = 'VisitThrottle'

    def get_cache_key(self, request, view):
        # 返回IP地址
        return self.get_ident(request)


class VIPThrottle(SimpleRateThrottle):
    scope = 'VIPThrottle'

    def get_cache_key(self, request, view):
        # 返回用户名为缓存key
        return request.user.username