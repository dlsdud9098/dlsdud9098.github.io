---
layout: post
title: "모바일(안드로이드)에서 파이썬 코딩하기(termux)"
category: studylog
tags: others_post
---

<br>

## 1. 시작

먼저 나는 [vscode.dev](vscode.dev)를 통해 개발하려고 사이트에 들어갔다.
하지만 따로 jupyter 서버를 연결하던가 codespace를 위해 돈을 내야 한다.

<p align="center" style="color:gray">
  <!-- 마진은 위아래만 조절하는 것이 정신건강에 좋을 듯 하다. 이미지가 커지면 깨지는 경우가 있는 듯 하다.-->
  <img style="margin:50px 0 10px 0" src="https://velog.velcdn.com/images/dlsdud9098/post/60694807-8be1-4bc5-b1f7-95d225ce297c/image.png"/>
  모바일에서 vscode.dev에 접속에 파이썬 코드를 실행시킬 때 커널 선택 창에는 2가지 방법만 나온다.
</p> 


이러한 문제를 해결하기 위해 방법을 찾던 도중, termux를 통해 우분투를 설치하고 거기에 code server를 설치하여 jupyter 서버를 열듯 사용 할 수 있다는 것을 알았다.

## 2. 환경

사용 기기: Samsung Galaxy S8 Ultra

## 3. termux 설치
먼저 안드로이드에 우분투를 설치하기 위해 termux를 설치해야 한다.
구글 플레이 스토어에도 termux가 있지만 이것으로 했을 때는 잘 되지 않았다.

다른 포스팅에서도 플레이스토에서 다운로드 하지 않고 깃허브에 있는 [termux-app](https://github.com/termux/termux-app/releases)를 사용했다.

![](https://velog.velcdn.com/images/dlsdud9098/post/c48f93bd-f289-424a-8219-d11f5c1dc3a5/image.png)

## 4. 우분투 설치

### 4-1. 설치 전 termux 업데이트
먼저 업데이터를 해준다.

```bash
pkg update && pkg upgrade -y
```

중간에 **bash.bashrc (Y/I/N/O/D/Z) \[default=N]?** 이라는 문구가 나온다.
전부 y 해주면 된다.

![](https://velog.velcdn.com/images/dlsdud9098/post/c1d8a3b3-6f31-412b-843b-dd40dbddfbc6/image.jpg)

그 다음 우분투를 설치하기 위한 proot-distro를 설치해 준다.

```bash
pkg install proot-distro
```

```bash
-- 설치할 수 있는 OS 리스트를 나타내는 것 같다.
proot-distro list
```
![](https://velog.velcdn.com/images/dlsdud9098/post/240c574c-91bf-49d2-8246-ee7b7ff0de9c/image.jpg)


이제 우분투를 설치하자

### 4-2. 본격적으로 우분투 설치
```bash
-- 우분투 설치
proot-distro ubuntu
```

![](https://velog.velcdn.com/images/dlsdud9098/post/8673f109-1be9-47c8-bdac-1d78991c76d1/image.png)

그러면 이렇게 ubuntu가 설치된다.

이제 **proot-distro login**으로 우분투에 접속한다.
그러면 **root@localhost:~#**으로 우분투에 접속된다.

### 4-3. 업데이트
이후 우분투에서 사용하듯이 업데이트를 해준다.

```bash
apt update && apt upgrade -y
```

### 4-4. vim 설치
그 다음 vim을 설치했다.

```bash
apt install vim
```

### 4-5. user 만들기
이제 user를 만들어준다.

```bash
adduser {이름}
```
그 다음 비밀 번호를 2번 입력해 주고
다른 기타 정보들도 입력해 준다.

![](https://velog.velcdn.com/images/dlsdud9098/post/c6a6adf6-b1c0-40e5-8ee9-b759c1183207/image.png)

그리고 sudo를 설치해 준다.
![](https://velog.velcdn.com/images/dlsdud9098/post/6329f96e-e89e-4216-8aa2-4c10f361f7f3/image.png)

다음 파일을 수정한다.

```bash
vim /etc/sudoers
```

![](https://velog.velcdn.com/images/dlsdud9098/post/e8647ab3-7768-4a98-bc63-b022639c36e1/image.jpg)

다음 저렇게
**{이름} ALL=(ALL:ALL) ALL**를 추가하고 저장한다.

다음에 **su {이름}**을 하면 (이름은 위에서 정한 user 이름)
![](https://velog.velcdn.com/images/dlsdud9098/post/0723512b-ca6f-4496-9525-9e498bb07c7c/image.png)
이렇게 접속할 수 있다.

**저 상태에서 code-server를 설치하려고 했는데 문제가 발생해서 다시 root 계정으로 되돌아와 설치했다.**

### 4-6. code-server 설치

[code-server](https://github.com/coder/code-server/releases/tag/v4.97.2)


<p align="center" style="color:gray">
  <!-- 마진은 위아래만 조절하는 것이 정신건강에 좋을 듯 하다. 이미지가 커지면 깨지는 경우가 있는 듯 하다.-->
  <img style="margin:50px 0 10px 0" src="https://velog.velcdn.com/images/dlsdud9098/post/37700ae8-538f-450d-8928-e103a164fe90/image.png"/>
  바로 위에 있는 파일과 이름과 용량이 같은데 위에 것으로 했을 때는 안됐다....
</p> 


```bash
apt install wget

-- code-server 설치
wget https://github.com/coder/code-server/releases/download/v4.97.2/code-server-4.97.2-linux-amd64.tar.gz
```
![](https://velog.velcdn.com/images/dlsdud9098/post/192532b9-6b8e-4b06-a5eb-512a6769a23f/image.png)

그리고 압축을 풀어주고 code-server를 실행한다.

```bash
-- 압축 풀기
tar -xvf ./code_server-4.97.2-linux-amd64.tar.gz

-- 폴더 이동
cd code-server-4.97.2-linux-arm64/bin/

-- code-server 비밀번호 설정(사이트 접속할 때 필요)
export PASSWORD="1234"

-- code-server 실행
./code-server
```

![](https://velog.velcdn.com/images/dlsdud9098/post/2eb7345b-8d97-4cee-82dc-ce5dd5b861f7/image.png)

이렇게 하고 로그에 나오는 주소 **http://127.0.0.1:8080**에 접속하면

![](https://velog.velcdn.com/images/dlsdud9098/post/34346d64-f059-4e6f-88d9-d183daa43cd5/image.png)
이렇게 나온다.

아까 작성한 비밀번호 **1234**를 입력하고 접속하면

![](https://velog.velcdn.com/images/dlsdud9098/post/117fb3b7-97b3-4135-9360-3b557bf0ab18/image.png)
이렇게 vscode.dev 처럼 인터넷에서 vscode를 사용할 수 있다!



## 5. vscode 사용하기
vscode에 접속하고 폴더를 열어보면 root 폴더에 들어가 있다.
여기서 대충 폴더 하나 만들고 jupyter 파일도 하나 만들어서 실행시키려고 하면

![](https://velog.velcdn.com/images/dlsdud9098/post/c09fe4c0-5a25-444a-b815-f091b8768dec/image.png)
이렇게 나온다.

여기서 python과 jupyuter를 설치하면

![](https://velog.velcdn.com/images/dlsdud9098/post/1da1bc4a-d9c3-4f53-ac6d-0627f0857c12/image.png)
이렇게 python을 선택할 수 있고 커널을 선택하여 실행시켜 보면

![](https://velog.velcdn.com/images/dlsdud9098/post/a668fbaf-8001-4d9d-ac1b-7b25db62bda4/image.png)
pip가 없다고 나온다.

아마 vscode에서 설치되는 것은 최소한만 설치되는 것 같다.
(그냥 python 파일을 만들어서 실행하면 정상적으로 작동된다. 아마 pip에서 문제가 생긴듯 하다.)

터미널에서 파이썬을 설치해주자.
(나는 서버 끄기 귀찮아서 vscode의 터미널을 활용했다.)

```bash
apt install python3 python3-pip python3-venv
```

이후 다시 실행했는데 계속 오류가 떠서 강제로 설치했다.

```bash
python3 -m pip install ipykernel --break-system-packages
```

![](https://velog.velcdn.com/images/dlsdud9098/post/d2a866de-222a-4284-ac65-7c0e85f5b80f/image.png)
하지만 그래도 오류가 떴다.

몇가지 방법을 시도했지만 계속 저 오류에서 문제가 생겼다.

일단 가상환경을 사용함으로써 pip 설치가 안되는 문제는 해결됐다.

![](https://velog.velcdn.com/images/dlsdud9098/post/f420efbc-3d81-4a08-8315-2276ea9eb02b/image.png)

이렇게 pandas 패키지도 설치하여 사용할 수 있었다.

참고로 저 사진은 sudo 계정으로 들어가 다시 설치하고 들어가 실행한 상황이다.
sudoers에서 문제가 발생했는데, root 계정에 들어가 /etc/sudoers의 권한을 440으르 설정했더니 정상적으로 작동됐다.(sudo가 안됐었음)

그리고 sudo 계정으로 code-server에 섭속할 때 비밀번호가 틀려서 접속이 안돼는 경우가 있었는데, 이 부분은 처음에 실행할 때 --auth none을 넣어주면 된다.
```bash
sudo ./code-server --auth none
```
--auth가 실행할 때 어떤 방식으로 실행할지(password, none) 정하는 것인데 기본 설정인 password로 하면 우리가 설정한 password(지금은 안돼는)로 접속하고 none으로 하면 로그인 없이 바로 접속된다.

아쉽게도 jupyter는 사용하지 못하지만 파이썬 파일은 정상 작동하니까 그냥 사용하려고 한다.

## 6. 속도 비교
일단 가능은 하니까 속도를 한 번 비교해 보았다.
코드 제공은 chatgpt

PC -> ubuntu 24.04, 19-13900kf, rtx3060, 80GB RAM
MOBILE -> Galaxy S8 Ultra

1. 
```python
import time

def measure_execution_time():
    # 시작 시간
    start_time = time.time()

    # 실행할 코드 (여기서 원하는 코드를 넣으세요)
    result = sum(range(100000000))

    # 종료 시간
    end_time = time.time()

    # 소요된 시간 계산
    return end_time - start_time

# 여러 번 실행하여 평균 시간 계산
num_trials = 10
total_time = 0

for _ in range(num_trials):
    total_time += measure_execution_time()

average_time = total_time / num_trials
print(f"Average Execution Time over {num_trials} trials: {average_time} seconds")
```

pc -> 약 0.4초
mobile -> 약 2초

2.
```python
import time
import numpy as np
import pandas as pd
import random
import string
import os

# 시작 시간 기록
start_time = time.time()

# 1. 대규모 행렬 연산 (NumPy 사용)
def matrix_operations():
    matrix = np.random.rand(1000, 1000)
    result = np.dot(matrix, matrix)
    return result

# 2. 대량의 파일 입출력
def file_operations():
    directory = 'test_files'
    if not os.path.exists(directory):
        os.mkdir(directory)
    
    # 파일 쓰기
    for i in range(1000):
        with open(f'{directory}/file_{i}.txt', 'w') as f:
            f.write(''.join(random.choices(string.ascii_letters + string.digits, k=1000)))
    
    # 파일 읽기
    files = os.listdir(directory)
    for file in files:
        with open(f'{directory}/{file}', 'r') as f:
            f.read()
    
    # 임시 파일 삭제
    for file in files:
        os.remove(f'{directory}/{file}')
    os.rmdir(directory)

# 3. 데이터프레임 연산 (Pandas 사용)
def dataframe_operations():
    df = pd.DataFrame({
        'A': np.random.rand(100000),
        'B': np.random.rand(100000),
        'C': np.random.rand(100000),
    })
    result = df['A'] + df['B'] * df['C']
    return result

# 4. 정렬 및 검색
def sorting_searching():
    random_list = random.sample(range(1, 1000000), 100000)
    sorted_list = sorted(random_list)
    return sorted_list.index(random.choice(sorted_list))

# 5. 대규모 숫자 계산
def complex_math_operations():
    result = 0
    for i in range(1, 100000):
        result += (i ** 2) / (i + 1)
    return result

# 모든 작업 실행
def run_complex_operations():
    matrix_operations()
    file_operations()
    dataframe_operations()
    sorting_searching()
    complex_math_operations()

# 여러 번 실행하여 평균 시간 측정
num_trials = 3
total_time = 0

for _ in range(num_trials):
    run_complex_operations()

end_time = time.time()
execution_time = end_time - start_time


print(f"Total Execution Time: {execution_time:.2f} seconds")
```
pc -> 약 0.46초
mobile -> 약 3.91초

대충 2배에서 3배정도 차이가 나는데 이정도면 대단한건 못하더라도, 알고리즘 공부할 때는 유용할 것 같다.

그리고 나중에 껏다가 키면 다시 로그인 해야하는데
**proot-distro login ubuntu**
이렇게 하면 우분투에 다시 접속하게된다.

## 7. 참고자료
https://www.codewithharry.com/blogpost/install-vs-code-in-android/
https://m.blog.naver.com/wonjinho81/222597996987
https://multitab.tistory.com/266
https://meoru-tech.tistory.com/70