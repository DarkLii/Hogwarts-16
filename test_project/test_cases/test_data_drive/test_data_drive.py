# # -*- coding:utf-8 -*-
#
# import pytest
# from test_project.service.calculator import Calculator
# from test_project.service.common.common import get_case_params
#
#
# class TestCalculator:
#
#     @classmethod
#     def setup_class(cls):
#         print("\nStart Run: setup_class")
#         cls.calcu = Calculator()
#
#     @classmethod
#     def teardown_class(cls):
#         print("\nStart Run: teardown_class")
#
#     path = "data_calculator.yml"  # data 目录下 yaml 文件名
#     params_list = get_case_params(path)
#
#     @pytest.mark.run(order=2)
#     @pytest.mark.parametrize("params", params_list)
#     def test_calculator(self, params, test_case_fixture):
#         """ 测试计算器 + - * / 功能用例 """
#
#         operator = params["operator"]
#
#         if operator == "+":
#             assert self.calcu.add(params["a"], params["b"]) == params["expected"]
#         elif operator == "-":
#             assert self.calcu.sub(params["a"], params["b"]) == params["expected"]
#         elif operator == "*":
#             assert self.calcu.mul(params["a"], params["b"]) == params["expected"]
#         elif operator == "/":
#             assert self.calcu.div(params["a"], params["b"]) == params["expected"]
#
#     @pytest.mark.run(order=1)
#     def test_one(self):
#         print("第一个运行的测试用例")
#         pass
