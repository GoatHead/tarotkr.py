import os
import re
path = 'your_img_path'
minor = {'Cups': 36 , 'Swords': 50 , 'Pents' :  64 , 'Wands': 22}
for fname in os.listdir(path):
    if fname[-3:] == 'png':
        onlyname = fname[:-4]
        if 'RWS' in onlyname:
            number = int(re.search(r'\d+', onlyname).group())
            newname = '[{:02}] {}.png'.format(number, onlyname)
            os.rename(path + fname, path + newname)
        if onlyname[0] != '[' and onlyname[:-2] in minor:
            name = onlyname[:-2]
            number = onlyname[-2:]
            convnum = minor[name] + 14 - int(number)
            newname='[{}] {}.png'.format(convnum, onlyname)
            os.rename(path+fname, path+newname)
