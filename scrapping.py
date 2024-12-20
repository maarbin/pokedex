import sys
sys.path.append("C:\\Users\\mbin1\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages")
import time
import pandas as pd
import numpy as np
import random as random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib
import requests


url = 'https://pokemondb.net/pokedex/national'

driver = webdriver.Chrome()
driver.get(url)


# All images from Serebii
for i in range(898):
    # Add this just in case the page kicks out out for downloading too fast!
    time.sleep(random.randint(1,3))
    
    # First, locate the image on the page using find_element
    image_element = driver.find_element_by_xpath('//*[@class="fooinfo"]/img')

    # Get the link to the image
    image_link = image_element.get_attribute("src")

    # Download the image and save it with an appropriate name
    urllib.request.urlretrieve(image_link, f"{i+1}.png")

    # Move to the next page
    driver.find_element_by_xpath('//td[@width="right"]/../td[1]/a').click()