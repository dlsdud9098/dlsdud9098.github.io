---
layout: post
title: "정규표현식으로 괄호, 특수문자 제거"
category: studylog
tags: python
---


## 모듈 임포트
```python
import re
```

## 문자열
```python
str = '[] 1234234 AS{@HG(A#T)}DGL !LKDG@(NGLS)ㅁㄴㅇㅎㅅㅂ'
```

출력 결과
[] 1234234 AS{@HG(A#T)}DGL !LKDG@(NGLS)ㅁㄴㅇㅎㅅㅂ

## 대괄호 제거
```python
str = re.sub(r"\s*\[.*?\]", "", str)
```

출력 결과
1234234 AS{@HG(A#T)}DGL !LKDG@(NGLS)ㅁㄴㅇㅎㅅㅂ

## 중괄호 제거
```python
str = re.sub(r"\s*\{.*?\}", "", str)
```

출력 결과
[] 1234234 ASDGL !LKDG@(NGLS)ㅁㄴㅇㅎㅅㅂ

## 소괄호 제거
```python
str = re.sub(r'\([^)]*\)', '', str)
```

출력 결과
[] 1234234 AS{@HG}DGL !LKDG@ㅁㄴㅇㅎㅅㅂ

## 특수문자(.,@!{}()[] 등) 제거
```python
str = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", str)
```

출력 결과
1234234 ASHGATDGL LKDGNGLS