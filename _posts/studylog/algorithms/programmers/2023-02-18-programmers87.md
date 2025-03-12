---
layout: post
title: "프로그래머스 - 87"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 가운데 글자 가져오기


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.


## 재한사항
* s는 길이가 1 이상, 100이하인 스트링입니다.




## 🔢입출력 예




<table><thead><tr><th>s</th><th>return</th></tr></thead><tbody><tr><td>"abcde"</td><td>"c"</td></tr><tr><td>"qwer"</td><td>"we"</td></tr></tbody>
</table>
---


## 💻코드


```python
def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        answer = s[len(s) // 2 -1:len(s) // 2+1]
    else:
        answer = s[len(s) // 2]
    return answer
```
    


https://school.programmers.co.kr/learn/courses/30/lessons/12903?language=python3
