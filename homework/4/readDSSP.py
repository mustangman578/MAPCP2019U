import os
import sys

outfile = sys.argv[1]



myFile=open("1A2T_A.dssp", 'r')
outfile=open (outfile, 'w')
    
AAlist = []
AAdict = {
        'A': 129.0,
        'R': 274.0,
        'N': 195.0,
        'D': 193.0,
        'C': 167.0,
        'Q': 225.0,
        'E': 223.0,
        'G': 104.0,
        'H': 224.0,
        'I': 197.0,
        'L': 201.0,
        'K': 236.0,
        'M': 224.0,
        'F': 240.0,
        'P': 159.0,
        'S': 155.0,
        'T': 172.0,
        'W': 285.0,
        'Y': 263.0,
        'V': 174.0,
                }
    
    
lineNum = 0

outfile.write('pdb  name  ACC  RSA\n')
    
for lines in myFile:
    lineNum += 1
        
    if lineNum <= 25:
        continue
            
    else:
        try:
            maximum_surface_area_from_table = int(AAdict[lines[13]])
            ACC = int(lines[35:38])
            
            RSA = ACC/maximum_surface_area_from_table
            
            
            print("1A2T_A  ", lines[13], ACC, RSA)
            
        except:
            continue
        new = "1A2T_A  "+" "+str(lines[13])+" "+str(ACC)+" "+str(RSA)+'\n'
        

    outfile.write(new)               
myFile.close()
outfile.close()
