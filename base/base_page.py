#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：WebUITest 
@File    ：base_page.py
@IDE     ：PyCharm 
@Author  ：萌新小缘
@Date    ：2022/8/9 14:39 
"""
from time import sleep

from selenium import webdriver


class BasePage:
    # 虚构driver对象
    # driver = webdriver.Chrome()

    # 构造函数,定义一个构造函数，self.driver做一个赋值
    def __init__(self, driver):
        self.driver = driver

    # 访问呢url,封装成函数
    def visit(self):
        self.driver.get(self.url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc,txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 等待
    def wait(self, time_):
        sleep(time_)
