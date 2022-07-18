import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import face_recognition as fc
from PIL import Image
import time
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

from downloader import Downloader
from TTLogger import TTLogger
from vid_to_frames import VidToFrames

DWNLD: Downloader
VTF: VidToFrames


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


def analyz(url):
    global DWNLD
    global VTF
    # анализирует видео по заданной ссылке и решает, удалить его или оставить
    # (если минимальный процент площади лица на протяжении всего видео больше 30
    # то его видео сохраняется в папке done, а если меньше, то удаляется)
    video_file = DWNLD.dwnld(url)
    if video_file == "":
        print("File cannot be loaded")
        return 1
    video_file = VTF.from_video_to_frames(video_file)

    path = video_file[:-4] + "\\"
    print(path)
    stat = []
    for frame_path in VTF.FRAMES_PATH:
        image = fc.load_image_file(frame_path)
        face_per = face_percent(image)
        stat.append(face_per)
        if face_per == 0:
            break

    arr = np.array(stat)
    argmin = arr.min()
    if arr.size != 0:
        print(f"The mean value is {arr.mean()}")
        print(f"The minimum value is {arr.min()}")

    if arr.min() > 17:

        try:
            os.rename(video_file, video_file.replace("data", "done"))
        except Exception:
            print("File was added earlier")
        else:
            print("Video is moved to Done")
    else:
        os.remove(video_file)
        print("Video is deleted")
    shutil.rmtree(path)

    return argmin


def main():
    global VTF
    global DWNLD
    mas = []
    delay = 10
    driver = webdriver.Chrome()
    driver.minimize_window()

    VTF = VidToFrames(1)
    DWNLD = Downloader(driver, delay)
    LogIn = TTLogger(driver, delay)

    t1 = time.time()
    is_file = input("From file or feed?\n")
    if is_file == "file":
        is_file = True
    else:
        is_file = False
    if is_file:
        file = input("URL file:")
        if file != "":
            start = int(input("Start from:"))
            f = open(file, "r")
            urls = f.readlines()
            f.close()
            urls = urls[slice(start, len(urls))]
            print(urls)

            count = start + 1
            driver.maximize_window()
            for url in urls:
                url = url[:-1]
                print(url)
                print(count)
                count += 1
                mas.append(analyz(url))
    else:
        driver.maximize_window()
        driver.get("https://www.tiktok.com/")
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ev30f212")))
            print("Page is ready!")
        except TimeoutException:
            raise Exception("NOT LOADED!")
        LogIn.login()
        time.sleep(5)

        for count in range(0, 10000):
            print(count)
            try:
                elem = driver.find_element(By.CLASS_NAME, "tiktok-lkdalv-VideoBasic")
                url = elem.get_attribute("src")
            except Exception:
                print("SRC WASNT LOADED!")
            else:
                mas.append(analyz(url))

            ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
            print("SCROLL!")
            time.sleep(0.5)
            loaded = False
            while not loaded:
                try:
                    WebDriverWait(driver, delay).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "tiktok-lkdalv-VideoBasic")))

                except TimeoutException:
                    print("wasnt loaded!")

                    print("SCROLL!")
                    time.sleep(0.5)
                else:
                    print("Page is ready!")
                    loaded = True

    big_data = np.array(mas)
    print(f"The mean value is {big_data.mean()}")
    print(f"The max value is {big_data.max()}")
    t2 = time.time() - t1
    print(f"Program running time is {t2} seconds")
    print("Program finished!")


if __name__ == '__main__':
    main()
