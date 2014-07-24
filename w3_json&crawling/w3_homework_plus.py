#-*- coding: utf-8 -*-

import webbrowser
import urllib
from xml.etree.ElementTree import parse
from bs4 import BeautifulSoup

	# root태그 얻어오기
joins = 'http://rss.joins.com/joins_news_list.xml'
chosun = 'http://www.chosun.com/site/data/rss/rss.xml'
donga = 'http://rss.donga.com/total.xml'

def news(url):
	xml = urllib.urlopen(url)	# 중앙일보rss
	tree = parse(xml)		# xml 파싱하여 나뭇가지 구조 얻기
	root = tree.getroot()
	article = {}
	articlelist = []
	count = 1
	for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
		for child in parent.findall("item"):
			print count, child.findtext("title")
			article["tit"] = child.findtext("title")		#article 딕셔너리만들기
			article["lin"] = child.findtext("link")
			articlelist.append(article)						#list에 딕셔너리 넣기
			article = {}									#article 비우기(key값이 중복되기때문)
			count += 1
	print	
	num = input("보고싶은 뉴스번호를 입력하세요 : ")
	print
	for i in range(1,len(articlelist)+1):
		if num == i:
			html_source = urllib.urlopen(articlelist[i-1]["lin"])
			data = html_source.read()
			soup = BeautifulSoup(data)
			print soup.head.title.string
			print articlelist[i-1]["lin"]
			webbrowser.open(articlelist[i-1]["lin"])
			print 

while 1:
	print "1. 조선일보"
	print "2. 중앙일보"
	print "3. 동아일보"
	print
	news_num = input("(종료:0) 보고싶은 언론사를 입력하세요 : ")
	if news_num == 1:
		news(chosun)
	elif news_num == 2:
		news(joins)
	elif news_num == 3:
		news(donga)
	elif news_num == 0:
		break
	elif news_num < 0 or news_num > 3:
		print '에러! 1~3 사이의 숫자를 입력해주세요'
