from tempfile import mkstemp
from os import close
from shutil import move
import time

def write_lines(file):
    T = time.time()
    ft, temp = mkstemp()
    lines = []
    count = 0
    with open(temp, 'w') as t, open(file) as f:
        for line in f:
            count += 1
            if (count % 10000 == 0):
                print(count)
            if (line not in lines) and not line.startswith("https://p"):
                lines.append(line)
                t.write(line)
    close(ft)
    move(temp, file)
    T = time.time() - T
    print(f"Program running time is {T} seconds")


if __name__ == '__main__':
    write_lines(file="urls.txt")


