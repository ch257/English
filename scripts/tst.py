# -*- coding: utf-8 -*- 
import sys

class run:
	def __init__(self):
		self.err = False
		self.err_desc = ""
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n  Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc + "\n"

	def read_ini(self, ini_file):
		pass

	def main(self, arguments):
		if len(arguments) > 1:
			print(arguments)
		else:
			self.rise_err(sys._getframe().f_code.co_name, "ini file not present")

r = run()
r.main(sys.argv)
if r.err:
	print(r.err_desc)
