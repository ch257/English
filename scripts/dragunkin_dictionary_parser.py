# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.DictParser import *
from modules.RWFile import *

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
			dict_parser = DictParser()
			work_folder = self.cfg['path']['work_folder']
			dict_name = self.cfg['params']['dict_name']
			output_folder = self.cfg['path']['output_folder']
			double_pages_folder = self.cfg ['path']['double_pages_folder']
			single_pages_folder = self.cfg ['path']['single_pages_folder']

			# dict_parser.split_into_double_pages(work_folder, dict_name, double_pages_folder)
			dict_parser.find_columns_in_double_pages(double_pages_folder)
			dict_parser.split_into_single_pages(double_pages_folder, single_pages_folder)


			if dict_parser.err:
				self.rise_err(sys._getframe().f_code.co_name, dict_parser.err_desc)
			else:
				print("OK")

						

main_program = MainProgram()
main_program.main(sys.argv)
if main_program.err:
	print(main_program.err_desc)
