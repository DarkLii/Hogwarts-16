# -*- coding:utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/15
# @Desc  : 装饰器


import time
import json
from functools import wraps


def clock(func):
    """记录函数执行时间"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} usedTime: {elapsed}")
        return result

    return wrapper


def log_wrapper(func):
    """记录函数 入参 和 返回值"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.log:
            params = ""
            if args:
                params = args
            if kwargs:
                kwargs_str = json.dumps(kwargs, ensure_ascii=True)
                if params:
                    params = f"{params} {kwargs_str}"
                else:
                    params = kwargs_str
            # 记录函数入参
            self.log.info(f"FunctionName: {func.__name__} - Params: {params}")

        ret = func(self, *args, **kwargs)

        if self.log:
            # 记录函数返回值
            self.log.info(f"FunctionName: {func.__name__} - Return: {ret}")

        # 返回函数结果
        return ret

    # 执行装饰器功能
    return wrapper
