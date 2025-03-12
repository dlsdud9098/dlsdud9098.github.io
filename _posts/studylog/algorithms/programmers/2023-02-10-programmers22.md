
---
layout: post
title: "프로그래머스 - 22"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 점의 위치 구하기


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.<br/><img alt="스크린샷 2022-07-07 오후 3.27.04 복사본.png" src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b58d4788-42fa-44fa-af50-481907e65473/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-07-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.27.04%20%E1%84%87%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A1%E1%84%87%E1%85%A9%E1%86%AB.png" title=""/>


* x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.




* x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.




* x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.




* x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.


x  좌표 (x, y)를 차례대로 담은 정수 배열 ```dot```
이 매개변수로 주어집니다. 좌표 ```dot```
이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.


---


<h4>제한사항</h4>
* ```dot```
의 길이 = 2




