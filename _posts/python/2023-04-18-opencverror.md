---
layout: post
title: "opencv 에러"
categories: [Coding, Python]
tags: [python, opencv error]
---

**import cv**를 하고 진행하려고 하는데 오류가 발생했다.

```bash
AttributeError: partially initialized module 'cv2' has no attribute 'gapi_wip_gst_GStreamerPipeline' (most likely due to a circular import)
```

찾아봤을 때, 순환 참조 때문이니
```python
import cv2
from cv2 import some_function
from GStreamerPipeline import some_other_function
```
이런 식으로 순서를 정하라고도 하고
```bash
pip uninstall opencv_contrib_python
pip install opencv_contrib_python
```
이렇게 재설치 하라고도 했으나, 소용없었다.

찾다가 이런 글을 발견했다.

![](/assets/img/content_imgs/opencverror.png)

저기서 하라는 대로 설치 했는데 설치가 됐고, 에러도 뜨지 않는다!

하지만 다른 오류가 발생했다.

```bash
error: OpenCV(3.4.18) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:659: error: (-2:Unspecified error) The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Carbon support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script in function 'cvShowImage'
```

```cv2.imshow()```를 수행하는데 오류가 발생했다.  
그래서 일단 ```cv2.imshow()``` 대신에 ```plt.imshow()```를 사용해 문제를 넘어갔는데, ```cv2.waitkey()```에서도 오류가 발생한 것이다.

