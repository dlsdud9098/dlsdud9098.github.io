---
layout: post
title: "프로그래머스 - 97"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 자연수 뒤집어 배열로 만들기


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.


## 제한 조건
* n은 10,000,000,000이하인 자연수입니다.




## 🔢입출력 예




<table><thead><tr><th>n</th><th>return</th></tr></thead><tbody><tr><td>12345</td><td>[5,4,3,2,1]</td></tr></tbody>
</table>
---


## 💻코드


```python
def solution(n):
    answer = []
    
    for i in range(len(str(n))-1, -1, -1):
        answer.append(int(str(n)[i]))
    return answer
```
    


https://school.programmers.co.kr/learn/courses/30/lessons/12932?language=python3
