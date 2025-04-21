import pyautogui
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

########Add Chrome absolute path here #############👇
service = Service(r"C:\Users\dell\Desktop\temp\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://monkeytype.com")



################################################
###### This Pause is To setup you account ######
################################################

a = input("Press Enter to continue")
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
words = [] # this will contains words
about_to_type_words = soup.find_all("div",class_="word")

for i in about_to_type_words:
    word = ''.join([l.get_text() for l in i.find_all('letter')])
    words.append(word)

print(words)

idx = []

for i in range(int(len(words)*0.1)):
    idx.append(random.randrange(65,65+25))


for i in idx:
    word = words.pop(int(i/10))
    word = word[:-1] + chr(i)
    print("new word is ",word)
    words.insert(int(i/10),word)  ## adding error to words for more human like behaiviour
    
print(words)
time.sleep(5)
for i in words:
    pyautogui.write(i)
    if(random.randrange(0,15) == 8): # adding a random pause to micik more like human
        print("inside random")
        time.sleep(random.randrange(0,15)/10)
    pyautogui.press("space")

#################################################################
####### 5 sec window to set the  mouse focus to MonkeyType ######
#################################################################

time.sleep(5)
a = input("press Enter to quit chrome!")
