# -*- coding:utf-8 -*-

import os
import yaml
from selenium import webdriver
from service.common.service_selenium import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            options = webdriver.ChromeOptions()
            # 需启动 chrome 远程调试端口(需添加 chrome.exe 环境变量)，cmd 执行：chrome --remote-debugging-port=9222
            # subprocess.call(f"chrome --remote-debugging-port=9222", shell=True)
            # 设置debug地址
            # options.debugger_address = "127.0.0.1:9222"
            # 当 Chrome 未安装在默认路径时，需指定 chrome.exe 的路径，否则会报错：cannot find Chrome binary
            chrome_path = "E:\Program Files\Google\Chrome\Application\chrome.exe"
            if os.path.exists(chrome_path):
                options.binary_location = chrome_path
                self.driver = webdriver.Chrome(chrome_options=options)
            else:
                self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            # self.__get_cookie()
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def __cookie_login(self):
        # 使用cookie登录
        with open(we_weixin_login_cookie_file_path(), encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 获取cookie，序列化后存入yaml文件内
    def __get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = self.driver.get_cookies()
        with open(we_weixin_login_cookie_file_path(), "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)
        print("获取网页版企业微信 cookie 成功")

    def find(self, by, value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)

    def wait_click(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        """退出二次封装
        :return:
        """
        self.driver.quit()
