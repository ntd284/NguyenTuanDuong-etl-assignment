from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
from selenium.webdriver.chrome.service import Service
from plugin.function.operation import opera
from plugin.function.filepath import conf

class extract():
    def main():
        with open(f'{conf.filepath()}/login_credential.txt',"r",encoding="utf-8") as outfile:
            lst_accs = outfile.read().split()
            num_of_page = 2
            title = "Software Engineer"
            print(f'save_profile_tag - number of page: {num_of_page}')
            for lst_ac in lst_accs:
                chrome_version = '114.0.5735.90'
                username = lst_ac.split(':')[0]
                password = lst_ac.split(':')[1]
                options = webdriver.ChromeOptions()
                options.add_argument("--incognito")
                options.add_argument("--headless")
                driver = webdriver.Chrome(options=options)
    
                wait = WebDriverWait(driver, 5)
                url = 'https://www.linkedin.com'
                driver.get(url)
                opera.login(driver,username,password)
                opera.search(wait,title,driver)
                opera.get_all_url_on_pages(conf.filepath(),driver,wait,num_of_page)
                opera.scan(conf.filepath(),driver,wait)

