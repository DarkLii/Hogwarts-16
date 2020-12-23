# -*- coding:utf-8 -*-

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from service.feature.page_object.we_weixin.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_add = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _location_add_department = (By.CSS_SELECTOR, ".js_create_party")
    _location_get_department = (By.CSS_SELECTOR, ".jstree-icon.jstree-themeicon")


    def goto_add_member(self):
        # 解决循环导入的问题
        from service.feature.page_object.we_weixin.add_member_page import AddMember
        """
        添加成员操作
        :return:
        """

        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return:
        """
        member_list = self.finds(*self._location_member_list)
        # 列表推导式
        member_list_res = [i.text for i in member_list]
        return member_list_res

    def goto_add_department(self):
        # 解决循环导入的问题
        from service.feature.page_object.we_weixin.add_department_page import AddDepartment
        """
        添加部门操作
        :return:
        """
        self.find(self._location_add).click()
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_add_department).click()

        return AddDepartment(self.driver)

    def get_department(self):
        """
        获取一级部门
        :return:
        """
        res = self.find(self._location_get_department)
        return res


