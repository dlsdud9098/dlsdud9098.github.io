#%%
import requests
from bs4 import BeautifulSoup
import os
import time
import datetime
from glob import glob
import re

#%%
# html 형식 md 형식으로 변환
def convert_tag_to_markdown(tag):
    content = tag.decode_contents()

    content = content.replace("<code>", "`")
    content = content.replace("</code>", "`")

    content = content.replace("<h5>", "#### ")
    content = content.replace("</h5>", "")
    
    content = content.replace('<h6 class="guide-section-title">', "#### ")
    content = content.replace("</h6>", "")
    
    content = re.sub(r"<div.*?>", "", content)
    content = content.replace('</div>', '')

    content = content.replace("<hr/>", "\n---")

    content = content.replace("<ul>", "")
    content = content.replace("<li>", "- ")
    content = content.replace("</ul>", "")
    content = content.replace("</li>", "")
    
    content = content.replace("<p>", "\n\n")
    content = content.replace("</p>", "\n\n")
    
    content = content.replace('<pre class="codehilite">', '``')
    content = content.replace('</pre>', '``')
    
    content = content.replace('```', '```\n')
    
    
    content = content.replace('####', '##')
    
    content = content.replace('## 문제 설명', '## 💡문제 설명\n')
    content = content.replace('## 제한사항', '## 🚫제한사항\n')
    content = content.replace('## 입출력 예 설명', '## 🔍입출력 예 설명\n')
    content = content.replace('## 입출력 예', '## 🔢입출력 예\n\n')

    # 이미지 변경
    if '<img' in content:
        def img_to_md(match):
            alt = match.group('alt')
            src = match.group('src')
            title = match.group('title')
            return f'\n![{alt}]({src} "{title}")\n\n'
        
        img_regex = r'<img\s+.*?alt="(?P<alt>.*?)".*?src="(?P<src>.*?)".*?title="(?P<title>.*?)".*?>'
        content = re.sub(img_regex, img_to_md, content)
        
    # 맨 앞에 이미지 추가
    content = '![](/assets/img/content_imgs/programmers_img.png)\n' + content

    return content
#%%
# 프로그래머스
def programmers(file, now_date):
    file_name = os.path.basename(file)
    code_number = file_name.split('_')[1][:-3]
    
    # url
    programmers_url = f'https://school.programmers.co.kr/learn/courses/30/lessons/{code_number}'

    rq = requests.get(programmers_url)
    soup = BeautifulSoup(rq.text, 'html.parser')

    # 본문
    content = soup.select_one('#tour2 > div')
    content = convert_tag_to_markdown(content)

    # 제목
    title = soup.select_one('#tab > li').text.replace('\n', '').strip()

    title = f'''
---
title: "{title}"
categories: [Algorithms, Programmers]
tags: [Programmers, Python, Algorithms]
---
'''.lstrip() + '\n\n'

    content = title + content
    
    # 코드 넣기
    with open(file, 'r') as f:
        file_content = ''.join(f.readlines())
    
    file_content = '```python\n' + file_content + '\n```'
    content = content + '\n\n\n## 💻코드\n' + file_content
    # 문제 링크 넣기
    content = content + '\n\n---\n\n' + f'[문제 링크]({programmers_url})'
    
    with open(f'./_posts/programmers/{now_date}-programmers{code_number}.md', 'w', encoding='utf-8') as file:
        file.write(content)
    
#%%
# 백준
def baekjoon(file):
    baekjoon_url = ''
    
#%%
today_date = datetime.date.today()

today_date = today_date.strftime('%Y-%m-%d')

# 코드 파일 폴더 명
originally_code_files_folder = '.\\code_files\\'
file_list = glob(originally_code_files_folder+'*')


# 포스트 파일 폴더 명
post_folder_path = '.\\_posts\\programmers\\'
post_list = glob(post_folder_path+'*')

post_file_list = [os.path.basename(post)[22:-3] for post in post_list]

for file in file_list:
    code_number = os.path.basename(file).split('_')[1][:-3]
    
    # 이미 만든 파일은 넘어가기
    if code_number in post_file_list:
        continue
    
    file_creation_time = os.path.getctime(file)
    file_creation_time = datetime.datetime.fromtimestamp(file_creation_time)
    file_creation_time = file_creation_time.strftime('%Y-%m-%d')
    
    # 파일 생성 날짜가 오늘 날짜와 일치한지 확인
    if file_creation_time == today_date:
        # 프로그래머스 파일 일 경우
        if 'programmers' in file:
            print(file)
            programmers(file, file_creation_time)
        # 백준 파일 일 경우
        elif 'baekjoon' in file:
            print(file)
            baekjoon(file, file_creation_time)
            
# %%

