# -*- coding:utf-8 -*-
import pytest


class TestFixTure:

    def test_one(self, test_class_fixture):
        print("执行：test_one")

    def test_two(self, test_case_fixture):
        print("执行：test_two")

    def test_three(self, test_case_fixture_return):
        print(f"获取 fixture 的参数:{test_case_fixture_return}")
        print("执行：test_three")
        print("执行：test_two")

    def test_four(self, test_case_fixture_yield):
        print(f"获取 fixture 的参数:{test_case_fixture_yield}")
        print("执行：test_three")
