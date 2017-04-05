# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.RWFile import *

class run:
	def __init__(self):
		self.err = False
		self.err_desc = ""
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n  Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc + "\n"

	def read_ini(self, ini_file):
		config = configparser.ConfigParser()
		config.read(ini_file)
		# print(config.sections())
		# for section in config.sections():
			# for key in config[section]:
				# print(config[section][key])
		section_name = 'path'
		if config.has_section(section_name):
			print(config.items(section_name))
		else:
			print("No such section in ini file")

	def main(self, arguments):
		if len(arguments) > 1:
			self.read_ini(arguments[1])
		else:
			self.rise_err(sys._getframe().f_code.co_name, "ini file not present")

r = run()
r.main(sys.argv)
if r.err:
	print(r.err_desc)
