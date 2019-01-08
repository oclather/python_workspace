#coding=utf-8

import os
import re


filename1 = "./chayi.txt"

#filename2 = input("Second file path:")
f1 = open(filename1,"r")
#f2 = open(filename2,"r")

data = f1.read()
f1.close()

def copyFile(filePath):
    os.system("copy "+filePath+" .\\temp\\")




temp = data.split("\n")
a = []

pattern = re.compile("/v.*/.*\.")
os.system("mkdir temp")
n = 1
for i in temp:
    i = i.replace("\\","/")
    if re.findall(pattern,i) != []:
        i = i.replace("/","\\")
        copyFile(i)
        #print i
        n = n+1
    #print i
    else:
        a.append(i)
    
print str(n) + " files."

print "can't copy:"
for i in a:
    print i 
