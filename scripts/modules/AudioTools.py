# -*- coding: utf-8 -*- 
from os import rename
import sys
import subprocess
from modules.Tools import *

class AudioTools:
	def __init__(self, cfg_reader):
		self.err = False
		self.err_desc = ''
		self.check_files_exist(cfg_reader)
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc
		
	def check_files_exist(self, cfg_reader):
		mp3splt_folder = cfg_reader.get_parameter('path', 'mp3splt_folder')
		mp3_file_folder = cfg_reader.get_parameter('path', 'mp3_file_folder')
		mp3wrap_folder = cfg_reader.get_parameter('path', 'mp3wrap_folder')
		
		mp3splt_file = cfg_reader.get_parameter('file_names', 'mp3splt_file')
		mp3_file_name = cfg_reader.get_parameter('file_names', 'mp3_file_name')
		mp3wrap_file = cfg_reader.get_parameter('file_names', 'mp3wrap_file')
		
		if not cfg_reader.err:
			tools = Tools()
			if not tools.file_exists(mp3_file_folder, mp3_file_name):
				self.rise_err(sys._getframe().f_code.co_name, tools.err_desc)
			elif not tools.file_exists(mp3splt_folder, mp3splt_file):
				self.rise_err(sys._getframe().f_code.co_name, tools.err_desc)
			elif not tools.file_exists(mp3wrap_folder, mp3wrap_file):
				self.rise_err(sys._getframe().f_code.co_name, tools.err_desc)
		else :
			self.rise_err(sys._getframe().f_code.co_name, cfg_reader.err_desc)
	
	def auda_to_mp3splt_convert_time(self, auda_time):
		splited_auda_time = auda_time.split('.')
		seconds = splited_auda_time[0]
		hundredths = splited_auda_time[1]
		minuts = int(seconds) // 60
		seconds = int(seconds) - minuts * 60
		return str(minuts) + '.' + str(seconds) + '.' + hundredths
	
	def add_silence(self, order, cfg_reader):
		silences_folder = cfg_reader.get_parameter('path', 'silences_folder')
		mp3wrap_folder = cfg_reader.get_parameter('path', 'mp3wrap_folder')
		output_folder = cfg_reader.get_parameter('path', 'output_folder')
		
		silence_for_sample_file = cfg_reader.get_parameter('file_names', 'silence_for_sample_file')
		mp3wrap_file = cfg_reader.get_parameter('file_names', 'mp3wrap_file')
		mp3_output_sample_file_name = cfg_reader.get_parameter('file_names', 'mp3_output_sample_file_name')
		
		tools = Tools()
		tools.delete_file(output_folder, mp3_output_sample_file_name + '_MP3WRAP.mp3')
		tools.delete_file(output_folder, mp3_output_sample_file_name + '_s.mp3')
		
		cmd = 	mp3wrap_folder + mp3wrap_file + chr(32) + \
				output_folder + mp3_output_sample_file_name + chr(32) + \
				output_folder + mp3_output_sample_file_name + '.mp3' + chr(32) + \
				silences_folder + silence_for_sample_file
				
		cmd = cmd.replace('/', '\\')
		print(cmd)
		os.system(cmd)
		rename(output_folder + mp3_output_sample_file_name + '_MP3WRAP.mp3', output_folder + mp3_output_sample_file_name + '_s.mp3')
		
	def cut_sample(self, start_time, end_time, cfg_reader):
		mp3splt_folder = cfg_reader.get_parameter('path', 'mp3splt_folder')
		mp3_file_folder = cfg_reader.get_parameter('path', 'mp3_file_folder')
		mp3_output_sample_folder = cfg_reader.get_parameter('path', 'mp3_output_sample_folder')
		
		mp3splt_file = cfg_reader.get_parameter('file_names', 'mp3splt_file')
		mp3_file_name = cfg_reader.get_parameter('file_names', 'mp3_file_name')
		mp3_output_sample_file_name = cfg_reader.get_parameter('file_names', 'mp3_output_sample_file_name')
		
		# print(start_time, end_time)
		cmd = 	mp3splt_folder + mp3splt_file + chr(32) + \
				mp3_file_folder + mp3_file_name  + chr(32) + \
				self.auda_to_mp3splt_convert_time(start_time) + chr(32) + self.auda_to_mp3splt_convert_time(end_time) + chr(32) + \
				'-n' + chr(32) + \
				'-o' + chr(32) + mp3_output_sample_folder + mp3_output_sample_file_name
		cmd = cmd.replace('/', '\\')
		print(cmd)
		os.system(cmd)
		
	def play_mp3(self, cfg_reader):
		mp3player_folder = cfg_reader.get_parameter('path', 'mp3player_folder')
		mp3_file_folder = cfg_reader.get_parameter('path', 'output_folder')
		
		mp3player_file = cfg_reader.get_parameter('file_names', 'mp3player_file')
		mp3_file_name = cfg_reader.get_parameter('file_names', 'mp3_output_sample_file_name') + '.mp3'
		
		cmd = 	mp3player_folder + mp3player_file + chr(32) + \
				mp3_file_folder + mp3_file_name
		cmd = cmd.replace('/', '\\')
		print(cmd)
		subprocess.Popen(cmd, shell = False)
	
	def save_sample(self, f_name_number, cfg_reader):
		mp3_file_folder = cfg_reader.get_parameter('path', 'output_folder')
		
		mp3_file_name = cfg_reader.get_parameter('file_names', 'mp3_output_sample_file_name')
		
		tools = Tools()
		f_name_suffix = tools.format_number('0000', f_name_number)
		tools.delete_file(mp3_file_folder, f_name_suffix + '.mp3')
		rename(mp3_file_folder + mp3_file_name + '_s.mp3', mp3_file_folder + f_name_suffix + '.mp3')
		