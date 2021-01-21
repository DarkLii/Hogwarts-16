# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/19
# @Desc  : Running Tests

import os
import sys
import shutil
import pytest
import subprocess
from pytest_allure.report.report import generate_test_report
from pytest_allure.utiles.dybanic_import import dynamic_import_module


class PytestAllure:
    """
    测试用例执行入口类
    """

    def __init__(self):

        path = os.getcwd()
        if path not in sys.path:
            sys.path.insert(0, path)
        init_settings = "__init__"
        settings = dynamic_import_module(init_settings)
        self.SETTINGS = settings.SETTINGS
        self.PROJECT_PATH = settings.PROJECT_PATH

    def run(self, run_case="ALL"):
        """
        执行测试用例入口方法
        :param run_case: 需要执行的测试用例，来源于工程内setting的Case测试用例配置的key
        :return:
        """
        run_params = []

        # 报告路径
        report_path = self.SETTINGS["Log"]["report_path"]
        # 删除以后报告，防止allure生成的报告不准确
        if os.path.exists(report_path):
            shutil.rmtree(report_path)
        allure_result_path = os.path.join(report_path, "allure_result")
        allure_report_path = os.path.join(report_path, "allure_report")

        # 获取测试用例
        case_list = self._init_test_case(run_case, self.SETTINGS["Case"], self.PROJECT_PATH)

        run_params.extend(case_list)

        # 添加参数 使用 allure 生成测试结果
        allure_params = ["--alluredir", allure_result_path]
        run_params.extend(allure_params)

        # 运行测试用例
        pytest.main(run_params)

        # 生成 report_json 文件，主要用于 Jenkins 发送邮件时获取测试结果数据
        generate_test_report(report_path, allure_result_path)

        # 使用 allure 生成测试报告
        subprocess.call(f"allure generate {allure_result_path} -o {allure_report_path} --clean", shell=True)
        #  自动打开 allure HTML 报告
        subprocess.call(f"allure open {allure_report_path}", shell=True)

    def _init_test_case(self, run_case, case_config, project_path):
        """
        初始化需要测试用例
        :param case: 需要执行的用例
        :param case_config: 已配置的用例集
        :param project_path: 工程目录
        :return:
        """
        case_path_list = []

        if run_case.upper() == "ALL":
            [case_path_list.extend(case_config.get(case_path)) for case_path in case_config.keys() if
             case_config.get(case_path)]
        else:
            case_path_list = case_config.get(run_case, None)
        if not case_path_list:
            raise Exception(f"根据：{run_case} 没有找到对应的自动化用例")

        case_list = []
        for case_path in case_path_list:
            case_dir_list = case_path.split(".")

            case_real_dir = project_path

            # 将 用例目录 拼接到路径
            for case_dir in case_dir_list:
                case_real_dir = os.path.join(case_real_dir, case_dir)

            if os.path.isdir(case_real_dir):
                # 查找 case_real_dir 下所有测试用例文件
                def get_case_files(path, suffix):
                    return [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files if
                            file.endswith(suffix) and not file.startswith("_")]

                case_file_list = get_case_files(case_real_dir, ".py")

                case_list.extend(case_file_list)
            else:
                case_real_dir += ".py"
                if os.path.exists(case_real_dir):
                    case_list.append(case_real_dir)

        return case_list
