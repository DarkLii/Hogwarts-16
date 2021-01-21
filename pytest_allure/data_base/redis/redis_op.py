# -*- coding:utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/28
# @Desc  : redis 操作封装


import json
from redis import StrictRedis, ConnectionPool
from pytest_allure.utiles.decorator import log_wrapper


class RedisOp:

    def __init__(self, obj, data_base_config):

        # if hasattr(obj, "Log") and obj.Log.get("output_console", True):
        #     self.log = Logger(level="info")
        # else:
        #     self.log = None

        self.log = obj.log if hasattr(obj, "log") else None

        self.host = data_base_config["host"]
        self.port = data_base_config["port"]
        self.user = data_base_config["user"]
        self.password = data_base_config["password"]
        self.db = data_base_config["database"]
        self.charset = data_base_config.get("charset", "UTF-8")
        self.decode_responses = data_base_config.get("decode_responses", True)

        self.pool = ConnectionPool(host=self.host, port=self.port, password=self.password, db=self.db,
                                   decode_responses=self.decode_responses)
        # 获取连接
        self.connection = StrictRedis(connection_pool=self.pool)

    def close(self):
        # 关闭连接池所有连接，PS：慎用
        self.connection.connection_pool.disconnect()

    """
    string 类型 redis 操作：{"key": "value"}
    """

    @log_wrapper
    def set(self, key, value, time=None):
        """
        单条插入 key_value
        :param key:
        :param value:
        :param time: 单位为秒
        :return:
        """
        if isinstance(value, dict):
            value = json.dumps(value, ensure_ascii=False)
        if time:
            ret = self.connection.setex(key, time, value)
        else:
            ret = self.connection.set(key, value)
        return ret

    @log_wrapper
    def setnx(self, key, value):
        """
        key 不存在时 插入数据
        :param key:
        :param value:
        :return:
        """
        return self.connection.setnx(key, value)

    @log_wrapper
    def psetex(self, name, time_ms, value):
        """
        插入含过期时间的 key_value
        :param name:
        :param time_ms: 单位为毫秒
        :param value:
        :return:
        """
        return self.connection.psetex(name, time_ms, value)

    @log_wrapper
    def mset(self, key_value_dict):
        """
        批量插入 key_value
        :param key_value_dict:
        :return:
        """
        for key, value in key_value_dict.items():
            if isinstance(value, dict):
                key_value_dict[key] = json.dumps(value, ensure_ascii=False)

        return self.connection.mset(key_value_dict)

    @log_wrapper
    def msetnx(self, key_value_dict):
        """
        key 均不存在时才插入
        :param key_value_dict:
        :return:
        """
        return self.connection.msetnx(key_value_dict)

    @log_wrapper
    def get(self, key):
        """
        获取 key 的 value
        :param key:
        :return:
        """
        return self.connection.get(key)

    @log_wrapper
    def mget(self, key_list):
        """
        回多个 key 对应的 value
        :param key_list: 格式为 列表
        :return:
        """
        return self.connection.mget(key_list)

    @log_wrapper
    def getset(self, key):
        """
        给数据库中 key 赋予值 value 并返回上次的 value
        :param key:
        :return:
        """
        return self.connection.getset(key)

    @log_wrapper
    def keys(self, key):
        """
        获取所有符合规则的 key
        :param key: eg: "n*"
        :return:
        """
        return self.connection.keys(key)

    """
    redis key 操作
    """

    @log_wrapper
    def exists(self, key):
        """
        判断 key 是否存在
        :param key:
        :return:
        """
        return self.connection.exists(key)

    @log_wrapper
    def expire(self, key, time):
        """
        设定key的过期时间，单位秒
        :param key:
        :param time: 单位秒
        :return:
        """
        return self.connection.expire(key, time)

    @log_wrapper
    def delete(self, key):
        """
        删除一个 key
        :param key:
        :return:
        """
        return self.connection.delete(key)

    @log_wrapper
    def mdelete(self, key_list):
        """
        删除多个指定的 key
        :param key_list:
        :return:
        """
        for key in key_list:
            self.connection.delete(key)

    """
    hash 类型 redis 操作：{"name":{"key": "value"}}
    """
    # TODO hash 类型 redis 操作

    """
    list 类型 redis 操作：{"key": []}
    """
    # TODO list 类型 redis 操作


if __name__ == '__main__':
    data_base_config = {
        "host": "172.16.11.127",
        "port": 6379,
        "database": 13,
        "user": "root",
        "password": "standalone_passwd_test",
    }

    data_base = RedisOp(data_base_config)

    test_key = "test_key"
    test_value = "test_value"
    data_base.set(test_key, test_value)
    data_base.get(test_key)

    key_value_dict = {
        "mset_key_1": {"mset_key_111": "mset_value_111"},
        "mset_key_2": {"mset_key_222": "mset_value_222"},
    }
    data_base.mset(key_value_dict)

    key_list = [test_key, "mset_key_1", "mset_key_2"]
    data_base.mdelete(key_list)
