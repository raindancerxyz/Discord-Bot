import random
import requests
import pyperclip
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'Hey there! (Insert fun facts and jokes here omegalul)'

    if p_message == '!roll':
        return str(random.randint(0,100) + 1)

    if p_message == '!help':
        return '''
        Here is a list of some of my commands:
        !hello - Let me greet you and share a computer related fun fact or joke! 
        (Second feature is W.I.P...)
        !roll - Generate a random number between 1-100.'''
    
    if p_message == '!epccnews': #WIP
        # url of news website
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        url = "https://www.geeksforgeeks.org/how-to-build-web-scraping-bot-in-python/"
        driver.get(url)    
        return 'News scraper deployed.'
    
    return 'I didn\'t understand what you wrote, try typing "!help".'