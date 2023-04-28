---
layout: post
title: "동영상 속 인물 변경하기 #5"
categories: [Project, Character Change]
tags: [Python, DL, Stable Diffusion]
---

> 현재 개발중으로 글이 수정될 수 있습니다.(2023.04.28)

## MultiControlNet

openpose 하나로는 원본 이미지와 비슷하게 만들기 힘들다.

그럼 다른 controlnet을 추가해야 한다.

기존에 만들어 놓은 depth를 추가해 보려고 한다.

하나의 controlnet을 이용할 때는 ```StableDiffusionControlNetPipeline```을 이용했지만, 이번에는 ```StableDiffusionMultiControlNetPipeline```을 이용한다.

StableDiffusionMultiControlNetPipeline은 기존의 ```pip install diffusers```를 해서 얻은 diffusers 패키지에는 존재하지 않는다.  
~~아마 개발중이라 그런 듯 하다~~

그래서 나는 diffusers의 [github](https://github.com/huggingface/diffusers)에 가서 따로 받은 후 연결했다.

> ```StableDiffusionControlNetPipeline```는  ```diffusers/src/diffusers/example/community/```에 가면 ```stable_diffusion_multi_controlnet.py```라는 파일이 있고 그 파일안에 ```StableDiffusionMultiControlNetPipeline```, ```ControlNetProcessor``` 등의 클래스가 존재한다.

### pipe 및 controlnet 가져오기
```python
pipe = StableDiffusionMultiControlNetPipeline.from_pretrained(
	"runwayml/stable-diffusion-v1-5", safety_checker=None, torch_dtype=torch.float16
).to("cuda")

pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_xformers_memory_efficient_attention()

controlnet_depth = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-depth", torch_dtype=torch.float16).to('cuda')
controlnet_pose = ControlNetModel.from_pretrained("fusing/stable-diffusion-v1-5-controlnet-openpose", torch_dtype=torch.float16).to('cuda')
```

### 이미지 로드

```python
depth_left = load_image('./depth_imgs/output0.png')
pose_right = load_image('./pose_imgs/output0.png')
```

### 이미지 생성

```python
image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        processors=[
            ControlNetProcessor(controlnet_depth, depth_left),
            ControlNetProcessor(controlnet_pose, pose_right),
        ],
        generator=torch.Generator(device="cuda").manual_seed(random.randint(1,100000)),
        num_inference_steps=30,
        width=600,
        height=800,
).images[0]
image.save("pose_left_right.png")
```

### 결과

![](/assets/img/content_imgs/stable15.png)

확실히 openpose 하나만 썼을 때에 비해, 좀 더 정확하게 나왔다.

## 문제점

하지만 가장 큰 문제점이 있는데

**Lora가 적용되지 않았다.**

단순하게 prompt에 넣으면 될 줄 알았는데 전혀 적용되지 않았다.

좀 더 찾아보니, lora의 확장자인 ```.safetensors```는 받지 않는다고 한다.

다시 고생길 시작이다...