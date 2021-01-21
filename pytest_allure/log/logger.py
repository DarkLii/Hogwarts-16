# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/15
# @Desc  : logging 封装

import json
import allure
import logging
import threading
from functools import wraps
from logging import handlers
from pytest_allure.utiles.timer import cur_datetime_ms


class Logger(logging.Logger):
    # 日志级别映射
    level_relations = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with threading.Lock():  # 多线程加锁
                cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, level='info', output_console=True, output_file=False,
                 console_log_color=False, when='D', backCount=10, filename='test_log.log',
                 format='[%(asctime)s] - [%(levelname)8s] - [thread:%(thread)s]-[process:%(process)s]: %(message)s'):

        super(Logger, self).__init__(self)
        # format = '[%(asctime)s] - [%(levelname)8s] - [thread:%(thread)s]-[process:%(process)s] - "%(pathname)s:%(lineno)d": %(message)s'
        self.format = format
        self.output_console = output_console
        self.console_log_color = console_log_color
        self.color = ""

        self.logger = logging.getLogger()

        # 设置日志格式
        self.log_format = logging.Formatter(self.format)

        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level.upper(), logging.INFO))

        if self.output_console:
            # 往屏幕上输出
            self.console = logging.StreamHandler()
            # 设置屏幕上显示的格式
            self.console.setFormatter(self.log_format)

        if output_file:
            # 往文件里写入
            output_file = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                                            encoding='utf-8')
            # 设置文件里写入的格式
            output_file.setFormatter(self.log_format)
            # 判断是否已有handlers，防止多个地方实例化Logger导致重复打印日志
            if output_file not in self.logger.handlers:
                # 把对象加到logger里，输出日志
                self.logger.addHandler(output_file)

    def _add_console_handler(self, color, message=None):
        """
        添加 console handler
        :param color: 颜色种类，更改控制台输出的日志颜色
        :return:
        """
        if self.output_console:
            if self.console_log_color:
                self.color = color % message
                self.console.setFormatter(logging.Formatter(color % self.format))
                self.logger.addHandler(self.console)
            else:
                self.logger.addHandler(self.console)

    def _remove_console_handler(self):
        if hasattr(self, "console"):
            self.logger.removeHandler(self.console)
        pass

    def debug(self, message=None):
        """
        输出调试信息
        :param message: 调试信息
        :return:
        """
        self._add_console_handler('\033[0;32m%s\033[0m')
        self.logger.debug(msg=message)
        self._remove_console_handler()

    def info(self, message=None):
        """
        输出程序运行详细信息
        :param message: 详细信息
        :return:
        """
        self._add_console_handler('\033[0;31m%s\033[0m')
        self.logger.info(msg=message)
        self._remove_console_handler()

    def warning(self, message=None):
        """
        输出程序运行警告信息
        :param message: 警告信息
        :return:
        """
        self._add_console_handler('\033[0;37m%s\033[0m')
        self.logger.warning(msg=message)
        self._remove_console_handler()

    def error(self, message=None):
        """
        输出程序运行错误信息
        :param message: 错误信息
        :return:
        """
        self._add_console_handler('\033[0;34m%s\033[0m')
        self.logger.error(msg=message)
        self._remove_console_handler()

    def exception(self, message=None):
        """
        输出程序运行异常信息
        :param message: 异常信息
        :return:
        """
        self._add_console_handler('\033[0;34m%s\033[0m')
        self.logger.exception(msg=message)
        self._remove_console_handler()

    def critical(self, message=None):
        """
        输出程序运行严重错误信息
        :param message: 错误信息
        :return:
        """
        self._add_console_handler('\033[0;35m%s\033[0m')
        self.logger.critical(msg=message)
        self._remove_console_handler()


class AllureLog:
    # 在allure report中记录日志

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with threading.Lock():  # 多线程加锁
                cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def _init_title(self, title):
        """
        记录日志时间
        :param title: 日志抬头
        :return:
        """
        title = f"{cur_datetime_ms()}: {title}"
        return title

    def text(self, title, message=None, format=True):
        """
        记录 allure test 类日志
        :param title: 日志抬头
        :param message: 日志内容
        :return:
        """
        title = self._init_title(title)
        if format:
            try:
                message = str(message) if isinstance(message, set) else message
                message = message if not isinstance(message, (dict, list, tuple)) else json.dumps(message,
                                                                                                  ensure_ascii=False)
            except Exception as e:
                message = str(message)

        allure.attach(message, title, allure.attachment_type.TEXT)


class Printf:

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with threading.Lock():  # 多线程加锁
                cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, message):
        """
        打印带有时间格式的调试信息
        :param message:
        """
        print(f"[{cur_datetime_ms()}] - [Print] - {message}")


def log_wrapper(func):
    """
    记录函数 入参 和 返回值
    :param func:
    :return:
    """
    log = Logger(level='debug')

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 记录函数入参
        params = ""
        if args:
            params = f"{args}"
        if kwargs:
            if params:
                params = params + f", {kwargs}"
            else:
                params = f"{kwargs}"

        log.info(f"FunctionName: {func.__name__} - Params: {params}")

        ret = func(*args, **kwargs)

        # 记录函数返回值
        log.info(f"FunctionName: {func.__name__} - Return: {ret}")

        # 返回函数结果
        return ret

    # 执行装饰器功能
    return wrapper


if __name__ == '__main__':
    print(f'Print: {id(Printf("Print 日志 1"))}')
    print(f'Print: {id(Printf("Print 日志 2"))}')
    print(f'Print: {id(Printf("Print 日志 3"))}')

    log = Logger(level='debug', console_log_color=True)
    log.debug('debug')
    print(id(log))
    log = Logger(level='debug', console_log_color=True)
    log.info('info')
    print(id(log))
    log = Logger(level='debug', console_log_color=True)
    log.warning('warning')
    print(id(log))
    log = Logger(level='debug', console_log_color=True)
    log.error('error')
    print(id(log))
    log = Logger(level='debug', console_log_color=True)
    try:
        raise ValueError('An error happend !')
    except ValueError as e:
        log.exception('exception')
    print(id(log))
    log = Logger(level='debug', console_log_color=True)
    log.critical('critical')
    print(id(log))

    # def task():
    #     obj = Logger(level='debug', console_log_color=True)
    #     print(id(obj))
    #
    #
    # for i in range(10):
    #     t = threading.Thread(target=task)
    #     t.start()
