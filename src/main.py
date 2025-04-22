import pyautogui
import time
import random
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

first_time = False
error = 0.1

def to_write(driver):
    global first_time
    global error
    paragraph = ""
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    words = [] # this will contains words
    if not first_time:
        first_word = input("Enter the first Word(You need to give this input only one time)")
        first_time = True
    else: 
        first_word = ''
    candidate_divs = soup.select("div.word")
    # Step 2: Filter only those with EXACT class ["word"]
    about_to_type_words = [div for div in candidate_divs if div.get("class") == ["word"]]
    
    for i in about_to_type_words:
        word = ''.join([l.get_text() for l in i.find_all('letter')])
        words.append(word)
    idx = []
    for i in range(int(len(words)*error)):
        idx.append(random.randrange(65,65+25))
    for i in idx:
        word = words.pop(int(i/10))
        word = word[:-1] + chr(i)
        words.insert(int(i/10),word)  ## adding error to words for more human like behaiviour
        
    paragraph = first_word + " " + " ".join(words)
    return paragraph



if __name__ == "__main__":
    ######## Add Chrome absolute path here #############👇
    service = Service(r"C:\Users\dell\Desktop\temp\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://monkeytype.com")

    ################################################
    ###### This Pause is To setup you account ######
    ################################################

    a = input("Press Enter to continue")

    paragraph = to_write(driver)
    dur = int(input("Enter the duration of Typing :"))
    
    #################################################################
    ####### 5 sec window to set the  mouse focus to MonkeyType ######
    #################################################################

    time.sleep(5)
    start_time = time.time()
    while(time.time() -  start_time < dur):
        pyautogui.write(paragraph)
        # time.sleep(2) # to achive desirable speed adjust the sleep time for 2 its give 750+ wpm
        paragraph = to_write(driver)  

    a = input("press Enter to quit chrome!")



