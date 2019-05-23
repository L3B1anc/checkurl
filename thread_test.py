# encoding=utf-8
"""
author:L3b1anc
date:2019.5.23
description:多线程扫描测试
"""
from threading import Thread
import checkurl
import time

class test(Thread):
	"""docstring for test"""
	def __init__(self,name):
		super(test, self).__init__()
		self.name=name
	def run(self):
		checkurl.geturl()
if __name__ == '__main__':
	t=test("1")
	t.start()
	print('test1')

		
		
