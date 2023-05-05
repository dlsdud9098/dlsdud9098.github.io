---
layout: post
title: "동영상 속 인물 변경하기 #6"
categories: [Project, Character Change]
tags: [Python, DL, Stable Diffusion]
---

> 현재 개발중으로 글이 수정될 수 있습니다.(2023.04.28)

## 왜 Lora가 적용되지 않는가?

일단 내가 가지고 온 Lora의 확장자는 ```.safetensor``` 확장자를 가지고 있다.  
하지만 이 diffusers의 패키지는 우리가 쓰는 확장자를 적용할 수 없다.  
커뮤니티에서도 safetensors 확장자를 diffusers에서 사용하는 방법에 대해 많은 의견들이 오갔고, 이런 safetensors 확장자를 diffusers로 변경해 주는 코드가 있는 것을 발견했다.

### safetensors -> diffsuers (1)
처음에는 [이곳](https://towardsdatascience.com/improving-diffusers-package-for-high-quality-image-generation-a50fff04bdd4)에서 글을 발견했다.

글에서는 ```convert_original_stable_diffusion_to_diffuusers.py```라는 파일을 이용했다고 한다.  
하지만 찾아봐도 없어서 깃허브를 들어가보니, 우리가 사용하는 pip 패키지에는 들어가 있지 않았다.

그래서 해당 깃허브를 클론해왔고, ```scripts``` 폴더 안에 파일이 있었다.

그리고 해당 명령어를 입력했다.  
```python convert_original_stable_diffusion_to_diffusers.py --from_safetensors --checkpoint_path="D:\stable-diffusion-webui\models\Stable-diffusion\deliberate_v2.safetensors" --dump_path='D:\sd_models\deliberate_v2' --device='cuda:0'```

하지만 글과는 달리, 제대로 수행되지 않았다.

### safetensors -> diffusers (2)
그래서 다른 [글](https://qiita.com/Limitex/items/275d91dd4acdbf57b5f4)을 찾아보았다.

이곳에서는 기존에 있던 convert_~ .py 파일을 이용하지 않고, 코드로 구현되어있었다.

하지만 코드를 사용하는데, ```pretrained_model_name_or_path='YOUR VAE MODEL PATH'``` 이 부분에서 어떤 것을 써야하는지 알 수 없었다.

### safetensors -> diffusers (3)

[다른 글](https://github.com/haofanwang/Lora-for-Diffusers)도 들어가 보았다.

이곳은 첫 번째랑 똑같이 ```conveert_original_stable_diffusion_to_diffusers.py```파일을 이용했다.  
이곳에서 하는 대로 깃을 클론하고, 명령어를 입력했다.

