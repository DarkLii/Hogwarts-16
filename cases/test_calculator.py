# -*- coding:utf-8 -*-

import pytest
from service.calculator import Calculator


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

    # 入参
    params_add = [
        pytest.param({"operator": "+", "a": 1, "b": 2, "expected": 3}, id="test_case_001:1 + 2"),
        pytest.param({"operator": "+", "a": -1, "b": -2, "expected": -3}, id="test_case_002: -1 + (-2)"),
        pytest.param({"operator": "-", "a": 1, "b": 2, "expected": -1}, id="test_case_003: 1 - 2"),
        pytest.param({"operator": "-", "a": -1, "b": -2, "expected": 1}, id="test_case_004: -1 - (-2)"),
        pytest.param({"operator": "*", "a": 1, "b": 2, "expected": 2}, id="test_case_005: 1 * 2"),
        pytest.param({"operator": "*", "a": -1, "b": -2, "expected": 2}, id="test_case_006: -1 * (-2)"),
        pytest.param({"operator": "/", "a": 1, "b": 2, "expected": 0.5}, id="test_case_007: 1 / 2"),
        pytest.param({"operator": "/", "a": -1, "b": -2, "expected": 0.5}, id="test_case_008: -1 / (-2)"),
    ]

    @pytest.mark.parametrize("params", params_add)
    def test_calculator(self, params):

        operator = params["operator"]

        if operator == "+":
            assert self.calcu.add(params["a"], params["b"]) == params["expected"]
        elif operator == "-":
            assert self.calcu.sub(params["a"], params["b"]) == params["expected"]
        elif operator == "*":
            assert self.calcu.mul(params["a"], params["b"]) == params["expected"]
        elif operator == "/":
            assert self.calcu.div(params["a"], params["b"]) == params["expected"]
