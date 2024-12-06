---
layout: post
title: "vscode 주피터 노트북 삭제된 셀 복구하기"
category: studylog
tags: python, vscode ,jupyter
---


vscode에서 주피터 노트북으로 코드를 작성하는데 왠지는 모르지만 뭘 잘못 눌렀는지 작성중이덴 셀이 삭제되었다.

찾아보면 ```ctrl+z```를 누르라는데 누르는 순간 삭제된 셀이 복구되는게 아니라 기존에 있던 셀이 하나 더 삭제되는 불상사가 일어났다.

![](https://velog.velcdn.com/images/dlsdud9098/post/4c9961f9-e2b4-423a-b868-6fbbdf33c7a2/image.png)

그러니 셀이 삭제되면 `ctrl+z`를 누르지 말고 `ctrl+shift+z`를 누르자

그럼 삭제되었던 셀이 복구된다.

하지만 혹여 모를 불상사를 대비해 먼저 백업 해놓고 해보길 바란다.

