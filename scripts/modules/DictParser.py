# -*- coding: utf-8 -*- 
from modules.RWFile import *

class DictParser:
	def __init__(self):
		self.err = False
		self.err_desc = ''

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n  Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc + "\n"

	def parse(self, work_folder, dict_name):
		dict_file = RWFile(work_folder, dict_name, 'read_binary', '')
		if (dict_file.err):
			self.rise_err(sys._getframe().f_code.co_name, dict_file.err_desc)
		else :
			while not dict_file.EOF:
				line = dict_file.read_line()
				print(line)
		
		dict_file.close_file()