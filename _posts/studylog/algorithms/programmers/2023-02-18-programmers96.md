---
layout: post
title: "프로그래머스 - 96"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 자릿수 더하기


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.<br/>예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.


## 🚫제한사항


* N의 범위 : 100,000,000 이하의 자연수




---




## 🔢입출력 예




<table><thead><tr><th>N</th><th>answer</th></tr></thead><tbody><tr><td>123</td><td>6</td></tr><tr><td>987</td><td>24</td></tr></tbody>
</table>


## 🔍입출력 예 설명
입출력 예 #1<br/>문제의 예시와 같습니다.
입출력 예 #2<br/>9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.
---


## 💻코드


```python
def solution(n):
    answer = 0


