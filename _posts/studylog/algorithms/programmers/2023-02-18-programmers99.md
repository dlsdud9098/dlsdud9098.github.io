
---
layout: post
title: "프로그래머스 - 99"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 정수 제곱근 판별


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.<br/>n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.


## 제한 사항
* n은 1이상,  50000000000000 이하인 양의 정수입니다.




## 🔢입출력 예




<table><thead><tr><th>n</th><th style="text-align: center">return</th></tr></thead><tbody><tr><td>121</td><td style="text-align: center">144</td></tr><tr><td>3</td><td style="text-align: center">-1</td></tr></tbody>
</table>


## 🔍입출력 예 설명
<strong>입출력 예#1</strong><br/>121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.
<strong>입출력 예#2</strong><br/>3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.
---


## 💻코드


```python
def solution(n):
    import math
    answer = 0
    
    # 루트를 씌우고 정수형으로 변환
    sqrt_num = int(math.sqrt(n))
