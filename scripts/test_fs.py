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

	def main(self):
		fs = FS()
		fs.test()
		
main_program = MainProgram(sys.argv)
main_program.main()
if main_program.err:
	print(main_program.err_desc)
