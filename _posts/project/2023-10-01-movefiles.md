---
layout: post
title: "파일을 빠르게 옮겨보자"
categories: [Project, Semi Project]
tags: [Python, PYQT5]
---

## 파일 옮기기

그 동안 쌓아놨던 파일들을 정리하고자 옮기려고 한다.

하지만 파일 크기는 약 400GB, 파일들의 수는 약 56만개...

그냥 옮기고자 하니 시간이 너무 오래걸린다.

생각을 해 봤는데, 파이썬의 멀티 프로세스를 이용하면 더 빨라지지 않을까 생각했고 만들어 보았다.

## 환경 및 계획

* 환경
  - OS: Ubuntu-20.04(wsl)
  - Language: Python
  - Version: 3.10.13
  - Editor: VSCode

* 계획
    1. 원본 위치와 복제할 위치를 설정
    2. 복사, 이동 선택
    3. 내가 원하는 파일만 이동 할 수 있도록 포함 단어 및 정규표현식 설정
    4. 이동하기

## GUI 만들기

GUI를 만들기 위해 파이썬의 PYQT5를 이용했고, 코드로 디자인하기 힘들기 때문에 **desinger**를 이용해서 만들었다.

> desinger는 pyqt5-tools를 pip를 이용하여 설치하면, 콘솔 창에서 desinger를 입력하여 실행할 수 있다.(없다면 pyqt5-tools 설치 폴더로 가서 찾으면 된다.)
> 사용법은 구글로 가자

![](/assets/img/python_semi/move_file_3.png)

이렇게 만들고 코드를 짰다.

## 실행 결과

PYQT5로 GUI를 만들고 복사는 멀티 프로세스를 이용했다.

먼저 윈도우를 했을 때의 속도다

![](/assets/img/python_semi/move_file_5.png)

이정도 인데, 약 1분 정도 걸렸다.

직접 만든 프로그램을 이용했을 땐?

![](/assets/img/python_semi/move_file_2.png)

약 30초로 두 배 정도 빠른 속도를 보였다.

이번에는 더 크고 양이 많은 것을 이동해 보았다.

![](/assets/img/python_semi/move_file_1.png)

252초.

약 4분정도 걸린 시간이다.

윈도우로 봤을 때?

![](/assets/img/python_semi/move_file_4.png)

흠... 한 1분 정도 