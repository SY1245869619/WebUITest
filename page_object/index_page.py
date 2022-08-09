#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：WebUITest 
@File    ：index_page.py
@IDE     ：PyCharm 
@Author  ：萌新小缘
@Date    ：2022/8/9 16:43 
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class IndexPage(BasePage):
    # 核心元素
    url = 'http://test.regulatory.kachexiongdi.com/'
    menu_button = (By.XPATH, '//*[@id="root"]/section/aside/div/ul/li[1]/div')
    menu_item_button = (By.XPATH, '//*[@id="sub1$Menu"]/li[1]')
    company_name_input_ = (By.XPATH, '//*[@id="root"]/section/section/main/div[2]/div/div[1]/div[1]/div[2]/span/input')
    search_button = (By.XPATH, '//*[@id="root"]/section/section/main/div[2]/div/div[1]/div[2]/div[2]/div/button[1]')

    # 核心业务流
    def search(self, company_name_input_):
        self.visit()
        self.click(self.menu_button)
        sleep(2)
        self.click(self.menu_item_button)
        sleep(2)
        self.input_(self.company_name_input_, company_name_input_)
        sleep(2)
        self.click(self.search_button)

# 调试代码

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     username = 'heshunData'
#     password = 'zhaoxiaojun'
#     lp = LoginPage(driver)
#     lp.login(username, password)
