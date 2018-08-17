
from selenium import webdriver
import time
import random
browser = webdriver.Firefox()
name_list = open("male.txt", "r")
name = name_list.read()
name = name.split()

browser.get('file:///home/arjun/Desktop/Workshop/index.html')
elem = browser.find_element_by_id('inputName')
elem2 = browser.find_element_by_id('inputEmail')
elem22 = browser.find_element_by_id('inputContact')

elem3=browser.find_element_by_id('btnClick')
for i in range(1,100):
	elem.send_keys(name[i])
	time.sleep(0.1)
	elem2.send_keys(name[i]+str(random.randint(1,101))+'gmail.com')
	time.sleep(0.1)
	elem22.send_keys(random.randint(9339827257,9976567459))	
	time.sleep(0.2)	
	elem3.click()

