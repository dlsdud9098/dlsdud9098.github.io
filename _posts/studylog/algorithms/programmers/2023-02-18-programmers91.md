
---
layout: post
title: "프로그래머스 - 91"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 문자열 내림차순으로 배치하기


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.<br/>s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.


## 제한 사항
* str은 길이 1 이상인 문자열입니다.




## 🔢입출력 예




<table><thead><tr><th>s</th><th>return</th></tr></thead><tbody><tr><td>"Zbcdefg"</td><td>"gfedcbZ"</td></tr></tbody>
</table>
---


## 💻코드


```python
def solution(s):
    answer = ''
    
    answer = sorted(s, reverse=True)
    return ''.join(answer)
```
    


https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3
