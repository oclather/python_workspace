#coding=utf-8

import os
import re


filename1 = "./chayi.txt"

#filename2 = input("Second file path:")
f1 = open(filename1,"r")
#f2 = open(filename2,"r")

data = f1.read()
f1.close()


def writeFile(xxx):
    s = open("difference.txt","w")
    temp = xxx.split("\n")
    for i in temp:
        a = i.replace("svn://192.168.10.245/front/cdn/","E:\\cdn\\")
        a = a.replace("/","\\")
        s.write(a +'\n')
    s.close()

def copyFile(filePath):
    os.system("copy "+filePath+" .\\temp\\")




temp = data.split("\n")
pattern = re.compile("/v.*/.*\.")
os.system("mkdir temp")
a = []
n = 0
for i in temp:
    if re.findall(pattern,i) != []:
        i = i.replace("svn://192.168.10.245/front/cdn/","E:\\cdn\\")
        i = i.replace("/","\\")
        copyFile(i)
        n = n+1
    else:
        a.append(i)
    
print str(n) + " files."

print "can't copy:"
for i in a:
    print i 


#print "1111" +str( re.findall("/v.*/.*\." ,"svn://192.168.10.245/front/cdn/android/v1.3.22.2000/optional/res/scene/mat/8511871839136a2d3cc3042000a78704.unity3d"))