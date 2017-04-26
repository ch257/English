# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.TemplateClass import *
from modules.RWFile import *

class MainProgram:
	def __init__(self):
		self.err = False
		self.err_desc = ""
		cfg = {}
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n  Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def read_ini(self, ini_file):
		cfg = {}
		config = configparser.ConfigParser()
		config.read(ini_file)
		for section in config.sections():
			cfg[section] = {}
			for key in config[section]:
				cfg[section][key] = config[section][key]
		return cfg

	def read_cfg(self, arguments):
		if len(arguments) < 2:
			self.rise_err(sys._getframe().f_code.co_name, "ini file name is not delivered")
		else:
			ini_file = RWFile('', arguments[1], 'read_binary', '')
			if ini_file.err:
				self.rise_err(sys._getframe().f_code.co_name, ini_file.err_desc)
			ini_file.close_file()

	def main(self, arguments):
		self.read_cfg(arguments)
		if not self.err:
			self.cfg = self.read_ini(arguments[1])
			# --------- write your code here ---------
			print(self.cfg) # print config
				
			template = TemplateClass() # using TemplateClass
			template.template_method() # using template_method from TemplateClass
			if (template.err):
				self.rise_err(sys._getframe().f_code.co_name, template.err_desc)
			# ---------------------------------------------
		
		if self.err:
			print(self.err_desc)
		else:
			print("OK")

main_program = MainProgram()
main_program.main(sys.argv)
if main_program.err:
	print(main_program.err_desc)
