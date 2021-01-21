# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2018/05/10
# @Desc  : 动态导入模块

import sys
import importlib


def dynamic_import_module(module_path):
    """
    动态导入模块
    :param module_path: 需要导入的模块路径 x.x.x
    :return: 调入的模块
    """
    if isinstance(module_path, dict):
        modules_obj = {}
        for key, value in module_path.items():
            modules_obj[key] = importlib.import_module(value, sys.modules)
        return modules_obj
    else:
        module = importlib.import_module(module_path, sys.modules)
        return module
