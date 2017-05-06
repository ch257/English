# -*- coding: utf-8 -*- 
import sys
from modules.CfgReader import *
from modules.PhraseManager import *

class MainProgram:
	def __init__(self, sys_argv):
		self.err = False
		self.err_desc = ""
		self.cfg_reader = CfgReader(sys_argv)
		if self.cfg_reader.err:
			self.rise_err(sys._getframe().f_code.co_name, cfg_reader.err_desc)
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def find_phrase(self):
		if not self.err:
			phrase_manger = PhraseManager(self.cfg_reader)
			phrase_manger.find_phrase()
			
			# for words_cnt in phrase_manger.text_words:
				# print(phrase_manger.text_words[words_cnt], phrase_manger.text_labels[words_cnt], phrase_manger.time_labels.get(words_cnt), phrase_manger.text_source_words[words_cnt])
			
			if (phrase_manger.err):
				self.rise_err(sys._getframe().f_code.co_name, phrase_manger.err_desc)
	
	def main(self):
		self.find_phrase()
		if not self.err:
			print("OK")

main_program = MainProgram(sys.argv)
main_program.main()
if main_program.err:
	print(main_program.err_desc)
