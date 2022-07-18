
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def send_search(driver, request,delay):
    srch = driver.find_element(By.CLASS_NAME, "ev30f212")
    srch.send_keys(request)
    srch.send_keys(Keys.RETURN)
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, "tabs-0-tab-search_video")))
        print("Page is ready!")
    except TimeoutException:
        raise Exception("NOT LOADED!")
    driver.find_element(By.ID, "tabs-0-tab-search_video").click()
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tiktok-yz6ijl-DivWrapper")))
        print("Page is ready!")
    except TimeoutException:
        raise Exception("NOT LOADED!")


def scrolling(driver, delay):
    html = driver.find_element(By.TAG_NAME, 'html')
    # html.send_keys(Keys.END)
    try:
        WebDriverWait(driver, delay*3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "e17vxm6m1")))
        print("Page is ready!")
    except TimeoutException:
        raise Exception("NOT LOADED!")
    clicked = False
    while not clicked:
        try:
            driver.find_element(By.CLASS_NAME, "e17vxm6m1").click()

        except Exception:
            print("Can't click!")
        else:
            clicked = True

def parsing(driver):
    urls = []
    divs = driver.find_elements(By.CLASS_NAME, "tiktok-yz6ijl-DivWrapper")
    for div in divs:
        urls.append(div.find_element(By.TAG_NAME, "a").get_attribute("href"))
    return urls


def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Обычно по 12 за скролл
    s_request = input("What we will search?")
    delay = 30

    t1 = time.time()
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.tiktok.com/")
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ev30f212")))
        print("Page is ready!")
    except TimeoutException:
        raise Exception("NOT LOADED!")

    send_search(driver, s_request, delay)
    time.sleep(4)
    old_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        try:
            scrolling(driver, delay)
        except Exception as e:
            print(e.args)
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == old_height:
            break
        old_height = new_height

    res = parsing(driver)
    print("LEN: ", len(res))
    f = open("urls.txt", "w+")
    for elem in res:
        f.write(elem + '\n')


if __name__ == '__main__':
    main()