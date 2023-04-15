---
layout: post
title: BeautifulSoup 크롤링 속도 높이기
categories: [Coding, Python]
tags: [python]
---
<br>

크롤링을 할 때 보통 requests와 BeautifulSoup을 통해 크롤링을 한다.

빠르긴 하지만 몇 만개의 데이터를 처리할 때는 이마저도 느리게 보인다.

더 빠르게 처리하기 위해서 크롤링을 혼자서가 아닌 여러명에서 하면 된다.

그것이 바로 멀티 프로세싱을 이용하는 방법이다.

## 모듈 설치

`pip install multiprocess`

일단 multiprocess를 설치한 후 모듈을 import 한다

```python
from multiprocessing import Pool, Manager
```

## 예제

```python
freeze_support()

# 코어 수
pool = Pool(processes=5)
# 함수, 파라미터
pool.starmap(crawl_link, zip(link_list,repeat(novel_df_list)))

pool.close()
```

freeze_support()가 없으면 에러가 난다.
꼭 import 하자

```python
from multiprocessing import Process, freeze_support
```

pool에 5개의 코어를 쥐어준다.
코어가 많을수록 속도는 빠르지만 4개까지는 드라마처럼 빨라지지만, 일정 개수 이상부터는 큰 차이가 없다고 한다.(보통 4개로 설정함)

```python
pool.starmap(함수 이름, 파라미터)
```

파라미터가 하나라면 한 개만 쓰면 되고, 두개 이상일 경우 zip()으로 묶는다.

참고로 multiprocessing으로 처리할 때 일반적인 배열을 global로 사용할 수 없다.

한 마디로

```python
link_list = ['sadf','asdf','asdf','sadf','asdf','asdf','sadf','asdf','asdf']
list_a = []
def test(link):
	global list_a
	list_a.append(link)


if __name__ == '__main__':
    freeze_support()

    pool = Pool(processes=4)
    pool.starmap(test, zip(link_list))

    pool.close()

    print(list_a)
```

가 불가능 하다는 소리다.
결과 값은 []. 빈 배열이 나온다.

그렇기 때문에 multiprocessing에서 배열이나 딕셔너리를 사용하고 싶다면 Manager()를 사용해야 한다.

```python
from multiprocessing import Process, freeze_support
from multiprocessing import Pool, Manager
from itertools import repeat

link_list = ['sadf','asdf','asdf','sadf','asdf','asdf','sadf','asdf','asdf']

def test(link, list_a):
	list_a.append(link)

if __name__ == '__main__':
    m = Manager()
    list_a = m.list()

    freeze_support()

    pool = Pool(processes=4)
    pool.starmap(test, zip(link_list, repeat(list_a)))
    pool.close()

    print(list_a)
```

Manager를 통해 빈 리스트를 만들고, 파라미터로 넣어주면 된다.

넣어줄 때, repeat을 통해 프로세스 개수만큼 들어가도록 해준다.
(repeat을 빼면 전과 마찬가지로 빈 배열이 나온다.)

참고로 jupyter에서 안될때가 있는데(나도 안됐다), 일반 파이썬으로 돌리면 정상적으로 작동한다.
(.ipynb가 아닌 .py)
