from selenium import webdriver
import os 
import time 
import config

class InstagramBot:
    def __init__(self  ):
        self.username = config.username
        self.password = config.password
        self.driver = webdriver.Chrome('./chromedriver')
        self.base_url = 'https://www.instagram.com'
        
       
       
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        username.send_keys(self.username)
        password.send_keys(self.password)
        login = self.driver.find_elements_by_xpath("//div[contains(text() , 'Log In')]")[0]
        login.click()
        time.sleep(3)
        
    def nav_user(self , user): 
        self.driver.get('{}/{}/'.format(self.base_url , user))
        
        
    def follow_user(self  , user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/button')[0]
        follow_button.click()
        
        
        
        
        
            

if __name__ == '__main__':
    ig_bot = InstagramBot()
    ig_bot.login()
    ig_bot.follow_user('amirhasansadatmand79')
    
    
    
