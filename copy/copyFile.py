#coding=utf-8
import re
import os
import sys
import time
import hashlib

reload(sys)
sys.setdefaultencoding('utf-8')

#根据本地实际情况，修改下列参数。
#-----------------------------------------
contury = sys.argv[1]#这里配置区域代码。直接从bat脚本中获取
exclude_word = "\\\\fx\\\\|\\\\scene\\\\|\\\\actor\\\\|\\\\audio\\\\"  #这里设置要排除的文件夹。要新增，则后面加：|\\\\audio\\\\这种形式即可
check_diff_sync_path = ("lua","exlfile","pb") #这里配置需要检查的文件夹（只有多平台没有差异的文件夹才有检查意义。不然平台不同，对比全都是差异）
#-----------------------------------------

def openFile(filepath): 
    s = open(filepath,"r")
    s_info = s.read()
    s.close()
    return s_info

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
	file_list = os.popen("dir /s /b " + file_path).read()
	file_list_a = file_list.split("\n") #用换行分割为列表，但是最后会生成一个空元素
	file_list_a.remove('') #去除末尾的空元素
	file_list_b = []
	for i in file_list_a:
		if os.path.isfile(i):
			file_list_b.append(i) #将所有文件加入列表file_list_b
	return file_list_b,len(file_list_b)#返回file_list和文件数量的二维数组


def copyFileToTarget(file_list,file_path,target_path):
	count = 1
	temp_list = []
	#print encodeString("文件总数：") + str(file_li1st[1])
	print encodeString("正在复制文件，请稍等。。。")
	for i in file_list[0]:

		a = reString("\\\\res.*\..*",i) #从文件列表中提取res/后面的文件名
		b = reString(exclude_folder,i) #查找带有这些关键字的文件路径

		if a and (not b): #排除带有b里面关键字的文件路径
			file_name = a[0]
			#print file_path + file_name 
			#print  target_path + file_name
			temp_list.append(file_name)#将需要复制的文件名，加入到这个临时列表
		else:
			pass


	for i in temp_list:
		if int (count*100/len(temp_list)) < 10:
			sys.stdout.write(str(int (count*100/len(temp_list))) + "%"  + "\b\b" ) #显示进度
			sys.stdout.flush()
		else:
			sys.stdout.write(str(int (count*100/len(temp_list))) + "%"  + "\b\b\b" ) #显示进度
			sys.stdout.flush()


		if copyFile(file_path + i , target_path + i):#判断是否复制成功。
			count = count + 1
		else:
			pass

	print     #这里就是这样的，删除这行进度会显示异常。
	print "copy " + str(count-1) + " files!"

def updateSvn(svn_path):
	os.system("svn up " + svn_path)

def svnLog(svn_path):
	os.system("svn log -v -l 5 " + svn_path)

def exclude():#用于让用户选择：复制时是否排除某些文件夹
	print exclude_word
	a = raw_input(encodeString("是否要排除复制以上文件夹？（直接回车排除，有任何输入则不排除）"))
	if a :
		print "*"*40
		print encodeString("	您选择：不排除！")
		print "*"*40
		return "veliuisvbmuurude"#这里是随便输入的，目的让他排除任何带有这段字符的路径
	else:
		print "*"*40
		print encodeString("	您选择：排除！")
		print "*"*40
		return exclude_word

#以下为新增的方法，用于对比diff中的文件差异
def getFileMd5(file_path):
	s = open(file_path,"rb")
	s_info = s.read()
	hash_md5 = hashlib.md5(s_info)
	return hash_md5.hexdigest()

def compareDic(dic_a,dic_b,parame_a,parame_b):
	result1 = []
	result2 = []
	for i in dic_a: #从字典a中返回所有key
		value_a = dic_a[i] #根据key，获得对应的value
		i = i.replace(parame_a,parame_b) #将key中的a参数，替换为b参数，用于查找b字典中是否有a元素	
		if i in dic_b: #判断字典a中的文件是否在字典b中存在
			value_b = dic_b[i] #根据替换后的key，获得b字典中对应的value
			if value_a == value_b:
				pass
			else:
				result1.append(i) #这里是判断有文件md5差异的，放入这里
		else:
			result2.append(i) #这里是判断有文件缺失的，放入这里
	amount_a = len(dic_a)
	amount_b = len(dic_b)
	if amount_a != amount_b:
		print parame_a + encodeString("有：") + str(amount_a)+ encodeString("个文件!    ") + parame_b + encodeString("有：") + str(amount_b) + encodeString("个文件!") + encodeString("    文件数量有差异，请检查")
	else:
		print parame_a + encodeString("有：") + str(amount_a)+ encodeString("个文件!    ") + parame_b + encodeString("有：") + str(amount_b) + encodeString("个文件!")
	
	if len(result1) != 0:
		result1.sort() #对列表进行排序
		print encodeString("以下文件在：") + parame_a + encodeString("和") + parame_b + encodeString("中有差异!")
		for m in result1:
 			print m
	if len(result2) != 0:
		result2.sort() #对列表进行排序
		print encodeString("以下文件在：") + parame_b + encodeString("中缺失了!")
		for n in result2:
			print n

def saveIntoDic(file_list):
	dic = {}
	for i in file_list:
		i = i.replace('\\','/')  #这里将路径中的\替换为/，方便处理。。\实在是问题太多
		file_md5 = getFileMd5(i)
		dic[i] = file_md5
	return dic

def outPutCheckResult(path_a,path_b,parame_a,parame_b):
	#这里开始检查资源
	pc_temp_str = ""
	other_temp_str = ""
	#将需要检查的文件夹，组合成dir /s /b  所需的文件加参数 
	for i in check_diff_sync_path:
		pc_temp_str = pc_temp_str + path_a + "\\res\\"  + i + " "
		other_temp_str = other_temp_str + path_b + "\\res\\"  + i + " "

	#将组合后的参数，带入getFileList，获得所有文件夹内文件的列表
	pc_file_list = getFileList(pc_temp_str)[0]
	orther_file_list = getFileList(other_temp_str)[0]

	#通过文件列表，获得文件MD5的字典
	pc_dic = saveIntoDic(pc_file_list)
	orther_dic = saveIntoDic(orther_file_list)

	#使用对比方法，对比pc和android目录中的文件差异
	print encodeString("----------------------------------------检查结果------------------------------------------------")
	compareDic(pc_dic,orther_dic,parame_a,parame_b)
	print encodeString("\n------------------------------------------------------------------------------------------------\n")
	compareDic(orther_dic,pc_dic,parame_b,parame_a)	
	print encodeString("------------------------------------------------------------------------------------------------")
#以上为新增方法

#以下是常用参数
config = openFile(r"config.txt")#读取配置文件
config = eval(config) #将配置从str转换为dict
#print config[contury]['pc_diff_path']
pc_diff_path = config[contury]['pc_diff_path']
android_diff_path = config[contury]['android_diff_path']
ios_diff_path = config[contury]['ios_diff_path']
base_target_path = config[contury]['base_target_path']

pc_target_path = base_target_path + "\pc\\v0.0.0.1" #用作全局变量

while True:
	print "-"*80
	case = raw_input(encodeString('''请输入操作编号：
	1、更新pc并复制diff到资源目录
	2、更新android并复制diff到资源目录
	3、更新ios并复制diff到资源目录
	4、查看最近5条diff/pc的svn log
	5、将pc资源中的text配置替换为空（用于查看文本id）
'''))

	if case == "1":
		print "-"*80
		exclude_folder = exclude()  
		#pc_target_path = base_target_path + "\pc\\v0.0.0.1"
		updateSvn(pc_diff_path)

		start_time = int (time.time())#记录开始时间
		copyFileToTarget(getFileList(pc_diff_path),pc_diff_path,pc_target_path)
		end_time = int (time.time())#记录结束时间
		print encodeString("耗时：") + str(end_time - start_time) + "s"

	elif case == "2":
		print "-"*80
		exclude_folder = exclude()  
		updateSvn(android_diff_path)
		updateSvn(pc_diff_path)

		#这里开始检查资源
		outPutCheckResult(pc_diff_path,android_diff_path,"/pc/","/android/")#如果pc和安卓的版本号路径不同，则需要带上版本号一起替换

		#检查结束后，开始覆盖资源
		android_version = raw_input(encodeString("请输入要覆盖的android版本号："))
		android_target_path = base_target_path + "\\android\\" + android_version
		#print android_target_path

		start_time = int (time.time())
		copyFileToTarget(getFileList(android_diff_path),android_diff_path,android_target_path)
		end_time = int (time.time())
		print encodeString("耗时：") + str(end_time - start_time) + "s"

	elif case == "3":
		print "-"*80
		exclude_folder = exclude()  
		updateSvn(ios_diff_path)
		updateSvn(pc_diff_path)

		#这里开始检查资源
		outPutCheckResult(pc_diff_path,ios_diff_path,"/pc/","/ios/")#如果pc和安卓的版本号路径不同，则需要带上版本号一起替换

		#检查结束后，开始覆盖资源
		ios_version = raw_input(encodeString("请输入要覆盖的ios版本号："))
		ios_target_path = base_target_path + "\\ios\\" + ios_version
		#print ios_target_path

		start_time = int (time.time())
		copyFileToTarget(getFileList(ios_diff_path),ios_diff_path,ios_target_path)
		end_time = int (time.time())
		print encodeString("耗时：") + str(end_time - start_time) + "s"

	elif case == "4":
		svnLog(pc_diff_path)

	elif case == "5":
		copyFile(r"textecont.bytes",pc_target_path+r"\res\exlfile\textecont.bytes")	
		print encodeString("空的text文件覆盖成功！")

	else :
		print "-"*80
		print "I do not know!"