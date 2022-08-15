import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import concurrent.futures
import face_recognition as fc
from PIL import Image
PERSENT = 15


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

def analyz(src):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.chrome
    }
    src = src[:-1]
    print(src)
    s = requests.Session()
    s.trust_env = True
    r = s.get(url=src, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    img = soup.find('img', class_="e1yey0rl1")
    prev = s.get(url=img['src'], headers=headers)
    start = src.find("@") + 1
    channel = src[start:src.find("/", start)]
    ids = src[src.rfind("/") + 1:]
    file_name = 'images/' + channel + "_" + ids + ".jpg"
    with open(file_name, "wb") as f:
        f.write(prev.content)
    image = fc.load_image_file(file_name)
    face_per = face_percent(image)
    if (face_per < PERSENT):
        os.remove(file_name)
    else:
        print("OK - ", file_name)


def main():
    file = "buff4.txt"
    with open(file, "r", encoding="utf-8") as f:
        urls = f.readlines()
    start = int(input("Start from:"))
    finish = int(input("End to:"))
    if (finish == -1):
        urls = urls[start:]
    else:
        urls = urls[start:finish]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(analyz, url) for url in urls]




if __name__ == '__main__':
    main()