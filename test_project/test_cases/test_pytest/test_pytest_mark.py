# # -*- coding:utf-8 -*-
#
# import pytest
# from test_project.service.calculator import Calculator
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
#     def setup(self):
#         # print("Start Run: setup")
#         pass
#
#     def teardown(self):
#         # print("Start Run: teardown")
#         pass
#
#     @pytest.mark.demo
#     def test_demo(self):
#         run_cli = 'ytest -sv -m "demo" '
#         print(run_cli)
#
#     @pytest.mark.smork
#     def test_smork(self):
#         run_cli = 'ytest -sv -m "smork" '
#         print(run_cli)
#         # pytest.assume(1 == 2)
#         pytest.assume(1 == 1)
#         # pytest.assume(2 == 3)
#         print(1)
