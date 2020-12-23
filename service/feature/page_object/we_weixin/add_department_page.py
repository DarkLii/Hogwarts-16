# -*- coding:utf-8 -*-

from time import sleep
from selenium.webdriver.common.by import By

from service.feature.page_object.we_weixin.base_page import BasePage
from service.feature.page_object.we_weixin.contact_page import ContactPage


class AddDepartment(BasePage):

    _location_department_name = (By.CSS_SELECTOR, ".qui_inputText.ww_inputText")
    _location_select_department = (By.CSS_SELECTOR, ".js_toggle_party_list")
    # _location_define_department = (By.CSS_SELECTOR, ".jstree-anchor.jstree-clicked")
    _location_define_department = (By.ID, "1688850998173016_anchor")
    _location_define_submit = (By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_btn_Blue")

    def add_department_seccess(self):
        """
        添加部门操作
        :return:
        """
        self.finds(self._location_department_name)[1].send_keys("一级部门")
        self.find(self._location_select_department).click()
        # a = self.finds(self._location_define_department)
        self.finds(self._location_define_department)[-1].click()
        self.finds(self._location_define_submit)[-1].click()

        return ContactPage(self.driver)
