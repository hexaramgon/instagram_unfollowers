
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys 

#jsx-2055372491 toggle-icon toggle-icon-v4


x = 'password'

class Instabot:

    def __init__(self, username, password):
        self.setup(username, password)
        self.action()


    def setup(self, user, psw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com")
        sleep(2)
        loginfield = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passfield = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        loginfield.send_keys(user)
        passfield.send_keys(psw)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(30)
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div').click()


    def action(self):
        instafollowers = self.grab_followers()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        unfollowers = self.find_unfollowers(instafollowers)
        print('Your Unfollwers are:')
        for x in unfollowers:
            print(x)

    
    def grab_followers(self):
        sleep(2)
        fol = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text 
        num_fol = int(fol)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(0.5)
        sugs = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]')
        self.driver.execute_script('arguments[0].scrollIntoView()' , sugs)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]') 
        last_ht, ht = 0, 1
        while last_ht != ht: 
            last_ht = ht
            sleep(0.5)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        followers = [name.text for name in links if name.text != '']
        actual_followers = followers[:num_fol]
        return actual_followers


    def find_unfollowers(self, followers):
        fol = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text 
        num_fol = int(fol)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(0.5)
        sugs = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]')
        self.driver.execute_script('arguments[0].scrollIntoView()' , sugs)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]') 
        last_ht, ht = 0, 1
        while last_ht != ht: 
            last_ht = ht
            sleep(0.5)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        following = [name.text for name in links if name.text != '']
        actual_follow = following[:num_fol]
        unfollowers = [x for x in actual_follow if x not in followers]
        return unfollowers


Instabot('username', x)


