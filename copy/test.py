#coding=utf-8
import os


exclude_folder = "\\\\fx\\\\|\\\\scene\\\\|\\\\actor\\\\|\\\\audio\\\\"


def copyFile():
    #os.popen("copy /y "+filePath+" "+dstPath)
    a = os.popen(r"copy /y C:\workspace\svn\v1.5.0_20181114_korean\diff\client\ios\res\lua\Config.txt C:\workspace\svn\v1.5.0_20181114_korean\client\AllRes\chs\fullRes\ioss\2222.txt")
    #print len(a.readlines())
    if a.readlines():
    	print "success"
    else:
    	print "error"



def exclude():
	a = raw_input("if paichu ? moren paichu/ 1 bu pai chu" + exclude_folder)
	if a :
		print "no"
		return "ssdfsd"
	else:
		print "exclude!"
		return exclude_folder

copyFile()

exclude_folder = exclude()
print exclude_folder
