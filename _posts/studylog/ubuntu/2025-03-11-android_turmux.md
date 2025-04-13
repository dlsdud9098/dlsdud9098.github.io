---
layout: post
title: "우분투 MYSQL 설치"
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
```