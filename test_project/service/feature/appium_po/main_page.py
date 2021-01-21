
from appium.webdriver.common.mobileby import MobileBy
from test_project.service.feature.appium_po.addresss_list_page import AddresssListPage
from test_project.service.feature.appium_po.base_page import BasePage


class MainPage(BasePage):
    """
    首页 PO
    """
    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        # self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/dqn']")
        return AddresssListPage(self.driver)
