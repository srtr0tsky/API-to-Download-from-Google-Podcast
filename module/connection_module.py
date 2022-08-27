# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 23:51:48 2022

@author: bispo
"""
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import requests
import time

class WebConnect:
    def __init__(self):
        pass
    
    def connection(self, link):
        service = Service(executable_path=(GeckoDriverManager().install()))
        option = Options()
        option.headless = True
        browser = webdriver.Firefox(service=service, options=option)
        print("configuration status: ok!")
        browser.get(link)
        print("connection: ok!")
        return browser
    
    def download(self, url, name):
        try:
            connectionSite = requests.get(url)
        
            spec_Characters = [' \ ', '/', ':', '*', '?', '"', '<', '>', '|']
            for character in spec_Characters:
                if character in name:
                    name = name.replace(character, ' ')
            
            with open(f"{name}.mp3", "wb") as audio:
                for byte in connectionSite.iter_content(1024):
                    audio.write(byte)
                
        except Exception as error:
            print(error)
            audio.close()
        finally: audio.close()
        return "All ok!"
    
    def getFeedURL(self, browser_driver):
         classJ0Qtec = browser_driver.find_element(By.CLASS_NAME, 'J0Qtec')
         classJ0Qtec.click()
         print("Playing Podcast")
         PODCAST_NAME = browser_driver.title
         print(PODCAST_NAME)
         time.sleep(10)
         classHQGk8 = browser_driver.find_element(By.CLASS_NAME, 'HQGk8')
         print("In class HQGk8...")
         # Catch FEED URL 
         classSYMOW = classHQGk8.find_element(By.CLASS_NAME, 'symow')
         FEED_URL = classSYMOW.text
         return [FEED_URL, PODCAST_NAME]
     
    def remove_spec_character(text): pass    

if __name__ == "__main__":
    WebConnect()