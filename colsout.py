# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:05:32 2016

@author: Lai
"""

def colsout(container,n):
	index=0
	rlist = [[] for i in range(n)]
	for x in container:
		if index >= n :
			index = 0
		rlist[index].append(x)
		index += 1
	return rlist
	
def listprint(alist):
	n = len(alist)
	rows = len(alist[0])
	for i in range(rows):
		for j in range(n):
			if i < len(alist[j]):
				print alist [j][i],
		print 
		
def main():
	rawstr = raw_input('Your string here please:\n')
	n = raw_input('How many cols do you want?  ')
	while(not n.isdigit()):
		n = raw_input('Please enter the number of cols you want: ')
	n = int(n);
	listprint(colsout(rawstr,n))

if __name__ == '__main__':
	main()
	