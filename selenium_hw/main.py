from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os
from dotenv import load_dotenv
def autorization_in_yandex():
    chrome_service = Service('C:\\Роман\\Projects\\HW_tests\\selenium\\chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    url = 'https://passport.yandex.ru/auth/'
    try:
        load_dotenv()
        driver.get(url=url)
        time.sleep(3)
        email_input = driver.find_element('id',"passp-field-login")
        email_input.clear()
        email_input.send_keys(os.getenv("Y_login"))
        time.sleep(2)
        input_button = driver.find_element('id', 'passp:sign-in').click()
        time.sleep(2)
        password_input = driver.find_element('id',"passp-field-passwd")
        password_input.clear()
        time.sleep(2)
        
        password_input.send_keys(os.getenv('Y_password'))
        input_button = driver.find_element('id', 'passp:sign-in').click()
        time.sleep(3)
        general_page = input_button = driver.title
        return general_page

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
 


