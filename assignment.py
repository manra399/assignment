#!/usr/bin/env python
# coding: utf-8

# In[55]:


import requests
import time
import json
from lxml import etree
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


url='https://www.target.com/p/apple-iphone-13-pro-max/-/A-84616123?preselect=84240109#lnk=sametab'
driver = webdriver.Chrome()
driver.get(url)
dict_={}

driver.get(url)
time.sleep(3)
try:
    dict_['price']=driver.find_element_by_xpath("//span[@data-test='da-price--monthly-price']").text.split('/')[0]
except:
    dict_['price']=''
try:
    dict_['title']=driver.find_element_by_xpath("//h1[@data-test='product-title']").text
except:
    dict_['title']=''
driver.find_element_by_xpath("//button[@data-test='toggleContentButton']").click()
try:
    dict_['description']=driver.find_element_by_xpath("//div[@data-test='item-details-description']").text
except:
    dict_['description']=''
try:
    dict_['specifications']=[i.text for i in driver.find_elements_by_xpath("//h3[contains(text(),'Specifications')]/parent::div//div//div")]
except:
    dict_['specifications']=''
try:
    dict_['highlights']=[i.text for i in driver.find_elements_by_xpath("//h3[contains(text(),'Highlights')]/parent::div//ul//div")]
except:
    dict_['highlights']=''
try:
    time.sleep(3)
    try:
        driver.execute_script("window.scrollTo(0,-500)")
        driver.find_element_by_xpath("//button[@class='styles__LegendGridButtonOverlay-sc-beej2j-13 ktNbWU h-display-flex h-flex-align-center h-flex-justify-center h-flex-direction-col h-position-absolute  h-text-bold h-text-md h-text-white']").click()
    except:
        driver.find_element_by_xpath("//button[@class='styles__LegendGridButtonOverlay-sc-beej2j-13 ktNbWU h-display-flex h-flex-align-center h-flex-justify-center h-flex-direction-col h-position-absolute  h-text-bold h-text-md h-text-white']").click()
    time.sleep(1)
    dict_['images urls']=[i.get_attribute('src') for i in driver.find_elements_by_xpath("//div[@class='ZoomedImageCarousel__ZoomedSlideDeckWrapper-sc-1x7o3k-1 FQnqC']//button//img")]
except:
    dict_['images urls']=''
driver.get(url)
try:
    driver.find_element_by_xpath("//div[contains(text(),'Q&A ')]/parent::a").click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,800)")
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(text(),'See all questions (')]").click()
    all_qus=[]
    while True:
        for i in driver.find_elements_by_xpath("//span[@data-test='questionSummary']"):
            all_qus.append(i.text)
        try:
            driver.find_element_by_xpath("//button[contains(text(),'show more')]").click()
        except:
            break
    time.sleep(3)
    dict_['questions']=all_qus
except:
    dict_['questions']=''
print(dict_)


# In[ ]:




