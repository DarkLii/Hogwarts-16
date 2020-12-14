# -*- coding:utf-8 -*-

import pytest
from service.calculator import Calculator
from service.common.common import *


class TestCalculator:

    @classmethod
    def setup_class(cls):
        print("\nStart Run: setup_class")
        cls.calcu = Calculator()

    @classmethod
    def teardown_class(cls):
        print("\nStart Run: teardown_class")

    def setup(self):
        print("\nStart Run: setup")

    def teardown(self):
        print("\nStart Run: teardown")

    path = "data_calculator.yml"  # data 目录下 yaml 文件名
    params_list = get_case_params(path)

    @pytest.mark.parametrize("params", params_list)
    def test_calculator(self, params):
        """ 测试计算器 + - * / 功能用例 """

        operator = params["operator"]

        if operator == "+":
            assert self.calcu.add(params["a"], params["b"]) == params["expected"]
        elif operator == "-":
            assert self.calcu.sub(params["a"], params["b"]) == params["expected"]
        elif operator == "*":
            assert self.calcu.mul(params["a"], params["b"]) == params["expected"]
        elif operator == "/":
            assert self.calcu.div(params["a"], params["b"]) == params["expected"]
