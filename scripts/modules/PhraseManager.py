# -*- coding: utf-8 -*- 
from modules.RWFile import *
from modules.TextTools import *
from modules.AudioTools import *

class PhraseManager:
	def __init__(self, cfg):
		self.err = False
		self.err_desc = ''
		
		self.cfg = cfg
		self.text_words = {}
		self.text_labels = {}
		self.text_source_words = {}
		self.time_labels = {}
		self.text_tools = TextTools()
		self.audio_tools = AudioTools()

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
		print(self.glue_phrase(phrase_start, phrase_end))
		start_time = self.time_labels[phrase_start]
		end_time = self.time_labels[phrase_end]
		
		# self.audio_tools.cut_sample(work_folder, audio_file_name, output_folder, start_time, end_time)
	
	def find_phrase(self):
		if not self.err:
			self.text_tools.find_text_words(self.cfg)
			self.text_tools.find_time_labels(self.cfg)
			
			self.text_words = self.text_tools.text_words
			self.text_source_words = self.text_tools.text_source_words
			self.time_labels = self.text_tools.time_labels
			
			# self.text_words = {0:'', 1:'', 2:'', 3:'', 4:'', 5:''}
			words_cnt = 0
			phrase_start = words_cnt
			phrase_end = phrase_start + 1
			phrase = self.text_words[words_cnt]
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
					if phrase_start - offset > 0:
						phrase_start -= offset
						phrase_end -= offset
					else:
						phrase_end = - phrase_start + phrase_end
						phrase_start = 0
				
				elif action == 'q':
					break

			
			
			
			
			
			
			
			
			
			
			
			
			
			