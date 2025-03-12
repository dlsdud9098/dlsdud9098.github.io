
---
layout: post
title: "프로그래머스 - 67"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 2차원으로 만들기


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
정수 배열 ```num_list```
와 정수 ```n```
이 매개변수로 주어집니다. ```num_list```
를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
```num_list```
가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 ```n```
이 2이므로 ```num_list```
를 2 * 4 배열로 다음과 같이 변경합니다. 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.


<table><thead><tr><th>num_list</th><th>n</th><th>result</th></tr></thead><tbody><tr><td>[1, 2, 3, 4, 5, 6, 7, 8]</td><td>2</td><td>[[1, 2], [3, 4], [5, 6], [7, 8]]</td></tr></tbody>
</table>


---




## 🚫제한사항


* ```num_list```
의 길이는 ```n```
의 배 수개입니다.




* 0 ≤ ```num_list```
의 길이 ≤ 150




* 2 ≤ ```n```
