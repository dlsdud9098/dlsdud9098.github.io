---
layout: post
title: "동영상 속 인물 변경하기 #2"
categories: [Project, Character Change]
tags: [Python, DL, Stable Diffusion]
---

> 현재 개발중으로 글이 수정될 수 있습니다.

## Stable Diffusion Webui

먼저 내가 원하는 이미지를 만들어야 한다.  
설치 방법은 [여기](https://flatsun.tistory.com/3573)에 있다.

설치하고 나서 폴더의 **webui-user.bat** 파일을 우클릭->편집에 들어가

**set COMMANDLINE_ARGS=** 뒤에 **--autolaunch**, **--xformers** 이 두개를 추가해 준다.

- --autolaunch: 웹 페이지를 자동으로 실행해줌
- --xformers: 메모리를 덜 쓰고, 속도를 증가시킨다.

그리고 내가 원하는 그림체의 캐릭터를 생성해야 한다.  
그림체를 생성하는데에는 두가지가 필요하다.

* checkpoint 
  * 일종의 그림체라고 할 수 있다.
* Lora
  * 특정 인물 또는 형태

동영상(한 명)에서 계속해서 같은 인물이 나오듯이, 캐릭터도 같은 캐릭터가 계속 나와야 한다.