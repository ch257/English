# -*- coding: utf-8 -*- 
import sys
from modules.FS import *

class MainProgram:
	def __init__(self, sys_argv):
		self.err = False
		self.err_desc = ""
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def check_file_exists(self, file_path):
		fs = FS()
		return fs.file_exists(file_path)
	
	def check_folder_exists(self, folder_path):
		fs = FS()
		return fs.folder_exists(folder_path)
	
	def main(self):
		folder_path = 'work'
		file_path = '.gitignore'
		# print(self.check_file_exists(file_path))
		print(self.check_folder_exists(file_path))
		
		
		
main_program = MainProgram(sys.argv)
main_program.main()
if main_program.err:
	print(main_program.err_desc)
