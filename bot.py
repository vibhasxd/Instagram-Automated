from selenium import webdriver
import os
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from secrets import username,password

driver = webdriver.Chrome(ChromeDriverManager().install())



class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
        self.functions()
  
    def login(self):
        self.bot.get(self.base_url)
  
        enter_username = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(6)
  
        try:
            driver.find_element_by_xpath("//button[text()='Not now']").click()
        except Exception:
                pass
        time.sleep(4)
  
        try:
            driver.find_element_by_xpath("//button[text()='Not Now']").click()
        except Exception:
            pass
        time.sleep(4)

    def functions(self):
        profiles_list=['google','twitter']
        comments=['Nice!', 'Well Done!', 'Great!','Interesting!']

        for i in range (len(profiles_list)): 
            #Search hover and click
            driver.find_element_by_xpath('//span[text()="Search"]').click()
            time.sleep(1)
            #Search enter
            search = driver.find_element_by_xpath('//input[@placeholder="Search"]')
            search.send_keys(profiles_list[i])

            count = 0
            while count <3:
                search.send_keys(Keys.ENTER)
                count +=1 # count = count +1
                time.sleep(1)

            # follow
            follow_button = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Follow']")))
            follow_button.click()
            time.sleep(2)

            # first media element
            media_element = driver.find_element_by_xpath('//div[@class="eLAPa"]')
            media_element.click()
            time.sleep(2)

            for k in range(2):
                # like
                driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
                time.sleep(1)
                # comment
                driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
                time.sleep(1)

                comment = driver.find_element_by_class_name('Ypffh')
                comment.send_keys(random.choice(comments))
                time.sleep(1)

                # post
                post = driver.find_element_by_xpath('//button[text()="Post"]')
                post.click()
                time.sleep(1)

                # click on next media element
                next_button = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/button')
                next_button.click()
                time.sleep(1)

            close = driver.find_element_by_xpath('//*[@aria-label="Close"]')
            close.click()
  
def init():
    bot(username, password)
  
    input("DONE")
  
init()