import shutil
from selenium import webdriver
import os
import face_recognition as fc
from PIL import Image
from rich.console import Console
from downloader import Downloader
from vid_to_frames import VidToFrames
import concurrent.futures



FACE_PERCENT = 17
DELAY = 30
VIDEO_PER_CHANNEL = 3


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


def analyz(url, check_per, check_count):
    VTF = VidToFrames(1)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    DWNLD = Downloader(driver, DELAY)
    id = url[url.rfind("/") + 1:]

    video_file = DWNLD.dwnld(url, id + ".mp4")
    video_file = VTF.from_video_to_frames(video_file)
    if video_file == "":
        driver.close()
        print("Cannot be proceed - ", url)
        return 0

    path = video_file[:-4] + "\\"
    for frame_path in VTF.FRAMES_PATH:
        image = fc.load_image_file(frame_path)
        face_per = face_percent(image)
        if face_per < check_per:
            print("NOT PASSED - ", url)
            shutil.rmtree(path)
            os.remove(video_file)
            return 0
    driver.close()
    shutil.rmtree(path)

    start = url.find("@") + 1
    channel = url[start:url.find("/", start)]
    id = url[url.rfind("/") + 1:]

    count_channel = 0
    dict = os.path.dirname(__file__) + "\\done\\"
    for file in os.listdir(dict):
        if file.startswith(channel + "_"):
            count_channel += 1
            if file.endswith(id + ".mp4") | (count_channel >= check_count):
                print("Channel limit exceeded OR was added earlier - ", url)
                os.remove(video_file)
                return 0


    done_path = video_file[:video_file.find("data")] + "done\\" + channel + "_" + id + ".mp4"
    try:
        os.rename(video_file, done_path)
    except FileExistsError:
        print("File was added earlier - ", url)
        os.remove(video_file)
        return 0
    finally:
        print("Video is moved to Done", url)
        return 1


def file():
    success = 0
    fails = 0
    console = Console()
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

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(
            analyz, url[:-1], FACE_PERCENT, VIDEO_PER_CHANNEL) for url in urls]

        for f in concurrent.futures.as_completed(results):
            count += 1
            if f.result() == 1:
                success += 1
            else:
                fails += 1
            print("SUCCESS: ", success, "\tFAILS: ", fails)


def main():
    file()


if __name__ == '__main__':
    main()
