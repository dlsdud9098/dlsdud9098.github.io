---
layout: post
title: "YES24 Ebook pdf로 만들기(오토캡쳐 매크로)"
categories: [Coding, Python]
tags: [python]
---

# 개요

영어 공부좀 하려고 이지라이팅을 샀는데 ebook이 처음인지라 pdf로 안나오는걸 몰랐다.  
처음에는 그냥 안되네? 하고 뷰어를 설치해서 뷰어로 공부하려고 했으나...

쓰레기다.

진짜 쓰레기다.

마법처럼 공부 의욕을 잠재운다.  
그래서 pdf화 하는 방법을 찾아봤다.  
일단 다운로드 목록을 보니

![](https://blog.kakaocdn.net/dn/cdeOyX/btrJBKsvO0r/5z063s3n7qKs1YaOXQ36x0/img.jpg)

어? pdf가 있네? 하고 열었는데

![](https://blog.kakaocdn.net/dn/dJ2vYj/btrJAdCHjYk/hLP5rPgiJFqfRgGE1Ah9s0/img.jpg)

역시 안열린다.

이것 저것 찾아보니 drm으로 보호되어있다고 한다.  
그럼 몇 몇 작업을 해야하는데 그건 너무 힘들다.

그리고 좀 더 찾아봤는데 pdf를 캡쳐해서 하는 방법을 주로 많이 쓰는거 같다.  
내가 볼때는 크게 두가지였는데,  
하나는 아이패드로 하나하나 캡쳐하는 것이고  
다른 하나는 오토캡쳐로 하는 방법이다.

그래서 나도 오토캡쳐(사실상 오토마우스)를 통해 찍었다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5bW52KbQuvk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

이 영상을 참고해서 만들었다.

방법은 간단하다.

# SCRCPY 설치

[출저](https://github.com/Genymobile/scrcpy/releases)  
[파일 다운로드](/assets/files/scrcpy-win64-v1.24.zip)

이건 우리 안드로이드를 pc로 미러링 해주는 프로그램이다.  
다른 미러링 방법이 있다면 그걸로 해도 좋을 것이다.  
(나는 영상에서 이 프로그램을 사용했기에 똑같이 사용했다.)  
그 전에 스마트폰(태블릿) 개발자 모드를 켜야한다.

# 캡쳐 프로그램

나같은 경우는 옛날에 반디캠을 구매했기 때문에 [반디캠](https://www.bandicam.co.kr/)을 사용했다.  
영상에서는 [Scapture](https://www.smemo.co.kr/scapture/index.html) 프로그램을 사용했다.

# 좌표 프로그램

이 방법은 오토마우스를 이용한 오토캡쳐다.  
그래서 캡쳐 버튼이 있는 곳의 좌표를 알아야 하는데 이때 사용한다.  
사용 프로그램은 XY2010_Rev2다.  
[마우스 좌표 추적기 다운로드](https://xsylphid.tistory.com/6)

# 오토캡쳐 코드 짜기

이때 궁금증이 생긴다.  
어차피 오토마우스로 해서 캡쳐하는거면 오토마우스 프로그램 쓰면 되는거 아닌가?  
내가 알기로 오토마우스는 다른창으로 넘어가면 멈춘다.  
(내가 썼던 오토마우스는 그랬다.)  

그래서 그냥 코드 짰다.  
코드같은 경우는 저 위에 영상 주인분이 따로 코드를 안 올렸기에 나도 안올린다.  
(자세히 보면 코드 보이니까 따라 써라 하지만 어느정도 코드를 바꿔줘야 한다.)

# 모니터 세로로 쓰기

갑자기 모니터는 왜? 라고 할 수 있는데 두가지 이유가 있다.

1. 처음에는 가로로 눕혀서 찍었는데 생각보다 화질이 떨어졌다.

   나는 갤탭s8울트라(14.6)라는 거대한 화면으로 봐서 그런지, 화질이 다소 떯어지는 느낌을 받았다.

   (참고로 나는 27인치 모니터를 사용하고 있다.)

2. 책이 전체화면으로 커지면 까맣게 변한다.

   그래서 세로로 바꾸로 전체 화면으로 한 다음 캡쳐했다.

   ![](https://blog.kakaocdn.net/dn/4oeEc/btrJA3sBNJw/TgLlwZtlO40VKLzj0X6qP0/img.jpg)

   이건 내가 전체화면을 하기 전

   ![](https://blog.kakaocdn.net/dn/kThBc/btrJB2TZSzw/nx5lgWNJsIT4ZhxOBQgMz0/img.jpg)

   전체화면으로 하면(위 아래의 도구 없애기) 이렇게 까맣게 변하는 상황을 볼 수 있다.  
   처음에는 왜 이러지 하면서 짜증났는데 내가 27인치라서 그런지 세로로 돌리고 도구모음을 부른 상태로 해도 잘 되었다.  
   그래서 그냥 두고 캡쳐했다.  
   참고로 캡쳐할 때 양면이 아닌 한면으로 하는걸 추천한다.

# pdf로 압축

[프로그램 다운로드](http://www.ezpdf.co.kr/main/downPage/downPage.jsp)

이걸 사용했다.  
저렇게 pdf 병합을 해주면 완성.  
결과물을 보니 괜찮게 나왔다.  
14.6인치로 보거나 공부할때 불편하지 않았다.  
앞으로 ebook사면 계속 이렇게 해서 pdf로 만들거 같다.