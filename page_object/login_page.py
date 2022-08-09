#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：WebUITest 
@File    ：login_page.py
@IDE     ：PyCharm 
@Author  ：萌新小缘
@Date    ：2022/8/9 14:57 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    # 核心元素
    url = 'http://test.regulatory.kachexiongdi.com/login'
    user = (By.ID, 'username')
    password = (By.ID, 'password')
    login_button = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/form/button')

    # 核心业务流
    def login(self, username, password):
        self.visit()
        self.input_(self.user, username)
        self.input_(self.password, password)
        self.click(self.login_button)


# 调试代码

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     username = 'heshunData'
#     password = 'zhaoxiaojun'
#     lp = LoginPage(driver)
#     lp.login(username, password)
