#!/usr/bin/python2.7
#coding=utf-8

import os
import re

def reString(pattern,reString):
    return re.findall(pattern,reString)  

def koreaPush():
    resPath = raw_input("请拖入想要单独推送的目录：")
    #resPath = r"e:\cdn_korea\android_test\v1.5.4.2011"

    disk = resPath[0].lower() #读取盘符，并转换成小写
    localResPath = resPath[2:].replace("\\","/") #提取本地资源地址
    cndPath = reString(r"\\android.*\d|\\ios.*\d",resPath)[0].replace("\\","/") #提取要推送的cdn地址

    #print localResPath
    #print cndPath
    #print disk

    pushCommand = "rsync -avzP /mnt/" + disk + localResPath + "/ gamebf@211.43.14.116::cdn" + cndPath + " --password-file=/home/chenquan/bfgame.pass --port=8337"
    # rsync -avzP /mnt/e/cdn_korea/android_test/v1.5.4.2011/ gamebf@211.43.14.116::cdn/android_test/v1.5.4.2011 --password-file=/home/chenquan/bfgame.pass --port=8337
    os.system(pushCommand)
while True:
    koreaPush()