#coding=utf-8

import os
import sys


#E:\工作\港澳台客户端\19-06.04-v1.5.59-港澳台google换包\fanti-tssy-v1.5.29.2012_6_obb_0604.apk
reload(sys)
sys.setdefaultencoding('utf-8')

def encodeString(string):
	return string.encode('gbk')


while True:
	apkpath = raw_input(encodeString("请拖入要检查的apk："))

	#aapt dump badging C:\Users\hc\Desktop\MyActivity.apk
	info = os.popen("aapt.exe dump badging " + apkpath).readlines()

	print "\n"
	for i in range(3):
		print info[i]
	print "*"*100