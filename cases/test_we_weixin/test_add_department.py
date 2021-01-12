# -*- coding:utf-8 -*-

import pytest

from service.feature.selenium_po.we_weixin.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        # 第一次实例化
        self.main = MainPage()

    # 回复到首页还原一开始的状态
    def teardown(self):
        # self.main.back_main()
        pass

    def teardown_class(self):
        # 退出浏览器
        self.main.quit()
        pass

    def test_add_department(self):
        """添加成员测试用例
        :return:
        """
        # 1.跳转添加成员页面  2. 添加成员  3. 自动跳转到通讯录页面  4. 查找新增的部门
        department_name = "一级部门"
        res = self.main.goto_contact().goto_add_department().add_department_seccess(department_name).get_department()
        assert department_name in res
