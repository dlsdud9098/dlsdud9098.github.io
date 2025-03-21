---
layout: post
title: "파이썬 패키지 한 번에 삭제하기"
category: studylog
tags: python
---


```bash
(obfuscation_korean_venv) apic@apic:~/python/dacon_project/obfuscation_korean$ pip list
Package                  Version
------------------------ -----------
accelerate               0.34.0
aiohappyeyeballs         2.4.6
aiohttp                  3.11.12
aiosignal                1.3.2
asttokens                3.0.0
attrs                    25.1.0
bitsandbytes             0.45.2
blessed                  1.20.0
certifi                  2025.1.31
charset-normalizer       3.4.1
colorama                 0.4.6
comm                     0.2.2
datasets                 2.17.0
debugpy                  1.8.12
decorator                5.2.0
dill                     0.3.8
docstring_parser         0.16
exceptiongroup           1.2.2
executing                2.1.0
filelock                 3.17.0
frozenlist               1.5.0
fsspec                   2023.10.0
huggingface-hub          0.29.1
idna                     3.10
importlib_metadata       8.6.1
ipykernel                6.29.5
ipython                  8.32.0
jedi                     0.19.2
Jinja2                   3.1.5
jupyter_client           8.6.3
jupyter_core             5.7.2
markdown-it-py           3.0.0
MarkupSafe               3.0.2
matplotlib-inline        0.1.7
mdurl                    0.1.2
mpmath                   1.3.0
multidict                6.1.0
multiprocess             0.70.16
nest_asyncio             1.6.0
networkx                 3.4.2
numpy                    2.2.3
nvidia-cublas-cu12       12.4.5.8
nvidia-cuda-cupti-cu12   12.4.127
nvidia-cuda-nvrtc-cu12   12.4.127
nvidia-cuda-runtime-cu12 12.4.127
nvidia-cudnn-cu12        9.1.0.70
nvidia-cufft-cu12        11.2.1.3
nvidia-curand-cu12       10.3.5.147
nvidia-cusolver-cu12     11.6.1.9
nvidia-cusparse-cu12     12.3.1.170
nvidia-cusparselt-cu12   0.6.2
nvidia-nccl-cu12         2.21.5
nvidia-nvjitlink-cu12    12.4.127
nvidia-nvtx-cu12         12.4.127
packaging                24.2
pandas                   2.2.3
parso                    0.8.4
peft                     0.8.2
pexpect                  4.9.0
pickleshare              0.7.5
pip                      25.0.1
platformdirs             4.3.6
prompt_toolkit           3.0.50
propcache                0.3.0
psutil                   6.1.1
ptyprocess               0.7.0
pure_eval                0.2.3
pyarrow                  19.0.1
pyarrow-hotfix           0.6
Pygments                 2.19.1
python-dateutil          2.9.0.post0
pytz                     2025.1
PyYAML                   6.0.2
pyzmq                    26.2.1
readchar                 4.2.1
regex                    2024.11.6
requests                 2.32.3
revel                    0.9.1
rich                     13.9.4
safetensors              0.5.2
setuptools               75.8.0
shtab                    1.7.1
six                      1.17.0
stack_data               0.6.3
sympy                    1.13.1
tokenizers               0.21.0
torch                    2.6.0
tornado                  6.4.2
tqdm                     4.67.1
traitlets                5.14.3
transformers             4.49.0
triton                   3.2.0
trl                      0.15.1
typeguard                4.4.2
typing_extensions        4.12.2
tyro                     0.9.16
tzdata                   2025.1
u                        1.0
urllib3                  2.3.0
wcwidth                  0.2.13
wheel                    0.45.1
xxhash                   3.5.0
yarl                     1.18.3
zipp                     3.21.0
```

### 삭제 방법
```bash
# 패키지 목록 저장
pip freeze > requirements.txt

# 저장된 패키지 목록 삭제
pip uninstall -r requirements.txt -y

# 목록 파일 삭제
rm requirements.txt
```

### 결과
```bash
(obfuscation_korean_venv) apic@apic:~/python/dacon_project/obfuscation_korean$ pip list
Package    Version
---------- -------
pip        25.0.1
setuptools 75.8.0
wheel      0.45.1
```