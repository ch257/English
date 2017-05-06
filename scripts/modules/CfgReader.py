# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.RWFile import *

class CfgReader:
	def __init__(self, sys_argv):
		self.err = False
		self.err_desc = ''
		self.cfg = {}
		
		self.check_ini_file(sys_argv)
		self.get_cfg(sys_argv[1])

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc
		
	def check_ini_file(self, arguments):
		if len(arguments) < 2:
			self.rise_err(sys._getframe().f_code.co_name, "ini file name is not delivered")
		else:
			ini_file = RWFile('', arguments[1], 'read_binary', '')
			if ini_file.err:
				self.rise_err(sys._getframe().f_code.co_name, ini_file.err_desc)
			ini_file.close_file()

	def get_cfg(self, ini_file):
		if not self.err:
			config = configparser.ConfigParser()
			config.read(ini_file)
			for section in config.sections():
				self.cfg[section] = {}
				for key in config[section]:
					self.cfg[section][key] = config[section][key]
		return self.cfg
	
	def get_parameter(self, section, key):
		if not self.err:
			if self.cfg:
				ini_section = self.cfg.get(section)
				if ini_section:
					ini_key_value = ini_section.get(key)
					if ini_key_value:
						return ini_key_value
					else:
						self.rise_err(sys._getframe().f_code.co_name, "no such key `" + key + "` in section [" + section + "]")
				else:
					self.rise_err(sys._getframe().f_code.co_name, "no such section [" + section + "]")
			else:
				self.rise_err(sys._getframe().f_code.co_name, "config is empty")
			
