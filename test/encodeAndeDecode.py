import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#直接定义为2个方法，方便调用
def encodeString(string):
    return string.encode("gbk")

#直接定义为2个方法，方便调用
def decodeString(string):
    return unicode(string, encoding='utf-8')

string2 = "你大爷的。。。。aaaaa"
print string2
print encodeString(string2)
print decodeString(string2)
