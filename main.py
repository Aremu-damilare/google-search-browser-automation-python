from turtle import tilt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=chrome_options)
driver.implicitly_wait(0.5)

# while True:
def browse(word):    
    titles_list = []
    links_list = []
    
    if word:                    
        if 'search' in word:               
            #launch URL
            driver.get("https://www.google.com/")
            # word = "search java"         
            m = driver.find_element(by=By.NAME, value="q")
            #enter search text
            m.send_keys(Keys.CONTROL + "a")
            m.send_keys(Keys.DELETE )
            m.send_keys(str(word).replace('search', '', 1))
            time.sleep(0.5)
            #perform Google search with Keys.ENTER            
            m.send_keys(Keys.ENTER)
            time.sleep(2)
            titles = driver.find_elements(by=By.CSS_SELECTOR, value='div.NJo7tc.Z26q7c.jGGQ5e > div > a > h3')
            links = driver.find_elements(by=By.CSS_SELECTOR, value='div.NJo7tc.Z26q7c.jGGQ5e > div > a ')      
           

            # try:
            #     first_video = driver.find_element(by=By.CSS_SELECTOR, value='div.FGpTBd > h3 > a')
            #     first_item = driver.find_element(by=By.CSS_SELECTOR, value='div.yuRUbf > a')

            #     first_video_title = driver.find_element(by=By.CSS_SELECTOR, value='div.FGpTBd > h3 > a')
            #     first_item_title = driver.find_element(by=By.CSS_SELECTOR, value='div.yuRUbf > a')
                
            #     links_list.append((first_video.get_attribute("href")))
            #     links_list.append((first_item.get_attribute("href")))
            #     titles_list.append((first_video_title.get_attribute("innerHTML")))
            #     titles_list.append((first_item_title.get_attribute("innerHTML")))
            # except:
            #     pass

            # for link in links:
            #     l = link.get_attribute('href')
            #     links_list.append(l)                                

            for title in titles:    
                scor = title.find_element(by=By.TAG_NAME, value='h3')            
                print(scor.get_attribute("innerHTML"))                
                return titles_list

    if word == 'go down':
        k = driver.find_element(by=By.CSS_SELECTOR, value="body")
        print("********down")
        key = Keys.PAGE_DOWN
        k.send_keys(key)
    elif word == 'go up':
        k = driver.find_element(by=By.CSS_SELECTOR, value="body")
        print("********up")
        key = Keys.PAGE_UP
        k.send_keys(key)        
     