from bs4 import BeautifulSoup
import os,sys
import requests
import sqlite3
import datetime
from datetime import datetime
from dateutil import tz, zoneinfo

from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    api_base_url = 'https://cmx-im.work/'
)

exitcode = 0

#项目参考的是lemonhall/lemon_blog/monitor/main.py

def scraping():
	url = "https://m.guancha.cn/"
	debug = {'verbose': sys.stderr}
	headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'}
	page = requests.get(url,headers=headers)
	page.encoding = 'utf-8'
	soup = BeautifulSoup(page.text, 'html.parser')

	#扫描页面，构造新闻条目的list，供后续处理
	news = []

	#找到所有的li
	items = soup.find_all("li",class_="big-pic")
	for item in items:
		new = {}
		#print(item)
		data_id = item["data-id"]
		title = item.find("h3")
		title_link = item.find("a")

		new["id"] = data_id

		if title:
			new["title"] = title.text
		else:
			new["title"] = "Error reading title"

		if title_link:
			#该条目的超链接
			title_link_href = title_link["href"]
			new["link"] = "https://m.guancha.cn"+title_link_href
		else:
			new["link"] = "Error reading title_link_href"
		news.append(new)
		#print(new)

	#print("==========")

	#找到所有的li
	items = soup.find_all("li",class_="long-pic")
	for item in items:
		new = {}
		#print(item)
		data_id = item["data-id"]
		title = item.find("h3")
		title_link = item.find("a")

		new["id"] = data_id

		if title:
			new["title"] = title.text
		else:
			new["title"] = "Error reading title"

		if title_link:
			#该条目的超链接
			title_link_href = title_link["href"]
			new["link"] = "https://m.guancha.cn"+title_link_href
		else:
			new["link"] = "Error reading title_link_href"
		news.append(new)
		#print(new)

	#print(news)
	return news

	#扫描页面，构造新闻条目的list，供后续处理

def save_in_db(news):
	sync_counter = 0
	con = sqlite3.connect('sync_guancha.db')
	cur = con.cursor()
	tz_sh = tz.gettz('Asia/Shanghai')
	#datetime object containing current date and time
	now = datetime.now(tz=tz_sh)
	# dd/mm/YY H:M:S
	dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
	for new in news:
		saved_in_db = cur.execute("SELECT * FROM sync WHERE id=:id", {"id": new["id"]})
		if saved_in_db.fetchall():
			#数据库里查到了条目，暂时不需要去管它是什么状态，直接跳过就好
			pass
		else:
			#数据库里没有这个条目则插入之
			print("I am going to be synced....")
			sync_counter = sync_counter +1
			print(new)
			cur.execute("insert into sync values (?,?,?,?,?)", (new["id"],new["title"],new["link"],0,datetime.now()))
	#循环完成后提交更改
	con.commit()
	if not sync_counter:
		print("Nothing to be sync....."+ dt_string)
	else:
		print("saving "+ str(sync_counter)+" news into database....."+ dt_string)

	con.close()


def post_to_mastodon(new):
	print("In post_to_mastodon")
	print(new)
	mastodon.toot("观察网新闻："+ new["title"] +"\n\n"+new["link"])

#抄的lemonhall/lemon_blog/coockbook_extractor.py
def sync_to_mastodon():
	## cur.execute('''CREATE TABLE sync (id text, title text, href text, status int, time timestamp)''')
	con = sqlite3.connect('sync_guancha.db')
	cur = con.cursor()
	saved_in_db = cur.execute("SELECT * FROM sync WHERE status=0")
	row_list = saved_in_db.fetchall()
	if row_list:
		for row in row_list:
			print("processing one row...................")
			id_in_db    = row[0]
			title_in_db = row[1]
			url_in_db   = row[2]
			new = {}
			new["title"] = title_in_db
			new["link"]  = url_in_db
			post_to_mastodon(new)
			cur.execute("update sync set status=2 WHERE id=:id", {"id": id_in_db})
		#for 循环结束，status为0的都会被update掉
		con.commit()
	else:
		print("do NOTHING.....nothoning to be synced")
	con.close()

#=======main======

news = scraping()
save_in_db(news)
sync_to_mastodon()
