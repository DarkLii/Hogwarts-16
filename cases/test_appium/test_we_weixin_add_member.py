# -*- coding:utf-8 -*-

from service.feature.appium_po.app import App


class TestWeWeiXin:

    def setup_class(self):
        self.caps = {
            "platformName": "Android",
            "deviceName": "wework",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",  # 不清空缓存
            "ensureWebviewsHavePages": True,
            "settings[waitForIdleTimeout]": 0  # 设置页面等待空闲状态的时间
        }

        self.app = App()
        self.app.start(self.caps)

    def teardown_class(self):
        self.app.quit()

    def test_add_member(self):

        name = "wahaha"
        sex = "女"
        mobile = "13500001111"

        result = self.app.goto_main().goto_address().click_addmember().add_member_manual().add_contact(name, sex, mobile)
        assert result
