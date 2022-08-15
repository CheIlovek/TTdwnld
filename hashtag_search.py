from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os




def search_tags(tag, driver, delay):
    driver.get("https://www.tiktok.com/tag/" + tag)
    try:
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "tiktok-yz6ijl-DivWrapper")))
        print("Page is ready!")
    except TimeoutException:
        return 0, 0

    old_height = driver.execute_script("return document.body.scrollHeight")
    html = driver.find_element(By.TAG_NAME, 'html')
    while True:
        html.send_keys(Keys.END)
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == old_height:
            break
        old_height = new_height

    divs = driver.find_elements(By.CLASS_NAME, "tiktok-yz6ijl-DivWrapper")
    prew = []
    video = []
    for div in divs:
        prew.append(div.find_element(By.TAG_NAME, "img").get_attribute("src"))
        video.append(div.find_element(By.TAG_NAME, "a").get_attribute("href"))
    return prew, video





def hashtag_req(delay):
    while True:
        file = input("URL file:")
        if os.path.isfile(file):
            break
        else:
            print("File is not exist.")

    with open(file, "r", encoding="utf-8") as f:
        tags = f.readlines()

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    count = 0
    with open("buff.txt", "a", encoding="utf-8") as f:
        for tag in tags:
            tag = tag[1:-1]
            print(tag)
            p, v = search_tags(tag, driver, delay)
            if p == 0:
                continue
            for i in range(len(p)):
                count += 1
                f.write(p[i] + '\n')
                f.write(v[i] + '\n')

    print("LEN: ", count)
    driver.close()
    input("VPN is bad man, turn this shit off")
    return count





def main():
    delay = 60
    hashtag_req(delay)



if __name__ == '__main__':
    main()
