# -*- coding:utf-8 -*-


import yaml
from test_project.service.calculator import Calculator


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

    def step1(self):
        print("打开浏览器")

    def step2(self):
        print("注册账号")

    def step3(self):
        print("登录")

    path = "./step.yml"

    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
