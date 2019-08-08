import sys


infile = sys.argv[1]
outfile = sys.argv[2]

myFile=open('infile', 'r')
outfile=open ('outfile', 'w')

for line in myFile:
    new_line = (line.split(','))
    for i in new_line:
