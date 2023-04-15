---
layout: post
title: "장르 자동 분류기 만들기 #3"
categories: [Project, Genre Division]
tags: [Python, NLP, Crawling]
---

<br>

지난번에 파일로 저장한 링크를 불러와 하나씩 가져와 데이터를 만드는 코드를 작성했다.

```python
# 제목
start = source.index('title":"')
end = source.index('","o')
title = source[start+8:end-6]
novel_title.append(title)

# 작가
start = source.index('author":"')
end = source.index('},"i')
author = source[start+9:end-1]
novel_author.append(author)

# 소개글
start = source.index('n":"')
end = source.index('","u')
intro = source[start+4:end]
novel_intro.append(intro)

# 장르
start = source.index('"소설 | ')
end = source.index('"}}}},')
genre = source[start+6:end]
novel_genre.append(genre)

print(f'{title}, {author}, {genre}')
```

오래 걸릴 것 같아 켜놓고 잤는데 자고 일어나니 오류가 뜨면서 멈췄다.

시간은 974분이 걸렸는데, 974분이 허공으로 날아가는 사태가 발생했다.

```
All arrays must be of the same length
```

이런 오류가 뜨면서 멈췄는데 다음과 같다.
`배열의 길이가 같지 않다`
크롤링 하는 도중에 데이터가 없어서 `python try: except:`로 묶었는데 여기가 화근이였다.

보통 author가 데이터가 없었는데, 만약 author에서 문제가 발생하면 title은 정상적으로 들어가는데, author와 genre, intro 부분이 들어가지 않아 각 배열의 길이가 같이 않게 된다.

그래서 지금 부랴부랴 코드를 수정했다.

```python
kakao_novel_list = pd.DataFrame()
cnt = 0
no = 0
# 파일에서 링크 읽어서 정보 가져오기
for novel_href in link_list:
    page = requests.get(novel_href+'?tab_type=about')
    soup = BeautifulSoup(page.content, 'html.parser')
    source = soup.find_all('script')
    source = source[-1].text

    try:
        # 제목
        start = source.index('title":"')
        end = source.index('","o')
        title = source[start+8:end-6]
    except:
        title = None

    try:
        # 작가
        start = source.index('author":"')
        end = source.index('},"i')
        author = source[start+9:end-1]
    except:
        author = None

    try:
        # 소개글
        start = source.index('n":"')
        end = source.index('","u')
        intro = source[start+4:end]
    except:
        intro = None

    try:
        # 장르
        start = source.index('"소설 | ')
        end = source.index('"}}}},')
        genre = source[start+6:end]
    except:
        genre = None

    try:
        novel_data = {
            'title': title,
            'author': author,
            'intro': intro,
            'genre': genre
        }

		# index=[0] 없으면 Value Error  If using all scalar values, you must pass an index 오류 뜸 이는 데이터프레임의 인덱스가 달라서 생기는 일
        df = pd.DataFrame(novel_data, index=[0])
        kakao_novel_list = pd.concat([kakao_novel_list, df])
    except:
        no += 1
        print('정보 없음')
    cnt += 1

print(f'{cnt}개 완료, {no}개 실패')
kakao_novel_list.to_csv('kakao_novel_list.csv', encoding='utf-8-sig')
kakao_novel_list
```

그냥 소설 하나씩 가져와서 없으면 해당 정보가 없으면 None 처리하는 방식으로 했고, 데이터 프레임도 다 모으고 만드는게 아닌, 소설마다 데이터 프레임을 만들고 합치는 방법으로 했다.

저렇게 하는건 좀 비효율 적인거 같고 데이터 프레임 만드는 것은 이렇게 했어도 좋았을 것 같다는 생각이 든다.

```python
    kakao_list = []
    try:
        novel_data = {
            'title': title,
            'author': author,
            'intro': intro,
            'genre': genre
        }

        df = pd.DataFrame(novel_data, index=[0])
        kakao_list.append(df)
    except:
        no += 1
        print('정보 없음')

    kakao_novel_list = pd.concat(kakao_list)
```

하지만 이미 데이터는 다 모았으니 상관 없을 것 같다.

전 코드는 974분이 걸렸는데, 그냥 귀찮아서 time.sleep을 빼고 진행했더니 3시간 만에 다 모았다 ㄷㄷ

내 974분...

![](https://velog.velcdn.com/images/dlsdud9098/post/92d6422b-1a8d-401a-a4bc-41ed69a7bd4e/image.png)

[장르 자동 분류기 #2](https://velog.io/@dlsdud9098/%EC%9E%A5%EB%A5%B4-%EC%9E%90%EB%8F%99-%EB%B6%84%EB%A5%98%EA%B8%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0-2)
[장르 자동 분류기 #1](https://velog.io/@dlsdud9098/%EC%9E%A5%EB%A5%B4-%EC%9E%90%EB%8F%99-%EB%B6%84%EB%A5%98%EA%B8%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0-1)
