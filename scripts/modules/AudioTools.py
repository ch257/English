# -*- coding: utf-8 -*- 
import os
import sys
from modules.Tools import *

class AudioTools:
	def __init__(self):
		self.err = False
		self.err_desc = ''
		self.tools = Tools()

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n	Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc
		
	def cut_sample(self, cfg):
		# cmd = cmd + \
				  # path['output'] + "make_video\\tmp\\" + subfolder + "audio\\" + \
				  # file_number + ".mp3 "
		# os.system(cmd)
		print(audio_file_name, start_time, end_time)
		