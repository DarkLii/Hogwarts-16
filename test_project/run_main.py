# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/19
# @Desc  : Run Tests

import os
import sys
from pytest_allure.run import PytestAllure

# 工程目录，必须配置
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
if not PROJECT_PATH in sys.path:
    sys.path.insert(0, PROJECT_PATH)

if __name__ == '__main__':
    runner = PytestAllure()

    # 命令行执行
    # run_case = sys.argv[1]

    # 执行全量用例
    runner.run()

    # 执行指定用例
    # run_case = "func_1"
    # runner.run(run_case)
