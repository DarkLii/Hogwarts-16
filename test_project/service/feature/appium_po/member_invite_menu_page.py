
from appium.webdriver.common.mobileby import MobileBy
from test_project.service.feature.appium_po.base_page import BasePage
from test_project.service.feature.appium_po.contact_add import ContactAdd


class MemberInviteMenuPage(BasePage):
    """
    添加成员 PO
    """
    def add_member_manual(self):
        """
        手动添加成员信息
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAdd(self.driver)
