# -*- coding: utf-8 -*- 
import os
import sys

class Tools:
	def __init__(self):
		self.err = False
		self.err_desc = ''

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc
		
	def file_exists(self, file_folder, file_name):
		if os.path.isfile(file_folder + file_name):
			return  True
		else:
			self.rise_err(sys._getframe().f_code.co_name, "no such file `" + file_folder + file_name + "`")
			return False

	def delete_file(self, file_folder, file_name):
		if os.path.isfile(file_folder + file_name):
			os.remove(file_folder + file_name)
			
	def format_number(self, zeros, nmbr):
		str_nmbr = str(nmbr);
		return zeros[0:(len(zeros) - len(str_nmbr))] + str_nmbr
