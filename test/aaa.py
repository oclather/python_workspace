#coding=utf-8

import sys
import random

reload(sys)
sys.setdefaultencoding('utf-8')

#@classmethod
def generate_id(cls, sex=0):
	"""
	随机生成身份证号，sex = 0表示女性，sex = 1表示男性
	"""
	# 随机生成一个区域码(6位数)
	area_info = random.randint(0, len(addr))
	id_number = str(addr[area_info][0])
	# 限定出生日期范围(8位数)
	start, end = "1960-01-01", "2000-12-30"
	days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
	birth_days = datetime.datetime.strftime(
	datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days)), "%Y%m%d"
	)
	id_number += str(birth_days)
	# 顺序码(2位数)
	id_number += str(random.randint(10, 99))
	# 性别码(1位数)
	id_number += str(random.randrange(sex, 10, step=2))
	# 校验码(1位数)
	return id_number + str(cls(id_number).get_check_digit())


print generate_id(622224,sex=0)