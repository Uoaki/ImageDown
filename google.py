from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
search = input("Input the word you want to find: ")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
END_NUM = 151
SLEEP_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            print("End of Scroll")
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1

# input your directory path
savepath = "C:/Users/Southernwind/Desktop/images/" + search
    
if not os.path.exists(savepath):
    os.makedirs(savepath)


for image in images:
    try:
        image.click()
        time.sleep(SLEEP_TIME)
        # imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
        
        os.chdir(savepath)
        os.getcwd()

        savefile = "new" + "_" + search + "_" + str(count) + ".jpg"
        urllib.request.urlretrieve(imgUrl, savefile)
        count = count + 1

        if count == END_NUM:
            break
    except:
        pass

print("The search is completed")
driver.close()