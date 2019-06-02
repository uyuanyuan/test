#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Chris
# @File    : helloselenium.py
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(1)
driver.get("https://www.baidu.com/")
sleep(1)
# driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_name("wd").send_keys("webdriver")
sleep(1)
driver.quit()