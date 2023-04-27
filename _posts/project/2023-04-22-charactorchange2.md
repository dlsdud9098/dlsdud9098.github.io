---
layout: post
title: "동영상 속 인물 변경하기 #2"
categories: [Project, Character Change]
tags: [Python, DL, Stable Diffusion]
---

> 현재 개발중으로 글이 수정될 수 있습니다.(2023.04.22)

## Stable Diffusion Webui 설치

먼저 내가 원하는 이미지를 만들어야 한다.  
설치 방법은 [여기](https://flatsun.tistory.com/3573)에 있다.

설치하고 나서 폴더의 **webui-user.bat** 파일을 우클릭->편집에 들어가

**set COMMANDLINE_ARGS=** 뒤에 **--autolaunch**, **--xformers** 이 두개를 추가해 준다.

- --autolaunch: 웹 페이지를 자동으로 실행해줌
- --xformers: 메모리를 덜 쓰고, 속도를 증가시킨다.

## 이미지 생성

이제 내가 원하는 그림체의 캐릭터를 생성해야 한다.  
그림체를 생성하는데에는 두가지가 필요하다.

* checkpoint 
  * 일종의 그림체라고 할 수 있다.
* Lora
  * 특정 인물 또는 형태

동영상(한 명)에서 계속해서 같은 인물이 나오듯이, 캐릭터도 같은 캐릭터가 계속 나와야 한다.  
그렇기 때문에 특히 Lora는 반 필수적이라고 할 수 있다.  

checkpoint와 lora의 모델들은 [Civitai](https://civitai.com/)에서 구할 수 있다.

![](/assets/img/content_imgs/stable3.PNG){: .align-center}
*Civitai 홈페이지*

오른쪽 필터에서 원하는 것들을 선택하여 볼 수 있다.

나는 저기서  
[meinapastel](https://civitai.com/models/11866/meinapastel) |  [standing-full-body-with-background-style-lora](https://civitai.com/models/16997/standing-full-body-with-background-style-lora)  
이 두 모델을 사용했다.

넣는 폴더는

> ./models/Stable-diffusion  
> ./models/Lora  

에 각각 checkpoint와 lora를 넣으면 된다.

## 이미지 생성 종류

이미지 생성에는 여러가지가 있지만 크게 두 가지를 사용한다.  
1. txt2img: 내가 쓴 프롬프트에 맞춰 이미지를 생성한다.
2. img2img: 만들어져있는 이미지에 추가 Controlnet, 추가 프롬프트를 넣어 비슷하지만 새로운 이미지를 생성한다.

처음에는 txt2img로 내가 원하는 이미지를 생성한다.  
이때, 앞서 말했듯이, 캐릭터가 일정해야 하기 때문에 프롬프트를 되도록 정확하게, 많이 적는 편이 좋다.  

예를 들어, 이미지에는 성인 여성 1명, 티셔츠에, 청바지를 입고 있는 이미지를 원한다면 그에 맞는 프롬프트를 넣어주면 된다.  
되도록 자세하게 해야 여러 장의 이미지를 뽑더라도 같은 이미지의 다른 배경으로 나온다.

그리고 프롬프트에 준비한 Lora를 넣어줘야 한다.  
오른쪽에 **Generate** 버튼 밑에 이런 버튼들이 있다.

![](/assets/img/content_imgs/stable4.PNG){: .align-center}
*추가 버튼들*

이 버튼들에서 오른쪽 3개를 가장 많이 사용한다.  
* 🎴 : Negative Prompt 밑에 여러 설정들을 선택할 수 있는 창이 나온다. 로라도 여기서 선택한다.
* 📋 : 저장한 프롬프트를 불러온다. 기존에 프롬프트가 있다면 그 뒤에 덧붙여진다.
* 💾 : 작성한 프롬프트를 저장한다. 만약 저장했는데 안보인다면 그 오른쪽에 Refresh 버튼을 누르면 나온다.

## 프롬프트 작성

보다 정확하고 일정한 그림을 얻기 위해서는 적절한 프롬프트를 작성해야 한다.  
각각 프롬프트에 자주 들어가는 단어들이 있다.
```
Positive Prompt
masterpiece, best quality, ultra-detailed, higres, 8k, UHD, detailed face, intricate details, detailed lighting 등등...

Negative Prompt
canvas frame, cartoon, 3d, too many fingers, bad art, extra limbs, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, ugly, long neck 등등..
```

그리고 단어들마다 가중치를 부여할 수 있는데, 단어를 ```()```로 감싸고, 숫자를 적어주면 가중치가 부여되어 더 강하게 들어간다.
> ex) (masterpiece:1.4)  
> 그리고 1.5 이상으로는 크게 의미가 없다는 말이 있다. 오히려 더 안좋아 질 수 있다는 말이 있어 되도록 1.4까지 올리도록 하자.

## 기타 설정

전부 설정하고 밑을 보면

![](/assets/img/content_imgs/stable5.PNG)

이런 설정들이 있다.  
자주 사용하는 설정들로 보자.

* Sampling method: 샘플링 하는 방법, 각 종류마다 걸리는 시간, 그림 등등이 다르다고 한다.
* Sampling steps: 몇 단계로 그림을 생성할 것인가. 높을 수록 단계가 많아서 정교하다고 하지만 그만큼 시간도 오래걸리며 일정 이상으로는 변화가 없다고 한다. 그렇기에 보통 20~30 정도로 두고 사용한다고 한다.
* Width: 출력되는 그림의 가로 길이.
* Height: 출력되는 그림의 세로 길이.
* CFG Scale: 프롬프트 영향력. 높을 수록 프롬프트와 가깝게 그림을 만들어 준다. 하지만 너무 높으면 그림이 아예 안나올 수도 있으니, 7~9 사이로 사용하자.
* Batch count: 한 번에 그림을 몇 장 뽑을 것 인가.
* Batch size: 몇 번 할 것인가. Batch count를 100, Batch size를 4로 둔다면 100*4 총 400 장의 이미지를 뽑게 된다.
* Seed: 그림 번호. -1은 랜덤이며, 특정 숫자를 넣으면 같은 사진만 나온다.

이렇게 설정을 두고 뽑으면 옆에서 그림이 생성된다.  
생성된 그림은 자동으로 저장되며, 위치는 ```./outputs/txt2img-images-오늘 날짜```에 저장된다.

