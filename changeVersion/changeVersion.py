#coding=utf-8
import re
import os
import color

def openFile(filename):
    s = open(filename,"r")#"r"方式读时的'\r\n'会被系统自动替换为'\n'；"rb"方式读时的'\r\n'不会被自动替换
    s_info = s.read()
    s.close()
    return s_info.split("\n")

def openFileLine(filename):
    s = open(filename,"r")
    s_info = s.readline()
    s.close()
    return s_info

def writeFile(filename,xxx):
    s = open(filename,"wb")#"w"方式写时的'\n'会被系统自动替换为'\r\n'；"wb"方式写时的'\n不会被自动替换
    n = 0
    for i in xxx:
        if n != len(xxx)-1: #用来判断是否是最后一行，如果到最后一行，则不输入回车，防止多出一个空行
            s.write(i+"\n")
        else:
            s.write(i)
        n += 1
    s.close()

def reString(pattern,reString):
    return re.findall(pattern,reString)  

#具体替换的实现方法：
def changeVersion(filename,version):
    version_list = openFile(filename)#读取文件内容
    version_list[0] = version[0] #替换第一行内容
    writeFile(filename,version_list)#将文件内容重新写入
    print "The new version is:" + color.colorText.yellow(openFileLine(filename))
    print "Write" + color.colorText.red(filename) + color.colorText.green(" sucdess\n")
    print "*"*80
while 1:
    filepath = raw_input(r"please input filepath:").strip()#用raw_input  才不会出现windows路径报错的问题；strip() 用来去掉结尾的\r
    print "*"*80
    version = reString(r"v\d.*\d$",filepath)
    filename1 = filepath + r'\hot\res\info.txt'
    filename2 = filepath + r'\optional\res\opinfo.txt'
    changeVersion(filename1,version)
    changeVersion(filename2,version)

    