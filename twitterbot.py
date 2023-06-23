from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.liste = []

    def login(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(10)
        self.browser.find_element(By.CSS_SELECTOR,"input[name='text']").send_keys(username)
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
        time.sleep(5)
        
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(password)
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span").click()
        time.sleep(10)

    def process_direct_messages(self):
        self.browser.get("https://twitter.com/messages")
        time.sleep(15)

        try:
            element = self.browser.find_element(By.CSS_SELECTOR,".css-901oao.css-1hf3ou5.r-18jsvk2.r-37j5jr.r-a023e6.r-majxgm.r-rjixqe.r-bcqeeo.r-qvutc0")
            element.click()
        except:
            print("Yeni mesaj yok")
            return 0
        
        time.sleep(6)
        messages = self.browser.find_elements(By.CSS_SELECTOR, "span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")

        for x in messages:
            x = x.text.strip()
            if x == "":
                pass
            else:
                self.liste.append(x)

        print(self.liste)
        username = self.liste[6]
        message1 = self.liste[-4]
        message2 = self.liste[-3]
        message3 = self.liste[-2]
        print(f"@{username}:\n{message1}\n,{message2}\n,{message3}\n")
        self.liste.clear()
        return 1



username = input("username: ")
password = input("password: ")

tw = twitter(username, password)
tw.login()
result = 1
while result:
    result = tw.process_direct_messages()
    time.sleep(2)
