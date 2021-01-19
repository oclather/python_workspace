#coding=utf-8

import os
import sys
import re
import zipfile

#E:\工作\港澳台客户端\19-06.04-v1.5.59-港澳台google换包\fanti-tssy-v1.5.29.2012_6_obb_0604.apk
#D:\bat\checkAndroidVersion\ttzg_gfblmzh_U.apk

reload(sys)
sys.setdefaultencoding('utf-8')

def encodeString(string):
	return string.encode('gbk')

def reString(pattern,reString):
    return re.findall(pattern,reString) 

def openFile(filename):
    s = open(filename,"r")#"r"方式读时的'\r\n'会被系统自动替换为'\n'；"rb"方式读时的'\r\n'不会被自动替换
    s_info = s.read()
    s.close()
    return s_info#.split("\n")

def extractFiles(extractfiles,apkpath):#提取包内的单个文件
	zFile = zipfile.ZipFile(apkpath,'r')
	zFile.extract(extractfiles,path=None, pwd=None) #提取xml文件
	zFile.close()


def printLebinInfo():
	if os.path.isfile("Manifest.xml"):
		info = openFile(r"Manifest.xml")
		LEBIAN_VERCODE = reString(r'android:name="LEBIAN_VERCODE".*\n.*',info)
		ClientChId = reString(r'android:name="ClientChId".*\n.*',info)
		if len(LEBIAN_VERCODE):
			print LEBIAN_VERCODE[0].replace("\n\t","") #打印中去掉换号，格式美观点
		else:
			print encodeString("当前包没有LEBIAN_VERCODE字段。"+ "\n")
		if len(ClientChId):
			print ClientChId[0].replace("\n\t","")
		else:
			print encodeString("当前包没有ClientChId字段。"+ "\n")		
	else:
		print encodeString("找不到解密后的Manifest.xml文件，请检查重试")


InfoFilePath = ['info.txt','opinfo.txt']

while True:
	apkpath = raw_input(encodeString("请拖入要检查的apk："))

	#aapt dump badging C:\Users\hc\Desktop\MyActivity.apk
	info = os.popen("aapt.exe dump badging " + apkpath).readlines()

	#for i in info:
	#	print i
	print "\n"
	for i in info:
		if reString(r"package: name.*.\n",i):
			print i
		if reString(r"sdkVersion:.*.\n",i):
			print i
		if reString(r"targetSdkVersion:.*.\n",i):
			print i
		if reString(r"launchable-activity:.*?  ",i):
			print encodeString(i)
		else:
			pass
	print "--"*20

	zFile = zipfile.ZipFile(apkpath,'r')
	for InfoFileName in InfoFilePath:
		data = zFile.read('assets/res/'+InfoFileName)
		infoContent = data
		if len(infoContent)>0:
			sp = infoContent.splitlines()
			print InfoFileName+encodeString("版本为：")+sp[0] 
		else:
			print encodeString("读取")+InfoFileName+encodeString("错误，无内容" )
	zFile.close()
	print "\n"
	print "--"*20

	extractFiles("AndroidManifest.xml",apkpath)#提取AndroidManifest文件
	os.system('java -jar AXMLPrinter2.jar  AndroidManifest.xml > Manifest.xml')#解密xml文件
	printLebinInfo()
	os.system("del AndroidManifest.xml Manifest.xml") #检查完后，删除解密前后的2个文件
	print "*"*100