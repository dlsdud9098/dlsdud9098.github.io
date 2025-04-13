---
layout: post
title: "우분투에서 mcp 사용하기"
category: studylog
tags: ubuntu
---

<br>

## 1. MYSQL-SERVER 설치
```
sudo apt-get install mysql-server
```

## 2. MYSQL 기본 설정
(안하면 나중에 MySQL Workbench를 사용할 때 오류가 난다고 한다.)

```bash
# 규칙 설정
sudo ufw allow mysql

# MYSQL 시작
sudo systemctl start mysql

# ubuntu 시작시 MYSQL 시작
sudo systemctl enable mysql

# MYSQL 접속
sudo /usr/bin/mysql -u root -p
```

## 3. 사용자 정보 확인
```mysql
SELECT User, Host, authentication_string FROM mysql.user;
```

![](https://velog.velcdn.com/images/dlsdud9098/post/bf5d5cb5-549e-44a4-b2e3-0c707b75b46a/image.png)

## 4. 데이터베이스 만들기
```mysql
# 데이터베이스 만들기
CREATE DATABASE TESTDB;

# 데이터베이스 확인
SHOW DATABASES;
```
![](https://velog.velcdn.com/images/dlsdud9098/post/0eb64134-c722-4522-930b-eb2dc8c5a3e3/image.png)

## 5. 계정 만들기
```mysql
CREATE USER '계정이름'@'localhost' IDENTIFIED BY 'mysql비번';
ex) CREATE USER 'Apic'@'localhost' IDENTIFIED BY '0000';

FLUSH PRIVILEGES;

# 계정 확인
SELECT User, Host, authentication_string FROM mysql.user;
```

## 6. 데이터베이스를 사용할 계정에 권한 부여
```mysql
GRANT ALL PRIVILEGES ON 데이터베이스이름.* TO '계정이름'@'localhost';

FLUSH PRIVILEGES;
```mcp가 핫하다길래 사용해 보려고 한다.

https://github.com/aaddrick/claude-desktop-debian

여기에 들어가서 설치 방법을 따라해준다.

```bash
# Clone this repository
git clone https://github.com/aaddrick/claude-desktop-debian.git
cd claude-desktop-debian

# Build the package (Defaults to .deb and cleans build files)
./build.sh

# Example: Build an AppImage and keep intermediate files
./build.sh --build appimage --clean no

# Example: Build a .deb (explicitly) and clean intermediate files (default)
./build.sh --build deb --clean yes

# Replace VERSION and ARCHITECTURE with the actual values from the filename
sudo dpkg -i ./claude-desktop_VERSION_ARCHITECTURE.deb 

# If you encounter dependency issues, run:
sudo apt --fix-broken install 
```


설치를 하면 

![](https://velog.velcdn.com/images/dlsdud9098/post/1c5b9e4e-cf0c-4245-a9cc-51455a1f6af3/image.png)

이렇게 앱이 생긴다.

이제 코드를 작성해준다.

프로그램을 실행하고 왼쪽 상단의 메뉴 - 설정으로 들어간다.

![](https://velog.velcdn.com/images/dlsdud9098/post/67315b5b-5975-4786-8f55-e053592637a0/image.png)

그리고 개발자 탭으로 가면 이렇게 뜨는데 여기서 설정 편집을 눌러준다.

![](https://velog.velcdn.com/images/dlsdud9098/post/9853e8a9-3c30-4b16-ac21-67546e16d06d/image.png)

그러면 이렇게 폴더 창이 하나 뜨는데 여기서 ```claude_desktop_config.json``` 파일을 수정해준다.

해당 파일을 vsocde에서 보면

![](https://velog.velcdn.com/images/dlsdud9098/post/bcc0b629-960a-4847-be30-8d7b7d7f00f5/image.png)

이렇게 빈 공간으로 나올텐데

```json
{
    "mcpServers": {
        "tutorial_1": {
            "command": "python",
            "args": [
                "/home/apic/python/temp/mcp_temp.py"
            ]
        }
    }
}
```

이런식으로 적으면 된다.

여기서 tutorial_1은 나중에 파이썬 코드에서 적을 이름이고,
command는 python의 위치.
args는 내가 적은 파이썬 코드 위치다.

이제 파이썬 코드를 적어준다.

파이썬 코드를 적을 위치는 위에 args에 적은 경로에 만들면 된다.

```python

from mcp.server.fastmcp import FastMCP

# MCP 서버 생성
mcp = FastMCP(name="tutorial_1", host="127.0.0.1", port=5000, timeout=30)


# 간단한 에코 도구
@mcp.tool()
def echo(message: str) -> str:
    return message + " 라는 메시지가 입력되었습니다. 안찍어 볼 수 없죠! hello world!"


# 서버 실행
if __name__ == "__main__":
    mcp.run()
```

이렇게 적으면 된다.
```FastMcp(name=[이름])``` 여기다가 json 파일에서 적은 이름을 똑같게 적으면 된다.
만약 ```FastMcp(name="demo", host="127.0.0.1", port=5000, timeout=30)``` 이런식으로 적었다면, json 파일에는

```json
{
    "mcpServers": {
        "demo": {
            "command": "python",
            "args": [
                "/home/apic/python/temp/mcp_temp.py"
            ]
        }
    }
}
```
이렇게 turorial_1 대신에 demo를 넣으면 된다.

이 상태에서 claude를 껏다가 다시 실행하면

![](https://velog.velcdn.com/images/dlsdud9098/post/a41c5806-17ff-4275-b902-17093f8e38b0/image.png)

이렇게 망치 모양이 나오게 된다.

만약 아래 사진처럼 오류가 난다면

![](https://velog.velcdn.com/images/dlsdud9098/post/452534d6-d2ed-4a66-a231-4aac0deb07b0/image.png)

python의 경로가 잘못됬다는 의미다.

나 같은 경우에는 conda 가상환경을 사용해서 기본 python에는 mcp 모듈이 설치되어있지 않는데, 그것 때문에 오류가 났다.

요는 python에 mcp 모듈이 없어서 생기는 문제다.

위에 json 파일에 적은 python을 conda 가상환경의 python 경로로 바꿔주면 해결된다.