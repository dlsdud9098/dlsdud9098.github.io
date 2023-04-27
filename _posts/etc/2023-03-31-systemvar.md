---
layout: post
title: 환경변수 바로 적용하기
categories: [Coding, Python]
tags: [python]
---
<br>

본래 환경변수를 추가하면 재부팅하는 것이 국룰이지만, 아래 명령어를 통해 재부팅 없어 적용할 수 있다.

명령 프롬프트(cmd) 열고

```taskkill /f /im explorer.exe```
```explorer.exe```

이 두개를 치면 탐색기 폴더가 모두 사라지고 다시 실행되면서 환경 변수가 적용된다.