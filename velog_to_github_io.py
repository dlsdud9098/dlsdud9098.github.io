#%%
# !pip install html2text
#%%
# 프로그래머스 파일 만들기
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
from glob import glob
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import re
import json
from markdownify import markdownify
import html2text

#%%

cookies = {
    '_gcl_au': '1.1.1888853790.1680250257',
    '_fbp': 'fb.2.1680250256844.1694083151',
    'locale': 'ko',
    'timezone': 'Asia%2FSeoul',
    '_gid': 'GA1.3.1508085567.1681434024',
    '_ba_rand': '93',
    '_ba_exist': 'true',
    '_clck': 'h58u6e|1|far|0',
    '_programmers_session_production': '01f80c2a17a31f3a51296c80bd176705',
    'my_courses_tab': 'learning',
    'ch-veil-id': '8e857bf2-124e-40bf-9e99-59aa617daf47',
    '_beu_utm_source': '__null__',
    '_beu_utm_medium': '__null__',
    '_beu_utm_campaign': '__null__',
    '_beu_utm_term': '__null__',
    '_beu_utm_content': '__null__',
    '_rtetUrl': 'https%3A%2F%2Fschool.programmers.co.kr%2F',
    '_rtetSessId': 'LLdyYGu47',
    'theme': 'light',
    'ch-session-23033': 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiIyMzAzMy02M2U1YjQ0N2E5YjVjOTY2M2EzOSIsImlhdCI6MTY4MTQzNDMxMSwiZXhwIjoxNjg0MDI2MzExfQ.JZxBWgG639XSv5yPSCcwap9r5yFaP-HDElqYyKHr06w',
    '_ba_initial_refer': 'https%3A%2F%2Fwww.google.com%2F',
    '_ba_initial_refer': '',
    '_rtetSessPageSeq': '2',
    '_ba_ssid': 'xHrqIJAi',
    '_ba_page_ct': '2023-04-14T01%3A07%3A14.228Z',
    '_ba_last_2nd_url': 'https%3A%2F%2Fschool.programmers.co.kr%2Flearn%2Fchallenges%3Forder%3Drecent%26page%3D9%26statuses%3Dsolved',
    '_ba_page_seq': '14',
    '_ba_parent_seq': '19',
    '_ba_last_url': 'https%3A%2F%2Fschool.programmers.co.kr%2Flearn%2Fchallenges%3Forder%3Drecent%26page%3D8%26statuses%3Dsolved',
    '_clsk': '1pw1r2r|1681435351423|32|1|t.clarity.ms/collect',
    '_gat_UA-72680702-5': '1',
    '_ga_XQDBZXSH2X': 'GS1.1.1681434024.2.1.1681435602.60.0.0',
    '_ga': 'GA1.1.666956520.1680250257',
    '_ba_reload_count': '1',
}

headers = {
    'authority': 'school.programmers.co.kr',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=production,sentry-public_key=96f9fc1ff3f44acbb98a9c156338d14b,sentry-trace_id=e7a47000574c486b8e8185adebcdc625,sentry-sample_rate=0.01',
    # 'cookie': '_gcl_au=1.1.1888853790.1680250257; _fbp=fb.2.1680250256844.1694083151; locale=ko; timezone=Asia%2FSeoul; _gid=GA1.3.1508085567.1681434024; _ba_rand=93; _ba_exist=true; _clck=h58u6e|1|far|0; _programmers_session_production=01f80c2a17a31f3a51296c80bd176705; my_courses_tab=learning; ch-veil-id=8e857bf2-124e-40bf-9e99-59aa617daf47; _beu_utm_source=__null__; _beu_utm_medium=__null__; _beu_utm_campaign=__null__; _beu_utm_term=__null__; _beu_utm_content=__null__; _rtetUrl=https%3A%2F%2Fschool.programmers.co.kr%2F; _rtetSessId=LLdyYGu47; theme=light; ch-session-23033=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiIyMzAzMy02M2U1YjQ0N2E5YjVjOTY2M2EzOSIsImlhdCI6MTY4MTQzNDMxMSwiZXhwIjoxNjg0MDI2MzExfQ.JZxBWgG639XSv5yPSCcwap9r5yFaP-HDElqYyKHr06w; _ba_initial_refer=https%3A%2F%2Fwww.google.com%2F; _ba_initial_refer=; _rtetSessPageSeq=2; _ba_ssid=xHrqIJAi; _ba_page_ct=2023-04-14T01%3A07%3A14.228Z; _ba_last_2nd_url=https%3A%2F%2Fschool.programmers.co.kr%2Flearn%2Fchallenges%3Forder%3Drecent%26page%3D9%26statuses%3Dsolved; _ba_page_seq=14; _ba_parent_seq=19; _ba_last_url=https%3A%2F%2Fschool.programmers.co.kr%2Flearn%2Fchallenges%3Forder%3Drecent%26page%3D8%26statuses%3Dsolved; _clsk=1pw1r2r|1681435351423|32|1|t.clarity.ms/collect; _gat_UA-72680702-5=1; _ga_XQDBZXSH2X=GS1.1.1681434024.2.1.1681435602.60.0.0; _ga=GA1.1.666956520.1680250257; _ba_reload_count=1',
    'referer': 'https://school.programmers.co.kr/learn/challenges?order=recent&page=8&statuses=solved',
    'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'e7a47000574c486b8e8185adebcdc625-921fd54308cdac3d-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36',
}


file_feature = {}

for i in range(1, 9):
	response = requests.get(
		f'https://school.programmers.co.kr/api/v1/school/challenges/?perPage=20&statuses[]=solved&order=recent&page={i}',
		cookies=cookies,
		headers=headers,
	)
	content = json.loads(response.text)

	for item in content['result']:
		file_feature[item['id']] = item['finishedAt'][:10]
#%%
# file_list = glob(r'C:\Users\inyoung\Desktop\git_programmers\*')
file_list = glob(r'../git_programmers/now/*')
file_names = os.listdir('../git_programmers/now/')

file_create_date = {}
now_date_upload_llist = []

# file_list = file_list[:1]
# file_names = file_names[:1]

# print(file_list, file_names)
i = 0
for idx, file in zip(file_names, file_list):
	# print(idx)
	url = f'https://school.programmers.co.kr/learn/courses/30/lessons/{idx}'
	rq = requests.get(url)

	print(file)
	with open(file, 'r', encoding='UTF8') as f:
		code = f.read()

	soup = BeautifulSoup(rq.content, 'html.parser')

	result = []
	title = soup.select_one('#tab > li').text.lstrip().rstrip()
	content = str(soup.select_one('#tour2 > div'))
	content = content.split('\n')
	for con in content:
		if ' class' in con:
			con = con[:con.index(' class')] + con[con.index('">')+1:]

		if '<h6>' or '<h5>' or '<h4>' in con:
			con = con.replace('<h6>', '\n## ')
			con = con.replace('<h5>', '\n## ')
			con = con.replace('<h4>', '\n## ')
		
		if '</h6>' or '</h5>' or '</h4>' in con:
			con = con.replace('</h6>', '')
			con = con.replace('</h5>', '')
			con = con.replace('</h4>', '')
		
		if '<div>' in con:
			con = con.replace('<div>', '')
		if '</div>' in con:
			con = con.replace('</div>', '')
		
		if '<hr/>' or '</hr>' in con:
			con = con.replace('</hr>', '\n---\n\n')
			con = con.replace('<hr/>', '\n---\n\n')

		if '<ul>' or '</ul>' in con:
			con = con.replace('<ul>', '')
			con = con.replace('</ul>', '')
		
		if '<li>' in con:
			con = con.replace('<li>', '\n* ')
		
		if '</li>' in con:
			con = con.replace('</li>','\n\n')

		if '<p>' or '</p>' in con:
			con = con.replace('<p>', '')
			con = con.replace('</p>', '\n')

		# if 'code>' in con:
		# 	con  =con.replace('<code>', '```')
		# 	con  =con.replace('</code>', '```\n')
		
		if '<table>' in con:
			con = con.replace('<table>', '\n<table>')
		
		if '</table>' in con:
			con = con.replace('</table>', '\n</table>\n')
   
		if '<img' in con:
			# start = con.find('<img ')
			# end = con[start:].find('/>')

			# srcstart = con[start:end].find('src=')
			# srcend = con[srcstart:end].find('\"')
			# img_link = f'![]({con[srcstart+4:srcend]})'
   
			# con[start:end+1] = 
			def img_to_md(match):
				alt = match.group('alt')
				src = match.group('src')
				title = match.group('title')
				return f'\n![{alt}]({src} "{title}")\n\n'


   
			img_regex = r'<img\s+.*?alt="(?P<alt>.*?)".*?src="(?P<src>.*?)".*?title="(?P<title>.*?)".*?>'
			con = re.sub(img_regex, img_to_md, con)
   



		if '문제 설명' in con:
			con = con.replace('## 문제 설명', '## 💡문제 설명\n')
		if '제한사항' in con:
			con = con.replace('## 제한사항', '## 🚫제한사항\n')
		if '입출력 예 설명' in con:
			con = con.replace('## 입출력 예 설명', '## 🔍입출력 예 설명\n')
		if '입출력 예' in con:
			con = con.replace('## 입출력 예', '## 🔢입출력 예\n\n')
		

		result.append(con)

	result.append('---\n\n')
	result.append('## 💻코드')
	result.append('\n')
	result.append(f'''
```python
{code}
```
	''')
	result.append('\n\n')


	# 맨 처음에 사진 추가하기
	result.insert(0, '![](../assets/img/content_imgs/programmers_img.png)')

	link = url.replace('.py', '?language=python3')
	# 해당 문제 링크 추가
	result.append(f'[문제 링크]({link})')

	result.insert(0, f'''
---
title: "{title}"
categories: [Algorithms, Programmers]
tags: [Programmers, Python, Algorithms]
---
'''.lstrip())

	# date = file_feature[int(idx[:-3])]
	date = datetime.today().strftime("%Y-%m-%d")
	velog_content_all = ''.join(result)
	with open(f'./_posts/{date}-programmers{idx[:-3]}.md', 'w') as f:
		f.write(velog_content_all)
	i += 1

# %%
url_list = [
	'https://www.acmicpc.net/status?user_id=dlsdud908&result_id=4',
	'https://www.acmicpc.net/status?user_id=dlsdud908&result_id=4&top=54400813',
	'https://www.acmicpc.net/status?user_id=dlsdud908&result_id=4&top=46619160'
]


cookies = {
    'OnlineJudge': '89hqasi3mdm295s9u48f5301in',
    '_ga': 'GA1.1.720863056.1681434089',
    '_fbp': 'fb.1.1681434088949.922141639',
    '__gads': 'ID=88f264aa96ad178e-225a864711df003d:T=1681434097:RT=1681434097:S=ALNI_MYprGTClceHiyOwTlSe8oRc75Hlsg',
    '__gpi': 'UID=00000be26018510a:T=1681434097:RT=1681434097:S=ALNI_Mb1UDdAq16d7gNI-kH6JXB236z5bg',
    '_ga_C81GGQEMJZ': 'GS1.1.1681436561.2.1.1681440308.0.0.0',
}

headers = {
    'authority': 'www.acmicpc.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'OnlineJudge=89hqasi3mdm295s9u48f5301in; _ga=GA1.1.720863056.1681434089; _fbp=fb.1.1681434088949.922141639; __gads=ID=88f264aa96ad178e-225a864711df003d:T=1681434097:RT=1681434097:S=ALNI_MYprGTClceHiyOwTlSe8oRc75Hlsg; __gpi=UID=00000be26018510a:T=1681434097:RT=1681434097:S=ALNI_Mb1UDdAq16d7gNI-kH6JXB236z5bg; _ga_C81GGQEMJZ=GS1.1.1681436561.2.1.1681440308.0.0.0',
    'referer': 'https://www.acmicpc.net/',
    'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36',
}
params = [
	{'user_id': 'dlsdud908',
    'result_id': '4'},
	{'user_id': 'dlsdud908',
    'result_id': '4',
    'top': '54400813'},
	{'user_id': 'dlsdud908',
    'result_id': '4',
    'top': '46619160'}
]
sublink = []
problem_links = []
soup_dates = []
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36'
}

items = {}
for param in params:
	# rq = requests.get(url, headers=headers)
	# soup = BeautifulSoup(rq.text, 'html.parser')
    
	response = requests.get('https://www.acmicpc.net/status', params=param, cookies=cookies, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
 
	soup_p = soup.find('table')
	table_tr = soup_p.find_all('tr')
	
	# print(table_tr)
	print(len(table_tr))
	
	for tr in table_tr[1:]:
		# print(tr)
		if 'Python' in tr.find("a", href=lambda href: href and "/source/" in href).text:
			id = tr.find('a', {'class': 'problem_title tooltip-click result-ac'}).text
		
			problem = tr.find('a', {'class': 'problem_title tooltip-click result-ac'}).get('href')
			source = tr.find("a", href=lambda href: href and "/submit/" in href).get('href')
			date = tr.find_all('td')[-1].find('a')['title']
			print(id, problem, source, date)

			items[id] = ['https://www.acmicpc.net'+problem, 'https://www.acmicpc.net'+source, date]

# problem_links = problem_links[:-7]
# print(problem_links)
cookies = {
    'OnlineJudge': '89hqasi3mdm295s9u48f5301in',
    '_ga': 'GA1.1.720863056.1681434089',
    '_fbp': 'fb.1.1681434088949.922141639',
    '__gads': 'ID=88f264aa96ad178e-225a864711df003d:T=1681434097:RT=1681434097:S=ALNI_MYprGTClceHiyOwTlSe8oRc75Hlsg',
    '__gpi': 'UID=00000be26018510a:T=1681434097:RT=1681434097:S=ALNI_Mb1UDdAq16d7gNI-kH6JXB236z5bg',
    '_ga_C81GGQEMJZ': 'GS1.1.1681436561.2.1.1681440759.0.0.0',
}

headers = {
    'authority': 'www.acmicpc.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'OnlineJudge=89hqasi3mdm295s9u48f5301in; _ga=GA1.1.720863056.1681434089; _fbp=fb.1.1681434088949.922141639; __gads=ID=88f264aa96ad178e-225a864711df003d:T=1681434097:RT=1681434097:S=ALNI_MYprGTClceHiyOwTlSe8oRc75Hlsg; __gpi=UID=00000be26018510a:T=1681434097:RT=1681434097:S=ALNI_Mb1UDdAq16d7gNI-kH6JXB236z5bg; _ga_C81GGQEMJZ=GS1.1.1681436561.2.1.1681440759.0.0.0',
    'referer': 'https://www.acmicpc.net/',
    'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36',
}
codes = []
for id, [problem, submit, date] in items.items():

	response = requests.get(submit, cookies=cookies, headers=headers)

	soup = BeautifulSoup(response.text, 'html.parser')

	codes.append(soup.find('textarea').get_text())

cookies = {
    'OnlineJudge': '89hqasi3mdm295s9u48f5301in',
    '_ga': 'GA1.1.720863056.1681434089',
    '_fbp': 'fb.1.1681434088949.922141639',
    '__gads': 'ID=88f264aa96ad178e-225a864711df003d:T=1681434097:RT=1681434097:S=ALNI_MYprGTClceHiyOwTlSe8oRc75Hlsg',
    '__gpi': 'UID=00000be26018510a:T=1681434097:RT=1681434097:S=ALNI_Mb1UDdAq16d7gNI-kH6JXB236z5bg',
    '_ga_C81GGQEMJZ': 'GS1.1.1681436561.2.1.1681442704.0.0.0',
}

headers = {
    'authority': 'www.acmicpc.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'OnlineJudge=89hqasi3mdm295s9u48f5301in; _ga=GA1.1.720863056.1681434089; _fbp=fb.1.1681434088949.922141639; __gads=ID=88f264aa96ad178e-225a864711df003d:T=1681434097:RT=1681434097:S=ALNI_MYprGTClceHiyOwTlSe8oRc75Hlsg; __gpi=UID=00000be26018510a:T=1681434097:RT=1681434097:S=ALNI_Mb1UDdAq16d7gNI-kH6JXB236z5bg; _ga_C81GGQEMJZ=GS1.1.1681436561.2.1.1681442704.0.0.0',
    'referer': 'https://www.acmicpc.net/',
    'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36',

}

for id, [problem, submit, date] in items.items():
	response = requests.get(problem, cookies=cookies, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	title = soup.select_one('#problem_title').text
	soup = soup.find('div', {'id':'problem-body'})
	section = soup.find_all('section')

	htmltext = html2text.HTML2Text()

	md_string=''
	for i in section:
		md_string += htmltext.handle(str(i)) + '\n'
		
	md_string = re.sub(r'\n{2,}', '\n', md_string)
	md_string = md_string.replace('##', '\n##')
	md_string = re.sub(r'\n\s*\n', '\n\n', md_string)
	# print(md_string)

	text = f'''
---
layout: post
title: "{title}"
categories: [Algorithms, Baekjoon]
tags: [Baekjoon, Python, Algorithms]
image: /assets/img/content_imgs/baekjoon_img.png
---

{md_string}

```python
{codes[0]}
```
{problem}
'''.lstrip()


	with open(f'./_posts/baekjoon/{date[:10]}-baekjoon{id}.md', 'w') as f:
		f.write(text)
# %%
