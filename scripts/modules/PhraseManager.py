# -*- coding: utf-8 -*- 

from modules.RWFile import *
from modules.TextTools import *
from modules.AudioTools import *

class PhraseManager:
	def __init__(self, cfg_reader):
		self.err = False
		self.err_desc = ''
		
		self.cfg_reader = cfg_reader
		self.text_words = {}
		self.text_labels = {}
		self.text_source_words = {}
		self.time_labels = {}
		
		self.audio_tools = AudioTools(cfg_reader)
		if self.audio_tools.err:
			self.rise_err(sys._getframe().f_code.co_name, self.audio_tools.err_desc)
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

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
		start_time = self.time_labels[phrase_start]
		end_time = self.time_labels[phrase_end]
		self.audio_tools.cut_sample(start_time, end_time, self.cfg_reader)
		self.audio_tools.add_silence('before', self.cfg_reader)
		
	
	def get_text_data(self):
		text_tools = TextTools()
		text_tools.find_text_words(self.cfg_reader)
		text_tools.find_time_labels(self.cfg_reader)
		
		self.text_words = text_tools.text_words
		self.text_source_words = text_tools.text_source_words
		self.time_labels = text_tools.time_labels
		
		if text_tools.err:
			self.rise_err(sys._getframe().f_code.co_name, text_tools.err_desc)
	
	def find_phrase(self):
		self.get_text_data()
		if not self.err:
			# self.text_words = {0:'', 1:'', 2:'', 3:'', 4:'', 5:''}
			words_cnt = 0
			phrase_start = words_cnt
			phrase_end = phrase_start + 1
			phrase = self.text_words[words_cnt]
			
			while not self.err:
				print(self.glue_phrase(phrase_start, phrase_end))
				# self.create_media(phrase_start, phrase_end)
				manage_seq = input()
				action, offset = self.determine_action(manage_seq)
				
				if action == '+':
					if phrase_end + offset < len(self.text_words):
						phrase_end += offset
					else:
						phrase_end = len(self.text_words) - 1
				
				elif action == '-':
					if phrase_end - offset > 2:
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
					if phrase_start - offset > 0:
						phrase_start -= offset
						phrase_end -= offset
					else:
						phrase_end = - phrase_start + phrase_end
						phrase_start = 0
				
				elif action == 'm':
					self.create_media(phrase_start, phrase_end)
					print('--------------- create_media end ----------------\n')
					
				elif action == 'q':
					break

			
			
			
			
			
			
			
			
			
			
			
			
			