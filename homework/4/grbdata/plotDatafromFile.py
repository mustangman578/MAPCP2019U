import os

filelist = os.listdir()

for i in filelist:
    if i.endswith('.txt'):
        with open(i,'r',encoding='ascii') as y:
            try:
                for line in y:
                    data = line.split('\\n')
            except:
                pass
