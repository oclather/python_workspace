#coding=utf-8
import re
import os

def openFile(filepath): #读取文件，按\n分割成列表
    s = open(filepath,"r")
    s_info = s.read()
    s.close()
    return s_info.split("\n")

def copyFile(filePath,dstPath):
#    os.system("mkdir diff_files")
    os.popen("copy "+filePath+dstPath)

def writeFile(xxx):
    s = open("diffinfo.txt","w")
    for i in xxx:
        s.write(i +'\n')
    s.close()
    
def diffFiles(filename1, filename2):
    f1 = open(filename1,"r")
    f2 = open(filename2,"r")
    data1 = f1.read()
    data2 = f2.read()
    diffienceInfo = []
    temp1 = data1.split("\n")
    temp2 = data2.split("\n")
    n = 0
    for i in temp2:
        if i not in temp1:
            diffienceInfo.append(i)
            n += 1
        else:
            pass
    print "All complete!"
    print str(n) + " diffs."

    f1.close()
    f2.close()
    writeFile(diffienceInfo)

#使用reString(a,b)这个方法，返回的是一个列表，要调用列表中的第一个内容，请使用reString(a,b)[0]
def reString(pattern,reString):
    return re.findall(pattern,reString)


configList = openFile("./config.txt")

info1 = configList[0] #读取config.txt中的第一行：对比文件基础版本
info2 = configList[1] #读取config.txt中的第二行：对比文件最新版本
copypath = reString(".*\\\\",info2)[0] #根据第二行，获取需要复制的源文件的位置
dstPath = configList[2] #读取config.txt中的第三行：复制文件的目标存放位置
diffFiles(info1,info2)

diffinfo = openFile("./diffinfo.txt")
os.popen("rmdir /s /q " + dstPath)
#os.popen("mkdir " + dstPath)
count = 0
print "Is copying! Please wait a moment..."
for i in diffinfo:
    filename = reString(".*\..* ",i) #获取info中的文件路径和文件名,后面带1个空格，使用copy命令时则不用继续加空格。不要后面的md5
    os.popen("mkdir " + dstPath)

    if filename:#这里为了判断是否是文件夹，如果是文件夹，则不进行后续的复制操作；否则创建文件夹结构再复制到对应文件夹下
        filepath = reString(".*/",filename[0])
        if len(filepath) == 0 : #如果这里内部没有文件夹，则直接复制
            copyFilepath = copypath + filename[0]
            copyFilepath = copyFilepath.replace("/","\\")
            copyFile(copyFilepath,dstPath)
        else: 
            copyFilepath = copypath + filename[0] #组成将要复制的源文件的路径和文件名
            dstPath2 = dstPath + filepath[0] #组成目标文件夹的路径
            copyFilepath = copyFilepath.replace("/","\\")
            dstPath2 = dstPath2.replace("/","\\")
            os.popen("mkdir " + dstPath2) #创建内部文件夹结构
            copyFile(copyFilepath,dstPath2)
        count += 1
print "Everything is OK"
print str(count) + " files copy complete!"
    
