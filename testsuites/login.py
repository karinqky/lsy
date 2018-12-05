#-*- coding=utf-8 -*-

import time
from selenium import webdriver

class Login(object):
    def test_login(self):
        page = webdriver.Chrome()
        page.maximize_window()
        start_url = 'http://'