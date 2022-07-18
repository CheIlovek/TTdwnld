import json

def main():
    f = open("total.txt", "r")
    urls = f.readlines()
    f.close()

    channels = {}

    for url in urls:
        start = url.find("@") + 1
        chan = url[start:url.find("/", start)]
        try:
            value = channels[chan]
        except KeyError:
            channels[chan] = 0
    print(channels)



if __name__ == '__main__':
    main()