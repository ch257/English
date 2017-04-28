# -*- coding: utf-8 -*- 
from modules.RWFile import *

class PhraseManager:
	def __init__(self):
		self.err = False
		self.err_desc = ''

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def format_number(self, zeros, nmbr):
		str_nmbr = str(nmbr);
		return zeros[0:(len(zeros) - len(str_nmbr))] + str_nmbr

	def find_phrase(self, work_folder, text_file_name):
		if not self.err:
			text_file = RWFile(work_folder, text_file_name, 'read', 'utf-8')
			while not text_file.err:
				smbs = text_file.read_symbols(10)
				if smbs:
					print(smbs)
				else:
					break
			
			text_file.close_file()

			if text_file.err:
				self.rise_err(sys._getframe().f_code.co_name, text_file.err_desc)