from lib2to3.pgen2 import driver
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import logininfo


driver_path = ("\\Users\Candas\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\Scripts\chromedriver.exe") 
browser = webdriver.Chrome(executable_path=driver_path)

def logintwitter():
    return

browser.get("https://twitter.com/?lang=fr")
time.sleep(3)

refuse_cookie = browser.find_element( "xpath", "/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div")
refuse_cookie.click()
time.sleep(3)


se_connecter = browser.find_element("xpath" , "//div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div")
se_connecter.click()
time.sleep(3)


login = browser.find_element("xpath", "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
login.send_keys(logininfo.mail)
time.sleep(3)

suivant = browser.find_element("xpath" , "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
suivant.click()
time.sleep(3)

utilisateur = browser.find_element("xpath" , "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
utilisateur.send_keys(logininfo.username)
time.sleep(3)

suivant2 = browser.find_element("xpath" , "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
suivant2.click()
time.sleep(3)

motDePasseInput = browser.find_element("xpath" , "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
motDePasseInput.send_keys(logininfo.password)
time.sleep(3)

se_connecter2 = browser.find_element("xpath" , "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
se_connecter2.click()

time.sleep(3)

texttweet = browser.find_element("xpath" , "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
texttweet.send_keys(logininfo.tweetText)

time.sleep(3)
