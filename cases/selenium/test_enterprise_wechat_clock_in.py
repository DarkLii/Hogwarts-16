# -*- coding:utf-8 -*-

import pytest
from time import sleep
from selenium import webdriver
from service.common.common import *
from service.calculator import Calculator


class TestCalculator:

    @classmethod
    def setup_class(cls):
        wb = webdriver.chrome
        print("\nStart Run: setup_class")

    @classmethod
    def teardown_class(cls):
        print("\nStart Run: teardown_class")

    def setup(self):
        print("\nStart Run: setup")

    def teardown(self):
        print("\nStart Run: teardown")

    def test_one(self):

        # {'deviceName': '必须与谷歌浏览器的值一致'}
        mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)

        driver = webdriver.Chrome(chrome_options=options)

        driver.get('http://m.baidu.com')

        sleep(3)
        driver.close()


