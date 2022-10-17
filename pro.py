from selenium.webdriver import Ie
import time
# -*- coding:utf-8 -*-
#海康威视网页自动化配置工具-designed by Eric/2022-10-16
import os
import time
from selenium import webdriver # 从selenium导入webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time
title = "海康威视摄像机网页批量配置工具v1.0\n"
print(title)
ie = Ie(executable_path='IEDriverServer.exe')
#读取文件行数
count = len(open(r"list.txt",'r').readlines())  
print("总共IP地址数量为：",end = "")
print(count)
#打开IP地址文件遍历,循环
time.sleep(2)
f = open("list.txt")
with open("list.txt") as file:
    for item in file:
        #关闭图片显示，提高运行速度
        ie.get(item)
        ie.implicitly_wait(10)
        #没有找到登录页的元素时
        len1 = ie.find_elements(By.ID,"username")
        if len(len1) == 0:
            print(item)
            continue
        else:
            ie.find_element(By.ID,"username").clear()
            ie.find_element(By.ID,"username").send_keys("admin")
            ie.find_element(By.ID,"password").clear()
            ie.find_element(By.ID,"password").send_keys("Admin256")
            ie.find_element(By.CLASS_NAME,"login-btn").click()
            time.sleep(1)
            ie.find_element(By.NAME,"event").click()
            time.sleep(2)
            ie.implicitly_wait(20)
            if not ie.find_element(By.ID,"enableMotion").is_selected():
                time.sleep(0.5)
                print("移动侦测已经关闭")
            if ie.find_element(By.ID,"enableMotion").is_selected():
                print("移动侦测已经关闭")
                ie.find_element(By.ID,"enableMotion").click()
                ie.find_element(By.CLASS_NAME,"btn-save").click()
ie.quit()
print("配置完成")




