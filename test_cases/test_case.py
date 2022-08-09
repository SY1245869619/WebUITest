#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：WebUITest 
@File    ：test_case.py
@IDE     ：PyCharm 
@Author  ：萌新小缘
@Date    ：2022/8/9 16:36 
"""

import unittest

# 测试用例的设计
from time import sleep

from selenium import webdriver

from page_object.index_page import IndexPage
from page_object.login_page import LoginPage


class TestCase(unittest.TestCase):
    def test_1_login(self):
        driver = webdriver.Chrome()
        username = 'heshunData'
        password = 'zhaoxiaojun'
        company_name_input_ = '介休晋能卡车司机运输有限公司和顺分公司'
        lp = LoginPage(driver)
        lp.login(username, password)
        sleep(2)
        ip = IndexPage(driver)
        ip.search(company_name_input_)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
