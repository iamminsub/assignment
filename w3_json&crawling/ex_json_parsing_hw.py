#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")
#data는 여러가지 dic을 list로 가지고있음
#totaldata는 data와 code를 dic으로 가지고 있음
totaldata = json.load(htmltext)
#data라는 dic의 요소들가져오기
element = totaldata["data"] 
print element
print "MEM_NUM \tAge \t\t Job \t \t  MEM_CODE \t\t  etc" #목록표 출력
for item in element:				
	if item["job"] == "Programmer": #프로그래머는 Master
		item["etc"] = "Master"
		if item["age"] >= 50:		#50이상 프로그래머는 Master Old
			item["etc"] = "Master Old"
	elif item["age"] >= 50:			#프로그래머가 아닌 50이상은 Old
		item["etc"] = "Old"
	else:							#나머지는 공백
		item["etc"] = " "
	print "%4s \t %6s \t %11s \t %10s \t %s"%(item["MEM_NUM"],item["age"],item["job"],item["MEM_CODE"],item["etc"])
