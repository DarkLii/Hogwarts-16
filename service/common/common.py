# -*- coding:utf-8 -*-

import os
import yaml
import pytest


def get_data(path):
    """
    读取 yaml 文件数据
    :param path: yaml文件路径
    :return: dict or list 类型数据
    """
    with open(path) as f:
        data = yaml.safe_load(f)

    return data


def format_data(data):
    """
    将数据格式化为 pytest 参数化数据
    :param data: dict 类型数据
    :return: pytest 参数化列表数据
    """
    if data and isinstance(data, dict):
        params_list = []
        for case_name, case_params in data.items():
            param = pytest.param(case_params, id=case_name)
            params_list.append(param)
        return params_list
    else:
        print("请输入 dict 类型数据")


def get_case_params(file_name):
    """
    获取 test case 参数化数据
    :param path: yaml文件名
    :return: pytest 参数化列表数据
    """
    data_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))  # 工程根目录
    path = os.path.join(data_path, "data", file_name)

    data = get_data(path)
    params_list = format_data(data)

    return params_list
