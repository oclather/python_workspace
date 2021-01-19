#coding=utf-8
import re
import os
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


def encodeString(string):
    return string.encode('gbk')

def openFile(filepath): #读取文件，按\n分割成列表
    s = open(filepath,"r")
    s_info = s.read()
    s.close()
    return s_info.split("\n")

def copyFile(filePath,dstPath):
#    os.system("mkdir diff_files")
    print encodeString("复制差异文件:")+ filePath+dstPath
    os.popen("copy /y "+filePath+dstPath)
 
def delFile(filePath):
    os.popen("del " + filePath)

def writeFile(xxx,filename):
    s = open(filename,"w")
    for i in xxx:
        s.write(i +'\n')
    s.close()
    
def diffFiles(filename1, filename2,difff_filename):
    f1 = open(filename1,"r")
    f2 = open(filename2,"r")
    data1 = f1.read()
    data2 = f2.read()
    diffienceInfo = []
    temp1 = data1.split("\n")
    temp2 = data2.split("\n")
    n = 0
    for i in temp1:
        if i not in temp2:
            diffienceInfo.append(i)
            n += 1
        else:
            pass
    print "Compare complete!"
    print difff_filename + ":" + str(n) + " diffs."
    print "-"*50

    f1.close()
    f2.close()
    writeFile(diffienceInfo,difff_filename)

#使用reString(a,b)这个方法，返回的是一个列表，要调用列表中的第一个内容，请使用reString(a,b)[0]
def reString(pattern,reString):
    return re.findall(pattern,reString)


def copy_diff_file(diffinfo_file,copypath,dstPath):
    copied_info = openFile(diffinfo_file)
    count = 0
    print "Is copying! Please wait a moment..."
    for i in copied_info:
        filename = reString(".*? ",i) #获取info中的文件路径和文件名,后面带1个空格，使用copy命令时则不用继续加空格。不要后面的md5

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




def main():
    zipfile = raw_input(encodeString(r"请输入要解压的资源zip包："))
    #X:\9130_android\v1.5.103.2015_0927-143529.zip

    targetpath = raw_input(encodeString(r"请输入要解压的目标位置，如：E:\cdn_9187\android 以平台结尾："))
    #targetpath = r"E:\cdn_korea\android"
    version = reString(r"v\d{1,4}.\d{1,4}.\d{1,4}.\d{1,4}",zipfile)[0] #原来的正则：(?<=android\\).*?(?=_)|(?<=ios\\).*?(?=_)

    hotinfo_old = targetpath + "\\" + version + "\\hot\\res\\info.txt"
    #print hotinfo_old
    hotinfo_new = "C:\\temp" + "\\" + version + "\\hot\\res\\info.txt"
    #print hotinfo_new
    opinfo_old = targetpath + "\\" + version + "\\optional\\res\\opinfo.txt"
    #print opinfo_old
    opinfo_new = "C:\\temp" + "\\" + version + "\\optional\\res\\opinfo.txt"
    #print opinfo_new
    copypath1 = "C:\\temp\\" + version + "\\hot\\res\\"
    copypath2 = "C:\\temp\\" + version + "\\optional\\res\\"
    dstPath1 = targetpath + "\\" + version + "\\hot\\res\\"
    #print dstPath1
    dstPath2 = targetpath + "\\" + version + "\\optional\\res\\"
    #print dstPath2

    if os.path.exists(hotinfo_old):#判断是否已经有旧资源。
        print encodeString("目标位置已存在文件夹：" + dstPath1 )#根据是否存在hot/res/info.txt来判断是不是已经解压过
        print encodeString("将进行对比差异再覆盖！")
        print encodeString("正在清理临时目录...")
        os.popen("rmdir /s /q C:\\temp") #先清理临时目录
        print encodeString("清理完成")
        print "-"*50
        os.system("7z x " + zipfile + " -oC:\\temp" )

        diffFiles(hotinfo_new,hotinfo_old,"info_diff_new-old.txt")#新的info和旧的info对比，获得差异文件，用于复制
        diffFiles(opinfo_new,opinfo_old,"opinfo_diff_new-old.txt")#新的opinfo和旧的opinfo对比，获得差异文件，用于复制
        
        if os.path.getsize("info_diff_new-old.txt") > 0:    #判断差异文件是否为空。   
            copy_diff_file("info_diff_new-old.txt" , copypath1 , dstPath1)
            copyFile(hotinfo_new," "+dstPath1)
        else:
            print encodeString("hot没有差异，不复制！")
            print "-"*50

        if os.path.getsize("opinfo_diff_new-old.txt") > 0:   #判断差异文件是否为空。  
            copy_diff_file("opinfo_diff_new-old.txt", copypath2 , dstPath2) 
            copyFile(opinfo_new," "+dstPath2)
        else:
            print encodeString("op没有差异，不复制！")
            print "-"*50

        print encodeString("正在清理临时目录...")
        os.popen("rmdir /s /q C:\\temp") #先清理临时目录
        print encodeString("清理完成")
        '''
        print encodeString("正在清理临时目录...")
        os.popen("rmdir /s /q C:\\temp")
        print encodeString("清理完成")
        print "-"*50
        '''
    else: #没有旧资源旧直接解压
        print encodeString("目标位置没有该版本资源，直接解压文件！")
        os.system("7z x " + zipfile + " -o" + targetpath)

if __name__ == '__main__':
    main()
