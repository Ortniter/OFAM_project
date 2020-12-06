from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

with Display():
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.ofam.org.ua/ua/shop")
        sleep(10)
        driver.find_element_by_css_selector('.js-store-load-more-btn > table:nth-child(1)').click()
        sleep(10)

        item_divs = driver.find_elements_by_class_name('js-product')
        for item_div in item_divs:
            item_div.click()
            sleep(5)
            url = driver.current_url

            html = requests.get(url).text

            soup = BeautifulSoup(html, 'lxml')

            name = soup.find('div', class_='js-store-prod-name').text.strip()
            description = soup.find('div', class_='js-store-prod-text').text.strip()
            price = soup.find('div', class_='js-product-price').text.strip()
            image_url = driver.find_element_by_class_name('t-slds__imgwrapper').get_attribute('data-img-zoom-url')

            print(name)
            print(description)
            print(price)
            print(image_url)
            print(url)

            sleep(2)
            close_button = driver.find_element_by_class_name('js-store-close-text')
            close_button.click()
            sleep(2)

    finally:
        driver.close()
        driver.quit()