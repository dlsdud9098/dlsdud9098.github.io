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

### 동영상 이미지로 바꾸기

먼저 동영상을 불러온다.
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

