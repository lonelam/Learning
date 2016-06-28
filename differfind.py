# -*- coding: utf-8 -*-
"""
Created on Sun May 22 23:56:47 2016

Compare two files and decide if they are the same.

@author: Lai
"""
from itertools import izip
def differ(fa,fb):
	la = fa.readline()
	row = 0
	while (la):
		lb = fb.readline()
		row += 1
		col = 0
		if la != lb :
			if len(la)==len(lb):
				for a,b in izip(la,lb):
					if (a!=b):
						return (row,col)
					col += 1
			else:
				for a,b in izip(la,lb):
					if(a!=b):
						return (row,col)
					col+=1
				return (row,col)
		la = fa.readline()
	return None

def main():
	filea = open("C:\Codes\learnc\hd2.1.9.cpp")
	fileb = open("C:\Codes\learnc\hd2.1ano.cpp")
	print differ(filea,fileb)
	
if __name__ == '__main__':
	main()