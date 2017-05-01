# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.PhraseManager import *
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
			phrase_manager = PhraseManager()	
			work_folder = self.cfg['path']['work_folder']
			output_folder = self.cfg['path']['output_folder']
			mp3splt_folder = self.cfg['path']['mp3splt_folder']
			text_file_name  = self.cfg['params']['text_file_name']
			time_labels_file_name = self.cfg['params']['time_labels_file_name']
			audio_file_name = self.cfg['params']['audio_file_name']
			# = self.cfg['params']['']
			phrase_manager.find_text_words(work_folder, text_file_name)
			phrase_manager.find_time_labels(work_folder, time_labels_file_name)
			
			# for words_cnt in phrase_manager.text_words:
				# print(phrase_manager.text_words[words_cnt], phrase_manager.text_labels[words_cnt], phrase_manager.time_labels.get(words_cnt), phrase_manager.text_source_words[words_cnt])
			
			phrase_manager.find_phrase(work_folder, audio_file_name, output_folder, mp3splt_folder)
			
			if (phrase_manager.err):
				self.rise_err(sys._getframe().f_code.co_name, phrase_manager.err_desc)
			# ---------------------------------------------
			print("OK")

main_program = MainProgram()
main_program.main(sys.argv)
if main_program.err:
	print(main_program.err_desc)
