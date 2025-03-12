
---
layout: post
title: "프로그래머스 - 95"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 약수의 합


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.


## 제한 사항
* ```n```
은 0 이상 3000이하인 정수입니다.




## 🔢입출력 예




<table><thead><tr><th>n</th><th>return</th></tr></thead><tbody><tr><td>12</td><td>28</td></tr><tr><td>5</td><td>6</td></tr></tbody>
</table>


## 🔍입출력 예 설명
입출력 예 #1<br/>12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.
입출력 예 #2<br/>5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
---


## 💻코드


```python
def solution(n):
    nums = []
    for i in range(1, n+1):
        if n % i == 0:
            if not i in nums:
                nums.append(i)
            else:
