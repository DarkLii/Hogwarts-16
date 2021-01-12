# -*- coding:utf-8 -*-

import os
import pytest
import time
import yaml
import shutil
import subprocess
from selenium import webdriver
from service.common.common import *
from selenium.webdriver.common.by import By


class TestWework:

    @classmethod
    def setup_class(cls):
        print("\nStart Run: setup_class")

        # 打开 chrome debug 远程调试模式，用于复用已有浏览器
        # subprocess.call(f"chrome --remote-debugging-port=9222", shell=True)
        # time.sleep(10)

        opt = webdriver.ChromeOptions()
        # 当 Chrome 未安装在默认路径时，需指定 chrome.exe 的路径，否则会报错：selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary
        chrome_path = "E:\Program Files\Google\Chrome\Application\chrome.exe"
        if os.path.exists(chrome_path):
            opt.binary_location = chrome_path

        # 需启动 chrome 远程调试端口(需添加 chrome.exe 环境变量)，cmd 执行：chrome
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        cls.driver = webdriver.Chrome(chrome_options=opt)
        cls.driver.implicitly_wait(10)
        # cls.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        # with open(we_weixin_login_cookie_file_path(), encoding="UTF-8") as f:
        #     yaml_data = yaml.safe_load(f)
        #     for cookie in yaml_data:
        #         cls.driver.add_cookie(cookie)

    @classmethod
    def teardown_class(cls):
        print("\nStart Run: teardown_class")
        cls.driver.quit()

    def setup(self):
        print("\nStart Run: setup")

    def teardown(self):
        print("\nStart Run: teardown")

    # 获取cookie，序列化后存入yaml文件内
    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = self.driver.get_cookies()
        print(cookie)
        with open(we_weixin_login_cookie_file_path(), "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    # 使用序列化cookie的方法进行登录
    def test_add_members(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()

        time.sleep(1)

        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element(By.ID, "username").send_keys("test_member_01")
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("test_member_01")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("test_member_01")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13500000000")
        self.driver.find_element(By.ID, "memberAdd_title").send_keys("测试")
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .js_btn_save").click()
        # self.driver.execute_script("window.scrollTo(0,43.20000076293945)")

        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".member_colRight_memberTable_tr_Inactive > .member_colRight_memberTable_td:nth-child(2) > span").text == "test_member_01"

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".member_colRight_memberTable_tr_Inactive > .member_colRight_memberTable_td:nth-child(2) > span").click()

        time.sleep(5)

        self.driver.find_element_by_link_text("删除").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("确认").click()

        time.sleep(5)
