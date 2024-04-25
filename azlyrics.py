import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def search(search_qeury):
    print(f'search: {search_qeury}')

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.azlyrics.com")
    print(driver)
    time.sleep(5)
    # page_source = driver.page_source()
    search_box = driver.find_element(By.CLASS_NAME, "form-control")
    print(f'search_box: {search_box}')
    # print('page source: ', page_source)


if __name__ == "__main__":
    main()