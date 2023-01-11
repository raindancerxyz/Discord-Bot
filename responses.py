import random
import requests
import pyperclip
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'Hey there! (Insert fun facts and jokes here omegalul)'

    if p_message == '!roll':
        return str(random.randint(0,100) + 1)

    if p_message == '!help': #Returns command list of bot features
        return '''
        Here is a list of some of my commands:
        !hello - Let me greet you and share a computer related fun fact or joke! 
        (Second feature is W.I.P...)
        !roll - Generate a random number between 1-100.'''

    if p_message == '!annoy': #Bot currently can't @ and ping users
        return '''
                @rain (they/them)#7217 !!!!
                @rain (they/them)#7217 !!!!!
                @rain (they/them)#7217 !!!!!!!'''
    
    if p_message == '!epweather': #Reworking to weather tweets. Must change from command based to being ran on launch
        # url of news website
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        url = "https://twitter.com/NWSElPaso?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
        driver.get(url) 
        driver.find_element(by=By.XPATH, value='//html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]').click()
        return 'News scraper deployed.'
    
    return 'I didn\'t understand what you wrote, try typing "!help".'