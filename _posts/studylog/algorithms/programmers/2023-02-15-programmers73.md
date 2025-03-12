---
layout: post
title: "프로그래머스 - 73"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 겹치는 선분의 길이


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 ```lines```
가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.
```lines```
가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
<img alt="line_2.png" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e4122d8b-9ce2-49ce-a360-3d1284babd8a/line_2.png" title=""/>
선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.


---




## 🚫제한사항


* ```lines```
의 길이 = 3




* ```lines```
의 원소의 길이 = 2




* 모든 선분은 길이가 1 이상입니다.




* ```lines```
의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
* -100 ≤ a &lt; b ≤ 100


