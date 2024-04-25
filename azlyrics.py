import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def search(search_qeury):
    options = Options()
    # options.add_experimental_option('exclude-switches', ['enable-logging'])
    options.add_argument("stert-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    # driver.set_page_load_timeout(5)
    driver.get(f"https://www.genius.com/")
    time.sleep(5)
    quick_search = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search lyrics & more')]")
    # quick_search = driver.find_element(By.CLASS_NAME, "PageHeaderSearchdesktop__Input-eom9vk-2 gajVFV")
    quick_search.send_keys(search_qeury)
    quick_search.send_keys(Keys.ENTER)
    time.sleep(5)
    search_result = driver.find_element(By.CLASS_NAME, "column_layout-column_span column_layout-column_span--primary")
    print('searchResult: ', search_result.text)
    # time.sleep(25) 
    # print(driver)
    # time.sleep(5)
    # page_source = driver.page_source()
    # search_box = driver.find_element(By.CLASS_NAME, "form-control")
    # print(f'search_box: {search_box}')
    # search_box.send_keys(search_qeury)
    # search_box.send_keys(Keys.ENTER)
    # print(f'search: {search_qeury}')
    # panel = driver.find_element(By.CLASS_NAME, "panel")
    # print('panel: ', panel.text)

def main():
    # usr_input = input('Search for a song: ')
    search("Sorry")

if __name__ == "__main__":
    main()