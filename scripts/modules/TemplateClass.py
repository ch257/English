# -*- coding: utf-8 -*- 
import os
import sys
import shutil

class TemplateClass:
	def __init__(self):
		self.err = False
		self.err_desc = ''

	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n	Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc

	def template_method(self):
		print('Hello!')
		