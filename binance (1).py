# -*- coding: utf-8 -*-
__author__ = 'JLPlata'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path='path of webdrver')
driver.get("https://www.binance.com/en/trade/BTC_USDT?layout=basic")

h1 = driver.find_element_by_class_name('orderbook-list')

print(h1.text)
driver.quit()