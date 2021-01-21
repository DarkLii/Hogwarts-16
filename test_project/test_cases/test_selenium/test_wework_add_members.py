# -*- coding:utf-8 -*-

import os
import subprocess
import time
from selenium import webdriver
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
        chrome_path = "E:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            opt.binary_location = chrome_path

        # 需启动 chrome 远程调试端口(需添加 chrome.exe 环境变量)，cmd 执行：chrome
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        cls.driver = webdriver.Chrome(chrome_options=opt)
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        print("\nStart Run: teardown_class")
        cls.driver.quit()

    def setup(self):
        print("\nStart Run: setup")

    def teardown(self):
        print("\nStart Run: teardown")

    def delete_members(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()

        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".member_colRight_memberTable_tr_Inactive > .member_colRight_memberTable_td:nth-child(2) > span").click()

            self.driver.find_element_by_link_text("删除").click()
            time.sleep(1)
            self.driver.find_element_by_link_text("确认").click()

        except Exception as e:
            pass

    def test_add_members(self):

        self.delete_members()

        time.sleep(2)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()

        time.sleep(1)

        name = "test_member_01"
        mobile = "13500000000"
        title = "测试"

        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(mobile)
        self.driver.find_element(By.ID, "memberAdd_title").send_keys(title)
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .js_btn_save").click()
        # self.driver.execute_script("window.scrollTo(0,43.20000076293945)")

        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".member_colRight_memberTable_tr_Inactive > .member_colRight_memberTable_td:nth-child(2) > span").text == "test_member_01"

        self.delete_members()
