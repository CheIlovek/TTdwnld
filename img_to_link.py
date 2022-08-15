import os

def main():
    directory = "images"
    urls = []
    for path in os.listdir(directory):
        path = path[:-4]
        sep = path.rfind("_")
        channel = path[:sep]
        id = path[sep+1:]
        urls.append("https://www.tiktok.com/@" + channel + "/video/" + id + '\n')

    with open("urls.txt", 'w') as f:
        f.writelines(urls)



if __name__ == '__main__':
    main()