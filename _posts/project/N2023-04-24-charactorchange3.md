---
layout: post
title: "동영상 속 인물 변경하기 #3"
categories: [Project, Character Change]
tags: [Python, DL, Stable Diffusion]
---

> 현재 개발중으로 글이 수정될 수 있습니다.(2023.04.22)

## Web이 아닌 코드로

사진이 잘 나온것을 확인했다.

하지만 서비스를 위해서는 이것을 코드로 구현해야 한다.

찾아보니 **diffusers**라는 패키지가 존재했고 다운로드 했다.
```bash
pip install diffusers
```

이 **diffusers**는 [Hugging Face](https://huggingface.co/)에 있는 파일로 이미지를 생성할 수 있는 것 같다.

> diffusers에 대한 사용 방법은 [여기](https://huggingface.co/docs/diffusers/v0.15.0/en/index)에 있다.

## 코드로 구현하기

### 시험해 보기

먼저 시험삼아 이미지를 뽑아보자.
```python
from diffusers import StableDiffusionPipeline
# 모델 불러오기
pipe = StableDiffusionPipeline.from_pretrained("Model Name", torch_dtype=torch.float16).to('cuda')
```

모델은 Hugging Face에서 원하는 모델을 검색하고 해당 모델의 이름을 복사해서 넣어준다.  
> ex) dreamlike-art/dreamlike-anime-1.0 

그리고 우리가 WebUI에서 가져온 프롬프트를 넣어준다.

```python
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    num_inference_steps=25,
    width=600,
    height=800
).images[0]

image.save('1111.png', 'png')
```

뽑아보면, 

![](/assets/img/content_imgs/stable6.png){: .align-center display: block margin:auto}
*파이썬 코드로 뽑아본 이미지*

이미지가 잘 출력되는 것을 확인 할 수 있다.

## 동영상 이미지로 바꾸기

나는 사진 한 장을 사용하는 것이 아닌, 동영상을 사용하는 것이기 때문에, 동영상 한 프레임 마다 적용시켜줘야 한다.

그래서 먼저 동영상을 프레임 단위로 분리시켜 줘야 한다.
```python
# 동영상 불러오기
vidcap = cv2.VideoCapture('1234.mp4')
```

그리고 해당 동영상의 총 프레임(추출되는 이미지 수)를 가져온다.  
파일 이름을 지정할 때 사용한다.

```python
# 총 프레임 수
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
```

그리고 이미지를 저장한다.
```python
# 각 프레임을 이미지로 저장하기
success,image = vidcap.read()
count = 0
pbar = tqdm(total=length)
while success:
    cv2.imwrite("./imgs/%06d.jpg" % count, image)
    success,image = vidcap.read()
    count += 1
    pbar.update(1)
pbar.close()
```

## 사진에서 pose, depth 추출

사진에서 인물만 바뀌어야 하기 때문에, 해당 인물의 크기(?)와 포즈가 같아야 한다.

그것을 위해 **ControlNet**의 **depth**와 **openpose**를 이용한다.

### Depth란?

해당 그림의 전체적은 모습과, 깊이감을 알아야 할 때 사용한다.

인물을 바꾸는데는 **Canny**를 사용해도 되지만, 생김새도 바뀌기 때문에 depth로 충분하다고 생각했다.

![](https://blog.kakaocdn.net/dn/bikUui/btr5OQew9Xv/eoVxV24kqxYVWmq3lGhd00/img.jpg){: .align-center width:"600" height:"800" display: block margin:auto}
*https://zzambab98.tistory.com/230*

![](https://blog.kakaocdn.net/dn/dixLUd/btr5ZkkyREm/rMBNvnwli3hgHuOi41okU0/img.jpg){: .align-center width:"512" height:"768" display: block margin:auto}
*https://zzambab98.tistory.com/230*

더 자세한 내용은 [여기](https://flatsun.tistory.com/3632)에서 확인할 수 있다.

### Openpose란?

사진 속 인물에서 포즈를 추출하는 것을 말한다.

포즈를 추출하고 이미지를 넣으면, 같은 포즈의 다른 이미지를 만들 수 있다.

![](https://blog.kakaocdn.net/dn/3llx7/btr4uQG4zjs/kmqiXRhCZAVRJMyEqLMcR1/img.png){: .align-center display: block margin:auto}
*https://huggingface.co/blog/controlnet*

![](https://blog.kakaocdn.net/dn/dtdGmV/btr4xLYUWed/wCI1uRaLy1KyNPOuk8qGBK/img.png){: .align-center display: block margin:auto}
*https://huggingface.co/blog/controlnet*

자세한 내용은 [여기](https://flatsun.tistory.com/3538)에서 확인 할 수 있다.

## 코드로 구현하기

### Pose 가져오기

먼저 ControlNet 모델을 가져온다.
```python
model = OpenposeDetector.from_pretrained("lllyasviel/ControlNet")
```

미리 분리해둔 이미지를 변수에 불러온다.
```python
from diffusers.utils import load_image

img_files = glob('./imgs/*')
img_files.sort()
imgs = [load_image(img) for img in img_files]
```

그리고 모델에 이미지를 넣어주면 된다.

```python
img = model(INPUT)
```

끝!

만약, 포즈에서 손가락, 얼굴까지 가져오고 싶다면, INPUT 뒤에 ```hand_and_face=True```를 넣어주면 된다.

참고로 

### Depth 가져오기

