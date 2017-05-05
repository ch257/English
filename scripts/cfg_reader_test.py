# -*- coding: utf-8 -*- 

from modules.CfgReader import *

def main(sys_argv):
	cfg_reader = CfgReader(sys_argv)
	
	print(cfg_reader.get_parameter('file_ames', 'text_file_name'))

	if cfg_reader.err:
		print(cfg_reader.err_desc)
main(sys.argv)