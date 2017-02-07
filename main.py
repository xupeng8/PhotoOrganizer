#!/usr/bin/env python
#! -*- coding: utf-8 -*-

#
# Copyright @ Eric Xu 2017-02-02
# To orgnize photos by creating directory with name of date
# and move corresponding files to it 
#

import os
import re
import shutil

rootdir = "./"

def get_files():
	files = []
	li = os.listdir(rootdir)
	for f in li:
		if os.path.isfile(f) and (f[0] != '.'):
			files.append(f)
	return files

if __name__ == '__main__':
	files = get_files()
	#print files
	for f in files:
		pattern = re.compile(r'.*(201\d{5}).*')
		match = pattern.match(f)
		if match:
			dirname = match.groups()[0]
			fulldir = os.path.join(rootdir, dirname)
			print fulldir
			if not (os.path.isdir(fulldir) and os.path.exists(fulldir)):
				os.mkdir(fulldir)
			shutil.move(os.path.join(rootdir, f), fulldir)


