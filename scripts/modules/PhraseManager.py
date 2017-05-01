# -*- coding: utf-8 -*- 
from modules.RWFile import *

class PhraseManager:
	def __init__(self):
		self.err = False
		self.err_desc = ''
		
		self.text_words = {}
		self.text_labels = {}
		self.time_labels = {}

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def format_number(self, zeros, nmbr):
		str_nmbr = str(nmbr);
		return zeros[0:(len(zeros) - len(str_nmbr))] + str_nmbr

	def find_text_words(self, work_folder, text_file_name):	
		if not self.err:
			excluded_symbols = (chr(32), '\n', '\t', '?', '!', '.', ',', '"', '-', ':', ';')
			text_file = RWFile(work_folder, text_file_name, 'read', 'utf-8')
			word = ''
			words_satarted = False
			symbols_cnt = 0
			words_cnt = 0
			while not text_file.err:
				smb = text_file.read_symbols(1)
				if smb:
					if smb in excluded_symbols:
						if words_satarted:
							self.text_words[words_cnt] = word.upper()
							self.text_labels[words_cnt] = symbols_cnt
							word = ''
							words_satarted = False
							words_cnt += 1
					else:
						if words_satarted:
							word += smb
						else:
							word += smb
							words_satarted = True
					
				else:
					break
				symbols_cnt += 1
				
			text_file.close_file()

			if text_file.err:
				self.rise_err(sys._getframe().f_code.co_name, text_file.err_desc)
	
	def find_time_labels(self, work_folder, time_labels_file_name):
		if not self.err:
			time_labels_file = RWFile(work_folder, time_labels_file_name, 'read', 'utf-8')
			words_cnt = 0
			while not time_labels_file.err:
				line = time_labels_file.read_line()
				if line:
					splitted_line = line.split(chr(32))
					time_label = float(splitted_line[0])
					word_label = splitted_line[1].strip('\n')
						
					not_found = True
					# if words_cnt == len(self.text_words):
						# words_cnt = 0
					while words_cnt < len(self.text_words) and not_found: 
						if word_label == 'SENT-END':
							break
						
						if word_label == self.text_words[words_cnt]:
							self.time_labels[words_cnt] = time_label
							not_found = False
						words_cnt += 1
				else:
					break
			time_labels_file.close_file()
			
		if time_labels_file.err:
				self.rise_err(sys._getframe().f_code.co_name, text_file.err_desc)
	
	def determine_action(self, manage_seq):
		offset = ''
		action = ''
		for smb in manage_seq:
			if ord(smb) > 47 and ord(smb)< 58:
				offset += smb
			else:
				action += smb
		return action, offset
		
	
	def find_phrase(self):
		if not self.err:
			self.text_words = {0:'', 1:'', 2:'', 3:'', 4:'', 5:''}
			words_cnt = 0
			phrase_start = words_cnt
			phrase_end = phrase_start + 1
			phrase = self.text_words[words_cnt]
			while True:
				print(phrase_start, phrase_end)
				manage_seq = input()
				action, offset = self.determine_action(manage_seq)
				
				if action == '+':
					int_offset = int(offset)
					if phrase_end + int_offset < len(self.text_words):
						phrase_end += int_offset
					else:
						phrase_end = len(self.text_words) - 1
				
				elif action == '-':
					int_offset = int(offset)
					if phrase_end - int_offset > 1:
						phrase_end -= int_offset
					else:
						phrase_end = 1
				
				elif action == '++':
					int_offset = int(offset)
					if phrase_end + int_offset < len(self.text_words):
						phrase_start += int_offset
						phrase_end += int_offset
					else:
						phrase_start = len(self.text_words) + phrase_start - phrase_end - 1
						phrase_end = len(self.text_words) - 1
					
				elif action == '--':
					int_offset = int(offset)
					if phrase_start - int_offset > 1:
						phrase_start -= int_offset
						phrase_end -= int_offset
					else:
						phrase_end = - phrase_start + phrase_end
						phrase_start = 0
				
				elif  manage_seq == 'q':
					break

			
			
			
			
			
			
			
			
			
			
			
			
			
			