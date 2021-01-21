# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/14
# @Desc  : 测试用例父类


import os
import sys
import pytest
from pytest_allure.log.logger import Logger, Printf, AllureLog
from pytest_allure.utiles.dybanic_import import dynamic_import_module


class TestBaseCase:

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def teardownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setup_class(cls):

        path = os.getcwd()
        if path not in sys.path:
            sys.path.insert(0, path)
        module_path = cls.__module__
        module_path_list = module_path.split(".")
        module_path_list[-1] = "__init__"
        init_settings = ".".join(module_path_list)
        settings_obj = dynamic_import_module(init_settings)
        settings = settings_obj.SETTINGS

        settings_keys = settings.keys()

        cls.Log = settings["Log"]

        if "DataBase" in settings_keys:
            cls.DataBase = settings["DataBase"]
        if "Urls" in settings_keys:
            cls.Urls = settings["Urls"]
        if "UserInfo" in settings_keys:
            cls.UserInfo = settings["UserInfo"]

        cls.print = Printf
        cls.allure_log = AllureLog()
        cls.log = Logger(level=cls.Log.get("level", "info"),
                         output_file=cls.Log.get("output_file", False),
                         output_console=cls.Log.get("output_console", True),
                         console_log_color=cls.Log.get("console_log_color", False),
                         filename=os.path.join(cls.Log.get("report_path"), "test_log.log"))

        cls.log.info("Start Run: setupClass")
        cls.setupClass()

    @classmethod
    def teardown_class(cls):
        cls.log.info("Start Run: teardownClass")
        cls.teardownClass()

    def setup(self):
        self.log.info("Start Run: setUp")
        self.setUp()

    def teardown(self):
        self.log.info("Start Run: tearDown")
        self.tearDown()


if __name__ == "__main__":
    pytest.main(["-s", "-v", "base_case.py"])
