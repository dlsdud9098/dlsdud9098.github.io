---
layout: post
title: "python -m venv venv error"
categories: [Coding, Python]
tags: [Python, venv, error]
---

## Error

```bash
jmt1234@DESKTOP-QJ50LP1:~/alpaca-lora$ python3.10 -m venv venv
Error: Command '['/home/jmt1234/alpaca-lora/venv/bin/python3.10', '-m', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
```

python 가상환경 만드는 명령어를 수행하는데 오류가 발생했다.  
python, python3.9, python3.10 등 다 안된다.

## 이유

pip 명령등의 실행할 수 있는 파일이 없어서 그렇다고 한다.

## 해결

without-pip 옵션으로 환경 셋팅 후 설치하는 방식으로 진행하면 된다.

```bash
python3 -m venv env --without-pip
source ./env/bin/activate
```

[출저](https://lasel.kr/archives/339)
