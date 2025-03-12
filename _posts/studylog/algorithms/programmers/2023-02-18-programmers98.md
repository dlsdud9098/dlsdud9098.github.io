
---
layout: post
title: "프로그래머스 - 98"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 정수 내림차순으로 배치하기


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.


## 제한 조건
* ```n```
은 1이상 8000000000 이하인 자연수입니다.




## 🔢입출력 예




<table><thead><tr><th>n</th><th style="text-align: center">return</th></tr></thead><tbody><tr><td>118372</td><td style="text-align: center">873211</td></tr></tbody>
</table>
---


## 💻코드


```python
def solution(n):
    answer = []
    
    for i in range(len(str(n))):
        answer.append(str(n)[i])
    answer = sorted(answer, reverse=True)
    return int(''.join(answer))
```
    


