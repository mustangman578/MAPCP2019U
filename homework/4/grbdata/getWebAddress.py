import urllib.request


file = open('triggers.txt','r')
for line in file:
    new_file = line.split('\\n')
for i in new_file:
    try:
        mystr = ('https://www.cdslab.org/ICP2017F/homework/5-problems/swift/GRB%s_ep_flu.txt' %i)
        x = urllib.request.urlopen(mystr)
        grbFile = open(i+'.txt','w')
        grbFile.write(str(x.read()))
        grbFile.close()
    except:
        continue
