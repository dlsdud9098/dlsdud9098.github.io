---
layout: post
title: "Chirpy 테마 조회수 적용하기"
categories: [Coding, Etc]
tags: [Jekyll, Chirpy Theme]
---


## 시작

블로그에 조회수 기능을 넣고 싶었다.

가장 많이 종류가 크게 2가지가 있다.

1. Google Analytics
   구글에서 주소 넣으면 그 주소에 관련해서 조회수, 유입 경로, 어느 게시글을 들어갔는가 등 정보들이 나옴
2. Hits
    해당 주소가 클릭되면 횟수가 올라감

Google Analytics도 좋지만, 실시간으로 블로그에서 보고 싶어서 Hits를 이용해 보려고 한다.

## Hits

[Hits 주소](https://hits.seeyoufarm.com/)로 들어간다.

![](/assets/img/content_imgs/chirpytheme1.PNG){: .align-center}
*Hits 홈페이지*

홈페이지는 위 사진과 같이 되어있다.

저기서 원하는 색, 모양, 이름 등을 지정하고 밑의 세 가지 중 자신에게 맞는 것을 복사하면 된다.  
(우리는 html로 이루어져 있기 때문에 html을 복사한다.)

그리고 복사한 html을 **sidebar.html** 파일을 열어 밑의 코드를 카테고리 밑에 넣어준다.

## html 수정

```html
<!-- the real tabs -->
{% for tab in site.tabs %}
<li class="nav-item{% if tab.url == page.url %}{{ " active" }}{% endif %}">
    <a href="{{ tab.url | relative_url }}" class="nav-link">
    <i class="fa-fw {{ tab.icon }} ml-xl-3 mr-xl-3 unloaded"></i>
    {% capture tab_name %}{{ tab.url | split: '/' }}{% endcapture %}

    <span>{{ site.data.locales[site.lang].tabs.[tab_name] | default: tab.title | upcase }}</span>
    </a>
</li> <!-- .nav-item -->
{% endfor %}

<div style="text-align: center;">
<a href="https://hits.seeyoufarm.com">
    <style>
    .hits {
        width: auto; height: auto;
        max-width: 99px;
        max-height: 20px;
    }
    </style>
    <img class='hits' src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fdlsdud9098.github.io&count_bg=%23FFB9FF&title_bg=%23B0A6D7&icon=&icon_color=%23000000&title=%EC%A1%B0%ED%9A%8C%EC%88%98&edge_flat=false" alt="Seeyoufarm"/>
</a>
</div>

</ul> <!-- ul.nav.flex-column -->
```

하지만 보면 Hits에서 복사한 내용과 다른데, 이것은 그냥 넣으면 박스 크기가 꽉차는 현상이 발생해, 저렇게 고정해주었다고 한다.

그리고 로컬에서 실행해 보면,

![](/assets/img/content_imgs/circle_list_img2.png)

이렇게 잘 들어가는 것을 확인 할 수 있다.

## 문제 발생

하지만 이것을 넣고 깃허브에 커밋한 다음, 확인해 보면 아래와 같은 현상이 발생한다.

