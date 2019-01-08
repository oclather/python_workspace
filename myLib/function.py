#coding=utf-8
from colorama import  init, Fore, Back, Style
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('utf-8')

init(autoreset=True)
class Colored(object):
 
    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.RED + s + Fore.RESET
 
    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.GREEN + s + Fore.RESET
 
    #  前景色:黄色  背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET
 
    #  前景色:蓝色  背景色:默认
    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET
 
    #  前景色:洋红色  背景色:默认
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET
 
    #  前景色:青色  背景色:默认
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET
 
    #  前景色:白色  背景色:默认
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET
 
    #  前景色:黑色  背景色:默认
    def black(self, s):
        return Fore.BLACK
 
    #  前景色:白色  背景色:绿色
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET

        #直接定义为2个方法，方便调用
def encodeString(string):
    return string.encode("gbk")

#直接定义为2个方法，方便调用
def decodeString(string):
    return unicode(string, encoding='utf-8')

def openFile(filename):
    s = open(filename,"r")#"r"方式读时的'\r\n'会被系统自动替换为'\n'；"rb"方式读时的'\r\n'不会被自动替换
    s_info = s.read()
    s.close()
#    return s_info.split("\n")
    return s_info

def openFileLine(filename):
    s = open(filename,"r")
    s_info = s.readline()
    s.close()
    return s_info

def writeFile(filename,xxx):
    s = open(filename,"wb")#"w"方式写时的'\n'会被系统自动替换为'\r\n'；"wb"方式写时的'\n不会被自动替换
    s.write(xxx)
    s.close()

def reString(pattern,reString):
    return re.findall(pattern,reString)  

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
    writeFile("diffinfo.txt",diffienceInfo)

'''----------------------------------------------------------'''
pc_diff_path = r"C:\workspace\svn\v1.5.0_20181114_korean\diff\client\pc"
android_diff_path = r"C:\workspace\svn\v1.5.0_20181114_korean\diff\client\android"
ios_diff_path = r"C:\workspace\svn\v1.5.0_20181114_korean\diff\client\ios"
base_target_path = r"C:\workspace\svn\v1.5.0_20181114_korean\client\AllRes\chs\fullRes"
exclude_folder = "\\\\fx\\\\|\\\\scene\\\\|\\\\actor\\\\|\\\\audio\\\\"  #这里设置要排除的文件夹。要新增，则后面加：|\\\\audio\\\\这种形式即可

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
        
def getLastSvnVersion(svn_path):
	svn_info = os.popen("svn info " + svn_path).readlines()
	last_version = reString("\d.*\d",svn_info[-7])[0]
	return last_version

def svnLog(svn_path,begin_version,last_version):
	svn_log = os.popen("svn log -v -r " + begin_version + ":" + last_version + " " + svn_path).readlines()
	if int(last_version) - int (begin_version) > 400:
		print encodeString("需要查询的log日志太多了，请查询少于200个版本的记录")
		return []
	else:
		return svn_log
