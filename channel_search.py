from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def parsing(driver):
    urls = []
    divs = driver.find_elements(By.CLASS_NAME, "tiktok-yz6ijl-DivWrapper")
    for div in divs:
        urls.append(div.find_element(By.TAG_NAME, "a").get_attribute("href"))
    return urls


def main():
    t1 = time.time()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    delay = 20

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.tiktok.com/@girlwalkingonfire")
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "e1yey0rl1")))
        print("Page is ready!")
    except TimeoutException:
        raise Exception("NOT LOADED!")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "e1ugmybf1")))
            print("Page is ready!")
        except TimeoutException:
            print("NOT LOADED!")
            break
        time.sleep(5)

    res = parsing(driver)
    print("LEN: ", len(res))
    f = open("urls.txt", "w+")
    for elem in res:
        f.write(elem + '\n')
    f.close()
    t2 = time.time() - t1
    print(f"Running time is {t2}")

if __name__ == '__main__':
    main()