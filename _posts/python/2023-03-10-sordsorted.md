---
layout: post
title: sorted, sort() 문자열 정렬하기
categories: [Coding, Python]
tags: [python]
---
<br>

# sorted와 sort()의 차이점은?

## sort()
### 설명
* 리스트에서만 사용 가능한 메서드(함수)
* 리스트 객체 자체를 정렬해줌
* 리스트 자체를 정렬하기에 반환이 없다.
* 기본적으로 오름차순 정렬이다.
* 대문자와 소문자가 섞여있을 경우, [ASCII CODE](https://velog.velcdn.com/images/dlsdud9098/post/c3dbd760-7190-4131-a547-122836d02fdb/image.png)를 참조하여 오름차순으로 정렬한다.

### 코드
```python
import random

list_a = [random.randint(-10, 15) for i in range(10)]
list_b = [chr(random.randint(97, 122)) for i in range(10)]
list_c = [chr(ascii_list[random.randint(0, 51)]) for _ in range(10)]

print(list_a) # [1, 4, -7, 3, -10, 2, -8, -4, -6, 3]
list_a.sort()
print(list_a) # [-10, -8, -7, -6, -4, 1, 2, 3, 3, 4]

print(list_b) # ['w', 't', 'z', 'm', 't', 'h', 'o', 'a', 'x', 's']
list_b.sort()
print(list_b) # ['a', 'h', 'm', 'o', 's', 't', 't', 'w', 'x', 'z']

print(list_c) # ['H', 'x', 'g', 'M', 'c', 'N', 'M', 'D', 'I', 'G']
list_c.sort()
print(list_c) # ['D', 'G', 'H', 'I', 'M', 'M', 'N', 'c', 'g', 'x']
```

## sorted()
### 설명
* sorted(정렬할 변수, key='어떤 것을 기준으로 할 것인가', reverse='오름차순, 내림차순')
* 오름차순은 False, 내림차순은 True다.
* 만약 단어의 특정 위치를 기준으로 정렬한다고 한다면, lambda x를 이용하여 정렬할 수 있다.

```python
 # 배열: ["abce", "abcd", "cdx"], 비교 자리 수: 2
 # x = ["abce", "abcd", "cdx"], n = 2
 # (x[n], x)는 n번째 글자를 기준으로 오름차순으로 정렬하는 것이고, (x, x[n])는 모든 글자를 기준으로 오름차순으로 정렬
 answer = sorted(strings, key=lambda x: (x[n], x))
```

* 리턴값이 존재하며 리스트 객체 자체를 정렬하지 않는다.

### 코드
```python
import random

ascii_list = [i for i in range(65, 91)] + [i for i in range(97, 123)]
list_a = [random.randint(-10, 15) for i in range(10)]
list_b = [random.randint(97, 122) for i in range(10)]
list_c = [chr(ascii_list[random.randint(0, 51)]) for _ in range(10)]

print(list_a)			# [6, -1, 12, -2, 4, 10, -4, -2, 2, 11]
print(sorted(list_a))	# [-4, -2, -2, -1, 2, 4, 6, 10, 11, 12]
print(list_a)			# [6, -1, 12, -2, 4, 10, -4, -2, 2, 11]

print(list_b)			# [114, 109, 105, 114, 122, 97, 110, 105, 101, 101]
print(sorted(list_b))	# [97, 101, 101, 105, 105, 109, 110, 114, 114, 122]
print(list_b)			# [114, 109, 105, 114, 122, 97, 110, 105, 101, 101]

print(list_c)			# ['D', 'P', 'O', 'U', 'm', 'o', 'z', 'V', 'j', 'H']
print(sorted(list_c))	# ['D', 'H', 'O', 'P', 'U', 'V', 'j', 'm', 'o', 'z']
print(list_c)			# ['D', 'P', 'O', 'U', 'm', 'o', 'z', 'V', 'j', 'H']
```
