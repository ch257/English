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
			excluded_symbols = (chr(32), '\n', '\t', '?', '!', '.', ',', '"')
			text_file = RWFile(work_folder, text_file_name, 'read', 'utf-8')
			word = ''
			words = []
			words_satarted = False
			while not text_file.err:
				smb = text_file.read_symbols(1)
				if smb:
					if smb in excluded_symbols:
						if words_satarted:
							words.append(word.lower())
							word = ''
							words_satarted = False
					else:
						if words_satarted:
							word += smb
						else:
							word += smb
							words_satarted = True
					
				else:
					break
			
			text_file.close_file()

			print(words)
			
			if text_file.err:
				self.rise_err(sys._getframe().f_code.co_name, text_file.err_desc)