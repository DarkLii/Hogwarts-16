from appium.webdriver.common.mobileby import MobileBy
from service.feature.appium_po.base_page import BasePage
from service.feature.appium_po.member_invite_menu_page import MemberInviteMenuPage


class AddresssListPage(BasePage):
    """
    通讯录 PO
    """

    def click_addmember(self):
        """
        添加成员
        :return:
        """

        # self.scroll_find_click("添加成员")
        self.swip_find_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return MemberInviteMenuPage(self.driver)
