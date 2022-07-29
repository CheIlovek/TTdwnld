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
from selenium.webdriver.common.action_chains import ActionChains
from rich.prompt import Prompt
from rich.live import Live
from rich.console import Console
from rich.table import Table
from rich import box
from statistics import mean

from downloader import Downloader
from TTLogger import TTLogger
from vid_to_frames import VidToFrames

CHANNELS_DB = {}
DWNLD: Downloader
VTF: VidToFrames

CONSOLE: Console
FACE_PERCENT = 17
DELAY = 30
VIDEO_PER_CHANNEL = 3


def db_init():
    global CHANNELS_DB
    dict = os.path.dirname(__file__) + "\\done\\"
    for file in os.listdir(dict):
        file = file[:-4]
        separator = file.rfind("_")
        if separator != -1:
            channel = file[:separator]
            if channel in CHANNELS_DB:
                CHANNELS_DB[channel].append(int(file[separator + 1:]))
            else:
                CHANNELS_DB[channel] = [int(file[separator + 1:])]
    print(CHANNELS_DB)


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


def analyz(url, channel ="", id=""):
    global CONSOLE
    global VIDEO_PER_CHANNEL
    global FACE_PERCENT
    global DWNLD
    global VTF
    global CHANNELS_DB
    console = CONSOLE
    status = 0

    table = Table(show_header=True, header_style="bold magenta", show_lines=False, box=box.HEAVY_EDGE)
    table.add_column("Key", style="dim")
    table.add_column("Value")
    table.add_row("URL", url)

    start = url.find("@") + 1
    if start != 0:
        channel = url[start:url.find("/", start)]
    if id == "":
        id = url[url.rfind("/") + 1:]
    table.add_row("Channel", channel)
    limit = False
    try:
        limit = len(CHANNELS_DB[channel]) >= VIDEO_PER_CHANNEL or id in CHANNELS_DB[channel]
    except KeyError:
        limit = False
    finally:
        if limit:
            table.add_row("Result:", "Channel limit exceeded OR was added earlier", style="yellow")
            console.print(table)
            return 0, 0



    # анализирует видео по заданной ссылке и решает, удалить его или оставить
    # (если минимальный процент площади лица на протяжении всего видео больше FACE_PERCENT
    # то его видео сохраняется в папке done, а если меньше, то удаляется)

    video_file = DWNLD.dwnld(url, id + ".mp4")
    video_file = VTF.from_video_to_frames(video_file)
    if video_file == "":
        table.add_row("Result:", "Video cannot be loaded", style="red")
        console.print(table)
        return 0, 0

    path = video_file[:-4] + "\\"
    arr = []
    for frame_path in VTF.FRAMES_PATH:
        image = fc.load_image_file(frame_path)
        face_per = face_percent(image)
        arr.append(face_per)
        if face_per == 0:
            break

    m = min(arr)
    if m > FACE_PERCENT:
        table.add_row("Mean value:", str(mean(arr)) + " %", style="green")
        table.add_row("Min value:", str(m) + " %", style="green")
        try:
            CHANNELS_DB[channel].append(id)
        except KeyError:
            CHANNELS_DB[channel] = [id]

        done_path = video_file[:video_file.find("data")] + "done\\" + channel + "_" + id + ".mp4"
        try:
            os.rename(video_file, done_path)
        except FileExistsError:
            table.add_row("Result:", "File was added earlier", style="yellow")
        else:
            table.add_row("Result:", "Video is moved to Done", style="green")
            status = 1
    else:
        table.add_row("Mean value:", str(mean(arr)) + " %", style="red")
        table.add_row("Min value:", str(m) + " %", style="red")
        os.remove(video_file)
        table.add_row("Result:", "Video is deleted", style="red")

    shutil.rmtree(path)
    console.print(table)
    return m, status


def update_table(perc, s, f) -> Table:
    table = Table(show_header=False, show_lines=False, box=box.HEAVY_EDGE)
    table.add_column("Data", style="dim")
    table.add_column("Title")
    table.add_row("Average min %", perc)
    table.add_row("FAILS", f, style="red")
    table.add_row("SUCCESS", s, style="green")
    return table


def feed():
    arr = []
    global DELAY
    global DWNLD
    global CONSOLE
    console = CONSOLE
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    DWNLD = Downloader(driver, DELAY)
    driver.maximize_window()
    driver.get("https://www.tiktok.com/")
    try:
        WebDriverWait(driver, DELAY).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ev30f212")))
    except TimeoutException:
        raise Exception("NOT LOADED!")
    LogIn = TTLogger(driver, DELAY)
    LogIn.login()
    time.sleep(10)

    fails = 0
    success = 0
    with Live(auto_refresh=False, console=console) as live:
        for count in range(0, 10000):
            console.print(str(count))
            loaded = False
            while not loaded:
                try:
                    WebDriverWait(driver, DELAY).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "e1yey0rl4")))

                except TimeoutException:
                    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(0.5)
                else:
                    loaded = True
            try:
                elem = driver.find_element(By.CLASS_NAME, "e1yey0rl4")
                f_path = elem.find_element(By.XPATH, "./../../../../../..")
                chn = f_path.find_element(By.CLASS_NAME, "emt6k1z0").text

                url = elem.get_attribute("src")
            except Exception:
                console.print("SRC WASNT LOADED!")
            else:
                perc, stat = analyz(url, chn)
                if perc != -1:
                    arr.append(perc)
                if stat == 1:
                    f_path.find_element(By.CLASS_NAME, "e1hk3hf90").click()
                    success += 1
                else:
                    fails += 1
            ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.5)
            print("MEAN ARR: ", str(mean(arr)))
            live.update(update_table(str(mean(arr)), str(success), str(fails)), refresh=True)


def file():
    success = 0
    fails = 0
    global CONSOLE
    console = CONSOLE
    global DWNLD
    arr = []
    while True:
        file = input("URL file:")
        if os.path.exists(file):
            break
        else:
            console.print("File is not exist.")
    start = int(input("Start from:"))  # Нужна защита от дурака?

    with open(file, "r") as f:
        urls = f.readlines()
    urls = urls[slice(start, len(urls))]
    count = start

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    DWNLD = Downloader(driver, DELAY)
    driver.maximize_window()

    console.print("\n")
    with Live(auto_refresh=False, console=console) as live:
        for url in urls:
            count += 1
            console.print(count)
            res, stat = analyz(url[:-1])
            if res != -1:
                arr.append(res)
            if stat == 1:
                success += 1
            else:
                fails += 1
            live.update(update_table(str(mean(arr)), str(success), str(fails)), refresh=True)


def main():
    global CONSOLE
    global VTF
    CONSOLE = Console()
    db_init()
    VTF = VidToFrames(1)
    is_file = Prompt.ask("From file or feed?", choices=["file", "feed"], default="feed")
    if is_file == "file":
        file()
    else:
        feed()


if __name__ == '__main__':
    main()
