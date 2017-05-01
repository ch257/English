# -*- coding: utf-8 -*- 
import os
import sys

class Tools:
	def __init__(self):
		self.err = False
		self.err_desc = ''

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n	Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc
		
	def CheckFileExists(self, file_folder, file_name):
		if os.path.isfile(file_folder + file_name):
			return  True
		else:
			return False
