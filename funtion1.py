# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 17:39:21 2018

@author: Aparajit Koshal
"""
##Diagonal Difference for a Matrix
# 11 2  4
# 4  5  6
# 10 8 -12
#For eg
#d1 will be
#11
#   5
#     -12
#d2 will be
#4
#  5 
#    10

import sys
def diagonalDifference(a):
    # Complete this function
	sum1=0
	sum2=0
	ran=len(a)
	for i in range(ran):
		sum1=sum1+int(a[i][i])
		sum2=sum2+int(a[i][ran-1-i])
	return abs(sum1-sum2)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_temp = input().strip().split(' ')
        a.append(a_temp)
    result = diagonalDifference(a)
    print (result)
len(a)
