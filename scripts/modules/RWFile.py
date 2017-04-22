# -*- coding: utf-8 -*- 
import os
import sys
import shutil

class RWFile:
	def __init__(self, file_folder, file_name, open_mode, coding):
		self.handler = None
		self.EOF = False
		self.err = False
		self.err_desc = ''
		self.file_folder = file_folder
		self.file_name = file_name
		self.open_mode = open_mode
		self.file = file_folder + file_name
		self.folder_list = []
		self.try_open(coding)
		
	def try_open(self, coding):
		try:
			if self.open_mode == "read_binary":
				self.handler = open(self.file, 'rb')
			elif self.open_mode == "read":
				self.handler = open(self.file, 'r', encoding = coding)
			elif self.open_mode == "write_binary":
				self.handler = open(self.file, 'wb', encoding = coding)
			elif self.open_mode == "write":
				self.handler = open(self.file, 'w', encoding = coding)
			elif self.open_mode == "append":
				self.handler = open(self.file, 'a', encoding = coding)
			elif self.open_mode == "in_folder":
				self.folder_list = os.listdir(self.file_folder)
			elif self.open_mode == "create_subfolder":
				self.create_subfolder()
			else:
				self.rise_err(sys._getframe().f_code.co_name, "Unknown open mode:'" + self.open_mode + "'")
		except FileNotFoundError:
			if self.open_mode == "in_folder":
				self.rise_err(sys._getframe().f_code.co_name, "No such folder:'" + self.file_folder + "'")
			else:
				self.rise_err(sys._getframe().f_code.co_name, "No such file:'" + self.file + "'")
		except NotADirectoryError:
			self.rise_err(sys._getframe().f_code.co_name, "'" + self.file + " isn`t the directory.'")
		except PermissionError:
			if self.open_mode == "in_folder":
				self.rise_err(sys._getframe().f_code.co_name, "Not enough permissions to read folder:'" + self.file_folder + "'")
			else:
				if os.path.isdir(self.file):
					self.rise_err(sys._getframe().f_code.co_name, "It`s the folder:'" + self.file + "'")
				else:	
					self.rise_err(sys._getframe().f_code.co_name, "Not enough permissions to " + self.open_mode + " file:'" + self.file + "'")

	def read_line(self):
		line = self.handler.readline()
		if line:
			return line
		else:
			self.EOF = True

	def write_line(self, line):
		self.handler.write(line)

	def close_file(self):
		if not self.err:
			self.handler.close()
			self.handler = None

	def delete_files_in_folder(self):
		for file in self.folder_list:
			if not os.path.isdir(self.file_folder + file):
				try:
					os.remove(self.file_folder + file)
				except FileNotFoundError:
					self.rise_err(sys._getframe().f_code.co_name, "Try to remove non existent file:'" + self.file_folder + file + "'")
					break
				except PermissionError:
					self.rise_err(sys._getframe().f_code.co_name, "Not enough permissions to remove file:'" + self.file_folder + file + "'")
					break

	def delete_subfolders_in_folder(self):
		for file in self.folder_list:
			if os.path.isdir(self.file_folder + file):	
				try:
					shutil.rmtree(self.file_folder + file)
				except FileNotFoundError:
					self.rise_err(sys._getframe().f_code.co_name, "Try to remove non existent subfolder:'" + self.file_folder + file + "'")
					break
				except PermissionError:
					self.rise_err(sys._getframe().f_code.co_name, "Not enough permissions to remove subfolder:'" + self.file_folder + file + "'")
					break

	def clear_folder(self):
		for file in self.folder_list:
			try:
				if os.path.isdir(self.file_folder + file):
					shutil.rmtree(self.file_folder + file)
				else:	
					os.remove(self.file_folder + file)
			except FileNotFoundError:
				self.rise_err(sys._getframe().f_code.co_name, "Try to remove non existent file or folder:'" + self.file_folder + file + "'")
				break
			except PermissionError:
				self.rise_err(sys._getframe().f_code.co_name, "Not enough permissions to remove file or folder:'" + self.file_folder + file + "'")
				break

	def create_subfolder(self):
		if os.path.isdir(self.file_folder):
			subfolders_list = []
			cnt = 0
			subfolder_path_length = len(self.file_name)
			subfolder_name = ""
			while cnt < subfolder_path_length:
				if self.file_name[cnt] == "\\" or	self.file_name[cnt] == "/":
					subfolders_list.append(subfolder_name)
					subfolder_name = ""
				else:
					subfolder_name = subfolder_name + self.file_name[cnt]
				cnt = cnt + 1
			if subfolder_name:
				subfolders_list.append(subfolder_name)

			parent_folder_path = self.file_folder
			for subfolder_name in subfolders_list:
				if not os.path.isdir(parent_folder_path + subfolder_name):
					os.mkdir(parent_folder_path + subfolder_name)
				parent_folder_path = parent_folder_path + subfolder_name + "\\"
		else:
			self.rise_err(sys._getframe().f_code.co_name, "No such folder:'" + self.file_folder + "'")

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n	Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc + "\n"
