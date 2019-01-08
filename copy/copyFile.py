#coding=utf-8
import re
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#根据本地实际情况，修改下列参数。
pc_diff_path = r"C:\workspace\svn\v1.5.0_20181114_korean\diff\client\pc"
android_diff_path = r"C:\workspace\svn\v1.5.0_20181114_korean\diff\client\android"
ios_diff_path = r"C:\workspace\svn\v1.5.0_20181114_korean\diff\client\ios"
base_target_path = r"C:\workspace\svn\v1.5.0_20181114_korean\client\AllRes\chs\fullRes"
exclude_folder = "\\\\fx\\\\|\\\\scene\\\\|\\\\actor\\\\|\\\\audio\\\\"  #这里设置要排除的文件夹。要新增，则后面加：|\\\\audio\\\\这种形式即可


def encodeString(string):
	return string.encode('gbk')

def decodeString(string):
	return unicode(string, encoding='utf-8')

def reString(pattern,reString):
    return re.findall(pattern,reString)

def copyFile(filePath,dstPath):
    a = os.popen("copy /y "+filePath+" "+dstPath)
    if a.readlines():
    	return True
    else:
    	print encodeString("复制文件出错，请手动复制：") + filePath
    	return False

def getFileList(file_path):
	file_list = os.popen("dir /s /b " + file_path).readlines()
	return file_list

def copyFileToTarget(file_list,file_path,target_path):
	count = 0
	print encodeString("正在复制文件，请稍等。。。")
	for i in file_list:
		a = reString("\\\\res.*\..*\\n",i) #查找文件路径，排除文件夹路径
		b = reString(exclude_folder,i) #查找带有这些关键字的文件路径

		if a and (not b): #排除带有b里面关键字的文件路径
			file_name = a[0].strip("\n")
			#print file_path + file_name
			#print  target_path + file_name
			if copyFile(file_path + file_name , target_path + file_name):#判断是否复制成功。
				count = count + 1
			else:
				pass
		else:
			pass
	print "copy " + str(count) + " files!"

def updateSvn(svn_path):
	os.system("svn up " + svn_path)


def exclude():#用于让用户选择：复制时是否排除某些文件夹
	print exclude_folder
	a = raw_input(encodeString("是否要排除复制以上文件夹？（直接回车排除，有任何输入则不排除）"))
	if a :
		print "*"*40
		print encodeString("	您选择：不排除！")
		print "*"*40
		return "veliuisvbmuurude"#这里是随便输入的，目的让他不排除任何带有这段字符的路径
	else:
		print "*"*40
		print encodeString("	您选择：排除！")
		print "*"*40
		return exclude_folder

while True:
	print "-"*80
	case = raw_input(encodeString('''请输入操作编号：
	1、更新pc并复制diff到资源目录
	2、更新android并复制diff到资源目录
	3、更新ios并复制diff到资源目录
'''))
	if case == "1":
		print "-"*80
		exclude_folder = exclude()
		pc_target_path = base_target_path + "\pc\\v0.0.0.1"
		updateSvn(pc_diff_path)
		copyFileToTarget(getFileList(pc_diff_path),pc_diff_path,pc_target_path)

	elif case == "2":
		print "-"*80
		exclude_folder = exclude()
		android_version = raw_input(encodeString("请输入要覆盖的android版本号："))
		android_target_path = base_target_path + "\\android\\" + android_version
		#print android_target_path
		updateSvn(android_diff_path)
		copyFileToTarget(getFileList(android_diff_path),android_diff_path,android_target_path)

	elif case == "3":
		print "-"*80
		exclude_folder = exclude()
		ios_version = raw_input(encodeString("请输入要覆盖的ios版本号："))
		ios_target_path = base_target_path + "\\ios\\" + ios_version
		#print ios_target_path
		updateSvn(ios_diff_path)
		copyFileToTarget(getFileList(ios_diff_path),ios_diff_path,ios_target_path)
	else :
		print "-"*80
		print "I do not know!"