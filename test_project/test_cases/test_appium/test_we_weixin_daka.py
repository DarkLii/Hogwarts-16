# -*- coding:utf-8 -*-

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWeWeiXin:

    def setup_class(self):
        caps = {
            "platformName": "Android",
            "deviceName": "wework",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true",  # 不清空缓存
            "ensureWebviewsHavePages": True,
            "settings[waitForIdleTimeout]": 0  # 设置页面等待空闲状态的时间
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)  # 全局隐式等待，只针对 find_element 方法生效

    def teardown_class(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()

        # 滚动查找元素  固定用法
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source
