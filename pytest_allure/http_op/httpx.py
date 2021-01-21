# -*- coding:utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/09/02
# @Desc  : requests 封装


import json
import httpx
import threading
from pytest_allure.utiles.decorator import log_wrapper


class HttpX:

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with threading.Lock():  # 多线程加锁
                cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, obj, headers=None, timeout=5):

        self.log = obj.log if hasattr(obj, "log") else None

        self.client = httpx.Client()
        self.headers = headers
        self.timeout = timeout
        self.cookies = None
        self.response_cookies = None

    def set_timeout(self, timeout):
        self.timeout = timeout

    def set_headers(self, headers):
        self.headers = headers

    def set_cookies(self, cookies):
        self.cookies = cookies

    def get_cookies(self):
        return self.response_cookies

    @log_wrapper
    def request(self, url, params=None, json_str=None, data=None, method=None):
        """
        Http 请求
        :param url:
        :param params:
        :param json:
        :param data:
        :param method:
        :return:
        """

        # if self.log:
        #     request_params = {}
        #     request_params["Url"] = url
        #     request_params["Params"] = params
        #     request_params["Json"] = json_str
        #     request_params["Data"] = data
        #     request_params["Method"] = method
        #     request_params["Headers"] = self.headers
        #     request_params["Cookies"] = self.cookies
        #     self.log.info(f"Start Request: {json.dumps(request_params, ensure_ascii=True)}")

        data = data if data and isinstance(data, dict) else json.dumps(data, ensure_ascii=True)
        json_str = json_str if json_str and isinstance(json_str, dict) else json.dumps(json_str, ensure_ascii=True)

        method = method.upper()
        if method == "GET":
            response = self.client.get(url=url, params=params,
                                       headers=self.headers, cookies=self.cookies, timeout=self.timeout)
        elif method == "PUT":
            response = self.client.put(url=url, params=params, json=json_str, data=data,
                                       headers=self.headers, cookies=self.cookies, timeout=self.timeout)
        elif method == "POST":
            response = self.client.post(url=url, params=params, json=json_str, data=data,
                                        headers=self.headers, cookies=self.cookies, timeout=self.timeout)
        else:
            response = self.client.delete(url=url, params=params,
                                          headers=self.headers, cookies=self.cookies, timeout=self.timeout)

        self.response_cookies = response.cookies

        try:
            try:
                result = response.json()
            except Exception as e:
                result = response.text[0:1100]  # 长度太长logging打印日志会报错
        except Exception as e:
            # if self.log:
            #     self.log.exception(f"Request Exception: {e}")
            result = response

        return result

    def get(self, url, params=None):
        return self.request(url, params=params, method="GET")

    def post(self, url, params=None, json_str=None, data=None):
        return self.request(url, params=params, json_str=json_str, data=data, method="POST")

    def put(self, url, params=None, json_str=None, data=None):
        return self.request(url, params=params, json_str=json_str, data=data, method="PUT")

    def delete(self, url, params=None, json_str=None, data=None):
        return self.request(url, params=params, json_str=json_str, data=data, method="DELETE")

    def download(self, url, file, file_name):
        pass

    def upload(self, url, files):
        pass

    def close(self):
        if self.client:
            self.client.close()
            if self.log:
                self.log.info("断开 Session 连接")


if __name__ == '__main__':
    pass
