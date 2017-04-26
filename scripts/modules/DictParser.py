# -*- coding: utf-8 -*- 
from modules.RWFile import *

class DictParser:
	def __init__(self):
		self.err = False
		self.err_desc = ''

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def format_number(self, zeros, nmbr):
		str_nmbr = str(nmbr);
		return zeros[0:(len(zeros) - len(str_nmbr))] + str_nmbr

	def split_into_double_pages(self, work_folder, dict_name, double_pages_folder):
		if not self.err:	
			dict_file = RWFile(work_folder, dict_name, 'read_binary', '')
			double_pages_directory = RWFile(double_pages_folder, '', 'in_folder', '')
			double_pages_cnt = 0
			output_file = None
			double_pages_directory.clear_folder()
			while not dict_file.err:
				line = dict_file.read_line()
				if line:
					if (line[0] == 12):
						if output_file:
							output_file.close_file()
						output_file = RWFile(double_pages_folder, self.format_number("000", double_pages_cnt) + '.txt', 'write_binary', '')
						if output_file.err:
							break
						double_pages_cnt += 1
					output_file.write(line)
				else:
					if output_file:
						output_file.close_file()
					break
			dict_file.close_file()
			
			if dict_file.err:
				self.rise_err(sys._getframe().f_code.co_name, dict_file.err_desc)
			elif double_pages_directory.err:
				self.rise_err(sys._getframe().f_code.co_name, double_pages_directory.err_desc)
			elif output_file.err:
				self.rise_err(sys._getframe().f_code.co_name, output_file.err_desc)
			
		
	def find_columns_in_double_pages(self, double_pages_folder, double_pages_columns_folder):
		if not self.err:
			double_pages_directory = RWFile(double_pages_folder, '', 'in_folder', '')
			double_pages_columns_directory = RWFile(double_pages_columns_folder, '', 'in_folder', '')
			double_pages_file = None
			double_pages_columns_file = None
			
			double_pages_columns_directory.clear_folder()
			if not double_pages_directory.err and not double_pages_columns_directory.err:
				for double_pages_file_name in double_pages_directory.folder_list:
					double_pages_file = RWFile(double_pages_folder, double_pages_file_name, 'read_binary', '')
					double_pages_columns_file = RWFile(double_pages_columns_folder, double_pages_file_name[0:-4] + '_c.txt', 'write', 'utf-8')
					columns = {}
					while not double_pages_file.err or double_pages_columns_file.err:
						line = double_pages_file.read_line()
						if line:
							word_start = False
							symbol_cnt = 0
							for symbol_code in line:
								if not word_start and symbol_code not in (32, 10, 13, 9):
									word_start = True
									if columns.get(symbol_cnt):
										columns[symbol_cnt] += 1
									else:
										columns[symbol_cnt] = 1
								if word_start and symbol_code in (32, 10, 13, 9):
									word_start = False
								symbol_cnt += 1
						else:
							break
						# break #----------------------------! first line only
					else:
						break
					double_pages_file.close_file()
					if not double_pages_columns_file.err:
						columns_line = ''
						for column_key in columns:
							columns_line += str(column_key) + ':' + str(columns[column_key]) +'\t'
						double_pages_columns_file.write(columns_line + '\n')
						
					double_pages_columns_file.close_file()
					# break #----------------------------! first file only
			
			if double_pages_directory.err:
				self.rise_err(sys._getframe().f_code.co_name, double_pages_directory.err_desc)
			elif double_pages_columns_directory.err:
				self.rise_err(sys._getframe().f_code.co_name, double_pages_columns_directory.err_desc)
			elif double_pages_file and double_pages_file.err:
				self.rise_err(sys._getframe().f_code.co_name, double_pages_file.err_desc)
			elif double_pages_columns_file and double_pages_columns_file.err:
				self.rise_err(sys._getframe().f_code.co_name, double_pages_columns_file.err_desc)
				
	def split_into_single_pages(self, double_pages_folder, single_pages_folder):
		if not self.err:
			double_pages_directory = RWFile(double_pages_folder, '', 'in_folder', '')
			for double_pages_file_name in double_pages_directory.folder_list:
				# print(double_pages_file_name)
				pass

			if double_pages_directory.err:
				self.rise_err(sys._getframe().f_code.co_name, double_pages_directory.err_desc)
