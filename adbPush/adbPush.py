#coding=utf-8
import sys
import re
import os

reload(sys)
sys.setdefaultencoding('utf-8')


#直接定义为2个方法，方便调用
def encodeString(string):
    return string.encode("gbk")

#直接定义为2个方法，方便调用
def decodeString(string):
    return unicode(string, encoding='utf-8')
def reString(pattern,reString):
    return re.findall(pattern,reString)  

path  = raw_input(encodeString("请拖入要推送到安卓模拟器的obb："))

#E:\工作\港澳台客户端\19-07.16-v1.5.70-泰国版google包\obb\main.1.com.wondergame.tssyandsea.obb
file_name = reString("main.*.obb",path)[0]
package_name = reString("com.*?(?=.obb)",path)[0]

push_command = "adb push " + path + " " + "/storage/emulated/0/Android/obb/" + package_name + "/" + file_name

print file_name
print package_name
print push_command

os.system("adb connect 127.0.0.1:7555")
os.system(push_command)
print encodeString("obb文件推送成功！")