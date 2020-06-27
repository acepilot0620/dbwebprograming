from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
import urllib.request
import requests
import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODUULE", "rip_floyd.settings")
import django
django.setup()


class Result_node():

    def __init__(self,title, img_url, time_stamp=datetime.datetime.now()):
        self.title = title
        self.img_url = img_url
        self.time_stamp = time_stamp

def croller():

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome('C:/Users/user/Desktop/dbproject/chromedriver.exe', chrome_options = chrome_options) # 로컬에서 돌릴때

    driver.get("https://news.google.com/search?q=george%20floyd%20when%3A1h&hl=en-US&gl=US&ceid=US%3Aen")
    
    i = 1
    result_node_list = []
    while True:
        try:
            title = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div['+str(i)+']/div/article/h3/a')
                                                  
            title_text = title.text
            img = driver.find_element_by_xpath('//*[@id="i'+str(i*2+2)+'"]')
            img_url = img.get_attribute('src')
            news_obj = Result_node(title_text,img_url)
            result_node_list.append(news_obj)
            i = i+1
            pass
        except NoSuchElementException:
            break
        
    return result_node_list


