# -*- coding: utf-8 -*-

import os

TEST_ENV = {
    # 报告配置 PS：不能缺失
    "Log": {
        "level": "INFO",
        "output_console": True,
        "output_file": False,
        "console_log_color": False,  # 当从入口 run 函数执行用例时，请设置为 False，否则 allure 报告有奇怪的东西乱入
        "report_path": os.path.join(os.path.dirname(__file__), "report")
    },

    # 数据库配置
    "DataBase": {
        "redis_1": {
            "engine": "redis",
            "host": "xxx",
            "port": 6379,
            "database": 1,
            "user": "xxx",
            "password": "xxx",
        },
        "mysql_1": {
            "engine": "mysql",
            "host": "xxx",
            "port": 3306,
            "database": "xxx",
            "user": "xxx",
            "password": "xxx",
        }
    },

    # url 配置
    "Urls": {
        "bai_du": "https://www.baidu.com/",
        "google": "https://www.google.com/"
    },

    # 测试用例配置 后期考虑将用例配置独立出去 原因：用例涉及到频繁改动，但其它基础配置一般不会改动
    "Case": {
        "test_appium": ["test_cases.test_appium"],
        "test_data_drive": ["test_cases.test_data_drive"],
        "test_pytest": ["test_cases.test_pytest"],
        "test_selenium": ["test_cases.test_selenium"],
        "test_we_weixin": ["test_cases.test_we_weixin"],
    },

    # 登录用户配置
    "UserInfo": {
        "user_1": {
            "user_name": "xxx",
            "password": "xxx",
            "uid": "xxx"
        },
        "user_2": {
            "user_name": "xxx",
            "password": "xxx",
            "uid": "xxx"
        }
    },

}

UAT_ENV = {}

ENV_TYPE = "TEST"

if ENV_TYPE == "TEST":
    SETTINGS = TEST_ENV
elif ENV_TYPE == "UAT":
    SETTINGS = UAT_ENV
