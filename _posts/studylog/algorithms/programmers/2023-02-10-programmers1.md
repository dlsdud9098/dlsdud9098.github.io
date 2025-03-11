---
layout: post
title: "중복된 숫자 개수"
category: studylog
tags: algorithm
---


## 💡문제 설명
정수가 담긴 배열 ```array```와 정수 ```n```이 매개변수로 주어질 때, ```array```에 ```n```이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

---


## 🚫제한사항

* 1 ≤ ```array```
의 길이 ≤ 100


* 0 ≤ ```array```
의 원소 ≤ 1,000


* 0 ≤ ```n```
 ≤ 1,000


---


## 🔢입출력 예


<table><thead><tr><th>array</th><th>n</th><th>result</th></tr></thead><tbody><tr><td>[1, 1, 2, 3, 4, 5]</td><td>1</td><td>2</td></tr><tr><td>[0, 2, 3, 4]</td><td>1</td><td>0</td></tr></tbody>
</table>

---


## 🔍입출력 예 설명
입출력 예 #1

* [1, 1, 2, 3, 4, 5] 에는 1이 2개 있습니다.

입출력 예 #2

* [0, 2, 3, 4] 에는 1이 0개 있습니다.

---

## 💻코드

```python
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer
```
    

https://school.programmers.co.kr/learn/courses/30/lessons/120583?language=python3