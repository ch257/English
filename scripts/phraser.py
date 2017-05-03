# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.RWFile import *
from modules.TextTools import *

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

	def determine_action(self, manage_seq):
		offset = ''
		action = ''
		for smb in manage_seq:
			if ord(smb) > 47 and ord(smb)< 58:
				offset += smb
			else:
				action += smb
		if not offset:
			offset = '1'
		return action, int(offset)
		
	def glue_phrase(self, phrase_start, phrase_end):
		words_cnt = phrase_start
		phrase = ''
		while words_cnt < phrase_end:
			phrase += self.text_source_words[words_cnt]
			words_cnt += 1
		return phrase
	
	def create_media(self, phrase_start, phrase_end):
		# print(phrase_start, phrase_end)
		print(self.glue_phrase(phrase_start, phrase_end))
		start_time = self.time_labels[phrase_start]
		end_time = self.time_labels[phrase_end]
		
	def find_phrase(self):
		if not self.err:
			# self.text_words = {0:'', 1:'', 2:'', 3:'', 4:'', 5:''}
			words_cnt = 0
			phrase_start = words_cnt
			phrase_end = phrase_start + 1
			while True:
				self.create_media(phrase_start, phrase_end)
				
				manage_seq = input()
				action, offset = self.determine_action(manage_seq)
				
				if action == '+':
					if phrase_end + offset < len(self.text_words):
						phrase_end += offset
					else:
						phrase_end = len(self.text_words) - 1
				
				elif action == '-':
					if phrase_end - offset > 1:
						phrase_end -= offset
					else:
						phrase_end = 1
				
				elif action == '++':
					if phrase_end + offset < len(self.text_words):
						phrase_start += offset
						phrase_end += offset
					else:
						phrase_start = len(self.text_words) + phrase_start - phrase_end - 1
						phrase_end = len(self.text_words) - 1
					
				elif action == '--':
					if phrase_start - offset > 1:
						phrase_start -= offset
						phrase_end -= offset
					else:
						phrase_end = - phrase_start + phrase_end
						phrase_start = 0
				
				elif action == 'q':
					break
	
	def main(self, arguments):
		self.read_cfg(arguments)
		if not self.err:
			self.cfg = self.read_ini(arguments[1])
			# --------- write your code here ---------
			# = self.cfg['params']['']
			# = self.cfg['path']['']

			text_tools = TextTools()
			text_tools.find_text_words(self.cfg)
			text_tools.find_time_labels(self.cfg)
			self.text_words = text_tools.text_words
			self.text_source_words = text_tools.text_source_words
			self.time_labels = text_tools.time_labels
			self.find_phrase()
			
			# for words_cnt in text_tools.text_words:
				# print(text_tools.text_words[words_cnt], text_tools.text_labels[words_cnt], text_tools.time_labels.get(words_cnt), text_tools.text_source_words[words_cnt])
			
			if (text_tools.err):
				self.rise_err(sys._getframe().f_code.co_name, text_tools.err_desc)
			# ---------------------------------------------
			print("OK")

main_program = MainProgram()
main_program.main(sys.argv)
if main_program.err:
	print(main_program.err_desc)
