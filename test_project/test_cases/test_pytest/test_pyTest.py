# -*- coding:utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/09/02
# @Desc  :

import allure
from pytest_allure.case.base_case import TestBaseCase


@allure.feature("主要功能模块--一级标签")
class TestAllure(TestBaseCase):
    @allure.story("子功能模块--二级标签")
    @allure.title("测试用例标题")
    @allure.description("测试用例描述")
    @allure.step("测试用例步骤")
    @allure.severity(allure.severity_level.CRITICAL)
    # 或者
    @allure.severity("critical")
    # Allure 中对严重级别的定义：
    # blocker 级别：致命缺陷（客户端程序无响应，无法执行下一步操作）
    # critical 级别：严重缺陷（功能点缺失）
    # normal 级别：普通缺陷（数值计算错误）
    # minor 级别：次要缺陷（界面错误与UI需求不符）
    # trivial 级别：轻微缺陷（必输项无提示，或者提示不规范）

    # # 使用方法：@allure.attach(body, name, attachment_type, extension)
    # body - 要写入文件的原始内容
    # name - 包含文件名的字符串
    # attachment_type - 其中一个allure.attachment_type值
    # extension - 提供的将用作创建文件的扩展名

    @allure.title("测试用例标题")
    def test_1(self):
        """也可以在这里添加用例的描述信息，但是会被allure.description覆盖"""
        print("\n1")
        print("\n1")
        print("\n1")
        # 添加附件
        # with open(r"imgs/attpng.png", "rb") as f:
        #     context = f.read()
        #     allure.attach(context, "错误图片", attachment_type=allure.attachment_type.PNG)
        assert 1 == 1

    def func(self, x):
        return x + 1

    @allure.feature("运行失败")  # feature标记测试场景
    def test_answer(self):
        assert self.func(3) == 5
