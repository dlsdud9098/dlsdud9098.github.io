
---
layout: post
title: "프로그래머스 - 93"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 수박수박수박수박수박수


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.


## 제한 조건
* n은 길이 10,000이하인 자연수입니다.




## 🔢입출력 예




<table><thead><tr><th>n</th><th>return</th></tr></thead><tbody><tr><td>3</td><td>"수박수"</td></tr><tr><td>4</td><td>"수박수박"</td></tr></tbody>
</table>
---


## 💻코드


```python
def solution(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2 == 0:
            answer += '박'
        else:
            answer += '수'
    return answer
```
    


