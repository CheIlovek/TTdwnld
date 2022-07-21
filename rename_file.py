import os

directory = input()
files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+'/'+path)])

i = 0

while files:
        file = files[0]
        ext = file.split('.')[-1]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            name = f'{i}.{ext}'
            os.rename(directory + '/' + file, directory + '/' + name)
            del files[0]
        i+=1