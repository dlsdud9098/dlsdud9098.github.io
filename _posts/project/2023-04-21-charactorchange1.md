---
layout: post
title: "동영상 속 인물 변경하기 #1"
categories: [Project, Character Change]
tags: [Python, DL, Stable Diffusion]
---

> 현재 개발 중으로 이후 수정될 수 있습니다.(2023.04.22)

## 개요

이번에는 **Stable Diffusion**으로 이미지를 번경해 보려고 한다.

동영상을 집어넣으면, 동영상에서 인물(한 명)을 내가 원하는 캐릭터르 바꿔주는 것을 목표로 하고 있다.  
(배경은 그대로, 인물만 바꿈)

약 한 달 동안 진행될 예정이다.

* 개발 환경
  * Windows 10, Ubuntu-20.04
  * Python
  * VSCode
  * WebUI, ComfyUI
  * requirements

* 진행 계획
  1. stable_diffusion에서 원하는 사진이 나오도록 프롬프트 제작
  2. 동영상에서 프레임 수 대로 사진 추출
  3. 사진에서 openpose를 적용하여 동작 추출
  4. 사진에서 depth 추출
  5. 준비해둔 프롬프트와 openpose, depth를 합침
  6. 새로 나온 사진을 기존의 영상 프레임 수에 맞게 동영상으로 제작

## stable diffusion webui

stable diffusion을 웹에서 사용할 수 있게끔 만들어진 프로그램이다. 
가장 유명한 ui는 두개가 있는데,  
 [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)과, ComfyUI](https://github.com/comfyanonymous/ComfyUI) 이렇게 두 가지가 있다.  

UI를 사용하는 이유는 단순히 코드로 접근하는 것 보다 보다 쉽게 접근할 수 있다.  
이곳에서 먼저 프롬프트를 만들고, 여러 이미지 실험을 한 뒤에 진행할 예정이다.

### webui와 comfyui의 차이점?

둘 다 사용해 본 입장으로써, 두 개를 비교해 보자면,
* WebUI
  * 모든 것이 GUI로 이루어져 있기 때문에, 사용에 용이하다.
  * 초보자들도 쉽게 접근할 수 있다.
  * 사용성이 편하기 때문에, 여러 확장 프로그램이 많이 있다.
![](/assets/img/content_imgs/stable1.PNG){: .align-center}
*AUTOMATIC1111/WebUI 예시*

<br>

* ComfyUI
  * 내가 하나하나 순서를 지정할 수 있다.
  * 내 입장에서는 이쪽이 더 편하다.
  * 확장성이 WebUI에 비해 작다.
![](/assets/img/content_imgs/stable2.PNG){:. align-center}
*comfyanonyous/ComyUI 예시*

Stable Diffusion를 처음 사용해 보기 때문에, 접근하기 쉬운 WebUI를 사용했다.