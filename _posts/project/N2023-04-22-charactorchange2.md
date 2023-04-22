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