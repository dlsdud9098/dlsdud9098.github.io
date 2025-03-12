---
layout: post
title: "프로그래머스 - 88"
category: studylog
tags: algorithm
---

<br>

## 프로그래머스 나누어 떨어지는 숫자 배열


![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)
## 💡문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.<br/>divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요. 


## 🚫제한사항


* arr은 자연수를 담은 배열입니다.




* 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.




* divisor는 자연수입니다.




* array는 길이 1 이상인 배열입니다.




## 🔢입출력 예




<table><thead><tr><th>arr</th><th>divisor</th><th>return</th></tr></thead><tbody><tr><td>[5, 9, 7, 10]</td><td>5</td><td>[5, 10]</td></tr><tr><td>[2, 36, 1, 3]</td><td>1</td><td>[1, 2, 3, 36]</td></tr><tr><td>[3,2,6]</td><td>10</td><td>[-1]</td></tr></tbody>
</table>


## 🔍입출력 예 설명
입출력 예#1<br/>arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.
입출력 예#2<br/>arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.
입출력 예#3<br/>3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.
---


