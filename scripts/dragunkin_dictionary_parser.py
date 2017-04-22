# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.DictParser import *

class MainProgram:
	def __init__(self):
		self.err = False
		self.err_desc = ""
		cfg = {}
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def read_ini(self, ini_file):
		cfg = {}
		config = configparser.ConfigParser()
		config.read(ini_file)
		for section in config.sections():
			cfg[section] = {}
			for key in config[section]:
				cfg[section][key] = config[section][key]
		return cfg

	def main(self, arguments):
		if len(arguments) > 1:
			self.cfg = self.read_ini(arguments[1])
			# --------- write your code here ---------
			dict_parser = DictParser()
			work_folder = self.cfg['path']['work_folder']
			dict_name = self.cfg['params']['dict_name']
			output_folder = self.cfg['path']['output_folder']
			double_pages_folder = self.cfg ['path']['double_pages_folder']
			single_pages_folder = self.cfg ['path']['single_pages_folder']

			dict_parser.split_into_double_pages(work_folder, dict_name, double_pages_folder)
			if (dict_parser.err):
				self.rise_err(sys._getframe().f_code.co_name, dict_parser.err_desc)
			else:
				print("01 - split_into_double_pages: OK")
				dict_parser.find_columns_in_double_pages(double_pages_folder)
				if (dict_parser.err):
					self.rise_err(sys._getframe().f_code.co_name, dict_parser.err_desc)
				else:
					print("02 - find_columns_in_double_pages: OK")
					dict_parser.split_into_single_pages(double_pages_folder, single_pages_folder)
					if (dict_parser.err):
						self.rise_err(sys._getframe().f_code.co_name, dict_parser.err_desc)
					else:
						print("03 - split_into_single_pages: OK")
						pass
			# ---------------------------------------------
			
		else:
			self.rise_err(sys._getframe().f_code.co_name, "ini file not present")

main_program = MainProgram()
main_program.main(sys.argv)
if main_program.err:
	print(main_program.err_desc)
