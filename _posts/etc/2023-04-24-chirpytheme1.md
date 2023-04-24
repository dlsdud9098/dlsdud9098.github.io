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

만약 파일이 없다면, [여기](https://github.com/cotes2020/jekyll-theme-chirpy)에 들어가 **_include**를 다운받아 폴더에 넣어주면 된다.

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

![](/assets/img/content_imgs/chirpytheme2.PNG)

이렇게 잘 들어가는 것을 확인 할 수 있다.

## 문제 발생

하지만 이 기능을 사용하는데 몇가지 문제점이 발생했다.

1. 조회수 위치가 이상함

    깃허브 블로그에 들어가 보면, 아래 사진과 같이 밑으로 가지 않고 옆에 **ABOUT**과 같은 공간을 사용하고 있다.

    ![](/assets/img/content_imgs/chirpytheme3.PNG)

    text-align:center가 제대로 적용되지 않은것 같다.

    수정하고 다시 실행 해 보니,

    ![](/assets/img/content_imgs/chirpytheme4.PNG)

    밑으로 내려갔지만, 여전히 문제가 있다.

2. 조회수
    뭐 위치는 그렇다고 치자.  
    하지만 조회수를 산정하는 방식이 문제다.

    홈페이지 위치에 관계 없이, 이용자 관계없이 ```https://dlsdud9098.github.io``` 페이지에 들어오면, 자동으로 1이 상승하며, 새로고침을 해도 상승한다.

    다른 게시판에 들어가도 상승하며, 뒤로 가기해도 상승한다.

    아주 근본적인 문제가 있는 것이다.

이렇게 되니, 생각보다 간단하지 않고, 뭔가 이것 저것 설정해야 하는 것이 많은 것 같다.

그냥 구글 애널리틱스나 써야겠다.