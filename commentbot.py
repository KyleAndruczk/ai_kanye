from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import math

from secrets import user, pw

class InstaBot:
    
    def __init__(self, usrname, pw):
        
        self.driver = webdriver.Chrome()
        self.username = usrname
        self.driver.get("https://instagram.com")
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(usrname)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()   
        
        

    def leave_comment(self, profile):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
            .send_keys(profile)
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]")\
            .click()
        time.sleep(4)

        pics = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main")
        links = pics.find_elements_by_tag_name('a')


        
        pic_href = links[3].get_attribute('href')
        self.driver.get(pic_href)
        time.sleep(4)


    
    def send_dm(self, user, message):
        self.driver.get("https://instagram.com/direct/inbox")
        time.sleep(random.randrange(2, 8))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button")\
            .click()
        time.sleep(random.randrange(2, 8))
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input")\
            .send_keys(user)
        time.sleep(random.randrange(2, 8))
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[1]")\
            .click()
        time.sleep(random.randrange(2, 8))
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div/button")\
            .click()
        time.sleep(random.randrange(2, 8))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")\
            .send_keys("This a message generated by KanyeBot in testing: " + message)
        time.sleep(random.randrange(2, 8))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")\
            .click()
        time.sleep(random.randrange(2, 8))
    



class TwitterBot:
    
    def __init__(self, usrname, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com/login")
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")\
            .send_keys(usrname)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div')\
            .click()
        time.sleep(4)
    
    def reply(self, profile, message):
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]")\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")\
            .send_keys("@" + profile)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")\
            .send_keys(Keys.ENTER)
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div[2]/div[3]/a")\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span")\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/span")\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_class_name("notranslate").click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_class_name("notranslate").send_keys(message)
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("//div[@data-testid='tweetButton']")\
            .click()
        time.sleep(random.randrange(2, 5))



class YoutubeBot:
    def __init__(self, email, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://youtube.com")
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button")\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")\
            .send_keys(email)
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div")\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")\
            .send_keys(pw)
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div")\
            .click()
        time.sleep(random.randrange(2, 5))
    
    def leave_comment(self, account, message):
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")\
            .send_keys(account)
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button")\
            .click()
        time.sleep(random.randrange(2, 5))
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/div/div[1]/a")\
            .click()
        time.sleep(random.randrange(3, 5))
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/app-toolbar/div/div/paper-tabs/div/div/paper-tab[2]/div")\
            .click()
        time.sleep(random.randrange(3, 5))
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/h3/a")\
            .click()
        time.sleep(random.randrange(3, 5))
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(random.randrange(3, 5))
        text_box = self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[1]")
        text_box.click()
        text_box = self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[2]/paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div")
        text_box.click()
        time.sleep(random.randrange(3, 5))
        text_box.send_keys(message)
        time.sleep(random.randrange(3, 5))
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[4]/div[5]/ytd-button-renderer[2]/a/paper-button")\
            .click()
        time.sleep(25)
        


# ig_bot = InstaBot(user, pw)
# ig_bot.leave_comment('yale')
tw_bot = TwitterBot(user, pw)
tw_bot.reply("theh3podcast", "I am testing")
#yt_bot = YoutubeBot(user, pw)
#yt_bot.leave_comment("ye", "test")
 