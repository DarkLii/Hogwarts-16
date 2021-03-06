from appium.webdriver.common.mobileby import MobileBy
from test_project.service.feature.appium_po.base_page import BasePage


class ContactAdd(BasePage):
    """
    成员信息编辑
    """

    def add_contact(self, name, sex, mobile):
        """
        添加信息
        :return:
        """

        self.find_and_send(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']", name)
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, f"//*[@text='{sex}']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']", mobile)

        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        return True
