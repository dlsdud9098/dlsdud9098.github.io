---
layout: post
title: "장르 자동 분류기 만들기 #4"
categories: [Project, Genre Division]
tags: [Python, NLP, Crawling]
---

<br>

이전까지는 카카오 페이지의 소설 정보들을 크롤링했다.

데이터 프레임까지 다 만들었으니 이제는 네이버 소설을 크롤링할 차례다.

먼저 네이버 시리즈 각 카테고리의 링크들을 가져오자

```python
# 네이버 소설 크롤링 본문
url_list = {
    '로맨스': 'https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=genre&genreCode=201&page=', # 로맨스
    '로판': 'https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=genre&genreCode=207&page=', # 로판
    '판타지': 'https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=genre&genreCode=202&page=', # 판타지
    '현판': 'https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=genre&genreCode=208&page=', # 현판
    '무협': 'https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=genre&genreCode=206&page=', # 무협
    '미스터리': 'https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=genre&genreCode=203&page=', # 미스터리(판타지)
}
```

이번에는 이전과는 다른 방식으로 효율성을 높였다.
저번에는 한 카테고리리를 크롤링 할 때마다 파일 이름을 바꿔주며 했는데, 이번에는 딕셔너리로 만들어, 키 값을 파일 이름으로 넣는 방식으로 했다.

또한 함수를 만드는 방식으로 코드를 작성했다.

```python
for name, url in url_list.items():
    write_novel_file(name, url)
```

```python
# 링크 가져와서 텍스트 파일로 저장하는 함수
def write_novel_file(genre_name, url):
    i = 1
    cnt = 0
    prev_soup = 0
    f = open(f'{genre_name}.txt', 'w')
    while True:
        now_url = url+str(i)
        rq = requests.get(now_url)
        time.sleep(.5)

        soup = BeautifulSoup(rq.content, 'html.parser')

        # 페이지의 끝에 도달하면 반복 끝내기
        if prev_soup == soup:
            break

        novel_list = soup.select('#content > div > ul > li')
        for novel in novel_list:
            href = novel.find('a')['href']
            print(href, file=f)
            cnt += 1

        print(f'{i} 페이지 완료')
        i += 1
        prev_soup = soup

    f.close()
    print(f'{genre_name} 완료, {cnt}')
```

전체적인 부분은 카카오 페이지를 크롤링할 때와 비슷하기 때문에 설명은 생략한다.

![](https://velog.velcdn.com/images/dlsdud9098/post/f9ce903a-30e1-4a97-bc75-01fd5556b7e8/image.png)
![](https://velog.velcdn.com/images/dlsdud9098/post/1b79d9ef-acf4-495c-b5f7-4dac04589f82/image.png)
