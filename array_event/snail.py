# -*- coding: utf-8 -*-
snail_array = []

for i in range(5):
	empty_array = []
	for j in range(5):
		empty_array.append(0)
	snail_array.append(empty_array)

for column in snail_array:
	for num in column:
		print "%2s" % num,
	print
# print init array
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0
 # 0  0  0  0  0

# change array like this
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9 

######## insert your algorithm here ########
a = 0
b = 0
c = 0
n = 1
for i in range(25):
	snail_array[a][b] = n
	n += 1
	if a == c and b < 4-c :	
		b += 1     		#0,1 0,2 0,3 0,4 
	elif a < 4-c and b == 4-c :
		a += 1    		#1,4 2,4 3,4 4,4
	elif a == 4-c and b > c:
		b -= 1   		#4,3 4,2 4,1 4,0
	elif a == 4-c and b == c:
		a -= 1
		c += 1    		#3,0
	elif c < a < 4 and b == c-1:
		a -= 1    		#2,0 1,0
		
"""
	elif a == 1 and -1 < b < 3:
		b += 1  		#1,1 1,2 1,3
	elif 0 < a < 3 and b == 3:
		a += 1			#2,3 3,3
	elif a == 3 and 1<b<4:
		b -= 1  		#3,2 3,1
	elif 2<a<4 and b == 1:
		a -= 1  		#2,1
	else:
		b += 1   		#2,2
"""

print 
for column in snail_array:
	for num in column:
		print "%2s" % num,
	print
# print result array
# 영어 주석 힘들다.