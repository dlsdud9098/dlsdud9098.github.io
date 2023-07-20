#%%
import requests
from bs4 import BeautifulSoup
import os
import time
import datetime
from glob import glob

#%%
# 프로그래머스
def programmers(file):    
    file_name = os.path.basename(file)
    code_number = file_name.split('_')[1][:-3]
    programmers_url = f'https://school.programmers.co.kr/learn/courses/30/lessons/{code_number}'
    
    rq = requests.get(programmers_url)
    soup = BeautifulSoup(rq.text, 'html.parser')
    # 문제 설명
    content = soup.select_one('#tour2 > div > div > p:nth-child(1)')
    content1 = str(content.prettify())
    content1 = content1.replace('  ', '').replace('\n ', '').replace('\n', '').replace('<p>', '').replace('</p>', '').replace('<code>','```').replace('</code>', '```')
    
    # 제한사항
    content = soup.select_one('#tour2 > div > div > ul:nth-child(4) > li')
    content2 = str(content.prettify())
    content2 = content2.replace('  ', '').replace('\n ', '').replace('\n', '').replace('<p>', '').replace('</p>', '').replace('<code>','```').replace('</code>', '```').replace('<li>', '* ').replace('</li>', '')
    
    # 입출력 예
    content = soup.select_one('#tour2 > div > div > table')
    
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

for file in file_list:
    file_creation_time = os.path.getctime(file)
    file_creation_time = datetime.datetime.fromtimestamp(file_creation_time)
    file_creation_time = file_creation_time.strftime('%Y-%m-%d')
    
    # 파일 생성 날짜가 오늘 날짜와 일치한지 확인
    if file_creation_time == today_date:
        # 프로그래머스 파일 일 경우
        if 'programmers' in file:
            programmers(file)
        # 백준 파일 일 경우
        elif 'baekjoon' in file:
            baekjoon(file)
        
        
#%%
