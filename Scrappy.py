import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
from lxml import etree
import csv, os, json
import requests
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\yakov\\Desktop\\chromedriver.exe')
#driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
driver.get("https://linkedin.com/")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-email")))
    un = driver.find_element_by_id("login-email")
    pw = driver.find_element_by_id("login-password")
    un.click()
    un.clear()
    un.send_keys("fake123@gmail.com")
    time.sleep(2)
    pw.send_keys("fake123")
    time.sleep(2)
    driver.find_element_by_id("login-submit").click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-nav-item")))
    time.sleep(2)
    pf = driver.find_element_by_id("profile-nav-item")
    pf.click()
    time.sleep(2)
    driver.find_element_by_xpath('//a[@href="/m/logout/"]').click()
    #driver.find_element_by_xpath("//a[@href='/m/logout/']").click()
    #driver.find_element_by_id("ember2417").click()
finally:
    time.sleep(5)
    driver.close()
# url = "https://medium.com/"  #
# url = "https://linkedin.com/"
# params = {'username': 'michael.breban666@gmail.com', 'password': 'MB@linkedin2018'}
# r = requests.post("https://linkedin.com/", params)
# print("cookie is set to: ")
# print(r.cookies.get_dict())
# print("---------------")
# time.sleep(2)
# print("going to profile page")
# r = requests.get("https://linkedin.com/",cookies=r.cookies)
# print("_--------------")
# print(r.content)
# print("-----------------")
# doc = html.fromstring(r.content)
# print(etree.tostring(doc,pretty_print=True))
#print(doc.xpath("//a[@class='ds-link ds-link--stylePointer']//text()"))
