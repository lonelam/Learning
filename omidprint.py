# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:06:39 2016

@author: Lai
"""

'处理不是＃开头的行'
import os

def writeln(openfile):
	for lines in openfile:
		if lines.startswith('#'):
			pass
		else:
			print lines
def write2(mixedfile):
	for lines in mixedfile:
		hashpos = lines.find('#')
		if hashpos!=-1:
			print lines[:hashpos]
		else:
			print lines
def writepages(pagebook):
	i = 0
	for lines in pagebook:
		i += 1
		if i == 25 :
			os.system('pause')
		print lines
flist = os.listdir('C:\Codes\Learning')
os.chdir('C:\Codes\Learning')
for fname in flist:
	status = raw_input('press enter or input"exit" here:' )
	if (status == 'exit'):
		break
	try:
		fin = open(fname)
		writepages(fin)
		fin.close()
	except IOError, e:
		print 'could not open file:'+fname,e
	
print '***DONE!'
