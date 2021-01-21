# -*- coding:utf-8 -*-

from time import sleep
from selenium.webdriver.common.by import By
from test_project.service.feature.selenium_po.we_weixin.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_add = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _location_add_department = (By.CSS_SELECTOR, ".js_create_party")
    _location_get_department = (By.CSS_SELECTOR, ".jstree-children")
    _location_delete_department = (By.CSS_SELECTOR, ".icon.jstree-contextmenu-hover")


    def goto_add_member(self):
        # 解决循环导入的问题
        from test_project.service.feature.selenium_po.we_weixin import AddMember
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
        from test_project.service.feature.selenium_po.we_weixin.add_department_page import AddDepartment
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
        sleep(2)
        return self.find(self._location_get_department).text

    def delete_department(self):
        """
        刪除一级部门
        :return:
        """

        # self.finds(self._location_delete_department).click()
        a = self.finds(self._location_delete_department)[1].click()
        pass


