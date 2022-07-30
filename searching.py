from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
import time
import os
import face_recognition as fc
from PIL import Image

def send_search(driver, request,delay):
    srch = driver.find_element(By.CLASS_NAME, "ev30f212")
    srch.clear()
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

def parsing(driver, PERSENT):
    urls = []
    divs = driver.find_elements(By.CLASS_NAME, "tiktok-yz6ijl-DivWrapper")
    for div in divs:
        img = div.find_element(By.TAG_NAME, "img").get_attribute("src")
        r = requests.get(img, allow_redirects=True)
        with open("the_image.jpg", "wb") as f:
            f.write(r.content)
        # Проверка превью
        img = fc.load_image_file("the_image.jpg")
        face_per = face_percent(img)
        if(face_per >= PERSENT):
            urls.append(div.find_element(By.TAG_NAME, "a").get_attribute("href"))
        else:
            print(div.find_element(By.TAG_NAME, "a").get_attribute("href"), end=" ")
            print("IS NOT SAVED!")
    return urls


def face_percent(fc_img):
    # возвращает процент площади, которую занимает лицо на заданном изображении
    fc_loc = fc.face_locations(fc_img)
    pil_img = Image.fromarray(fc_img)
    width, height = pil_img.size
    if len(fc_loc) != 1:
        percent = 0
    else:
        percent = (((fc_loc[0][2] - fc_loc[0][0]) * (fc_loc[0][1] - fc_loc[0][3])) / (width * height)) * 100
    return percent


def main():
    PERSENT = 17

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    delay = 10
    while True:
        file = input("URL file:")
        if os.path.isfile(file):
            break
        else:
            print("File is not exist.")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.tiktok.com/")
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ev30f212")))
        print("Page is ready!")
    except TimeoutException:
        raise Exception("NOT LOADED!")
    res = []
    with open(file, "r", encoding='utf-8') as f_r:
        for item in f_r:
            send_search(driver, item, delay)
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
            res = parsing(driver, PERSENT)

    print("LEN: ", len(res))
    with open("urls.txt", "w+") as f:
        for elem in res:
            f.write(elem + '\n')


if __name__ == '__main__':
    main()
