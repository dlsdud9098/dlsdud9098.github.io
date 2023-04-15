---
layout: post
title: Linked List(링크드 리스트)
categories: [Coding, Python]
tags: [Python]
---

<br>

# 📒 Linked-list (연결 리스트)

## 💻 Linked-list란?
링크드 리스트는 배열의 단점을 보완하기 위해 만들어진 자료구조다.

Linked-list 구조
![](https://velog.velcdn.com/images/dlsdud9098/post/4d44a6c0-c9e9-45fa-9569-fdaa8bb37c79/image.png)

head: 첫(시작지점) 노드를 가리키고 있다.
node: 데이터와 다음 데이터를 가리키는 link를 가지고 있다.

Link-list는 다음 노드를 가리키는 link에 NULL을 넣음으로서 끝을 지정할 수 있다.

---
## 💻 노드 생성
```python
# 노드를 만들 수 있는 클래스 생성
class Node:
    def __init__(self):
        self.datat = None
        self.link = None

# head 변수 생성
head = None     
# 노드 생성   
node = Node()
node.data = 10

# head가 시작지점인 node를 가리킴
head = node
```
![](https://velog.velcdn.com/images/dlsdud9098/post/45e6bc6e-d3c5-41eb-be0b-233a6991345e/image.png)

이런식으로 노드가 만들어지고, head는 시작 노드를 가리킨다.

---
## 💻 노드 삽입

노드를 삽입하는데 3가지 경우가 있다.
1. head 다음부분(첫부분)에 삽입할 때
![](https://velog.velcdn.com/images/dlsdud9098/post/cf973262-5540-485c-afb0-45731257d488/image.png)
2. 중간에 삽입할 때
![](https://velog.velcdn.com/images/dlsdud9098/post/d72471b5-2a98-4061-a2bb-5b12185b46e3/image.png)
3. 마지막 노드 다음에 삽입할 때
![](https://velog.velcdn.com/images/dlsdud9098/post/b59da595-4f85-4375-aa34-0584eb3908db/image.png)


조건은 여러가지가 있겠지만 일단 오른차순으로 하겠다.

그러면 삽입하려는 노드가 기존 노드보다 작으면 앞쪽으로, 크다면 다음으로 넘어가게하면 된다.

```python
def insert_node():
    global head
    
    data = int(input('데이터를 입력하세요'))
    
    # 노드 생성
    node = Node()
    node.data = data
    print(f'입력: {data}')
    
    # 첫 노드
    if head == None:
        head = node
        return
    
    temp = head
    # 끝에 도달할 떄까지 무한반복
    while temp != None:
        # 삽입하려는 데이터가 더 크면 다음 노드로 이동
        if data > temp.data:
            # 이동하기 전에 현재 노드를 prev 변수에 저장한 수 다음 노드로 이동
            # 앞에 삽입할 때 이전 노드의 link에 삽입할 노드를 저장해야하기 떄문
            prev = temp
            temp = temp.link
        # 삽입하려는 노드가 더 작으면 현재 노드 앞에 삽입
        elif data < temp.data:
            # 만약 앞의 노드가 head일 경우
            if temp == head:
                head = node
                node.link = temp
                return
            else:
                node.link = temp
                prev.link = node
                return
    
    # while문을 빠져나왔다는 것은 마지막 노드 위에 붙이라는 의미
    prev.link = node
    
head = None

insert_node()
insert_node()
insert_node()

temp = head
print('출력: ')
# 노드 전체 출력
while temp != None:
    print(temp.data, end=' ')
    temp = temp.link
    
```

![](https://velog.velcdn.com/images/dlsdud9098/post/33d5ba17-d289-4e56-b903-11a333489e71/image.png)

---
## 💻 노드 삭제

노드를 삭제하는 것도 3가지 경우가 있다.
1. 가장 앞에 있는 노드를 삭제할 떄
![](https://velog.velcdn.com/images/dlsdud9098/post/db9f160b-f586-4333-b222-d9119a56fc78/image.png)
2. 가운데 노드를 삭제할 때
![](https://velog.velcdn.com/images/dlsdud9098/post/591af238-66ad-45ac-a201-9092ba4951ab/image.png)
3. 가장 마지막 노드를 삭제할 때
![](https://velog.velcdn.com/images/dlsdud9098/post/17cdf158-b3cb-48e1-976f-f7797efa3fd2/image.png)

먼저 노드를 순차적으로 돌면서 삭제할 값과 일치한 노드를 찾고 삭제한다.

```python
def delete_node(data):
    global head
    
    temp = head
    while temp != None:
        # 삭제할 데이터를 찾음
        if temp.data == data:
            # 삭제할 노드가 가장 앞에 있을 경우
            if temp == head:
                head = temp.link
                del temp
                return
            prev.link = temp.link
            del temp
            return
        # 못찾으면 다음 노드로 이동
        else:
            prev = temp
            temp = temp.link
    # 삭제할 노드가 가장 마지막일 경우
    prev.link = None
    del temp
    
head = None

insert_node(10)
insert_node(15)
insert_node(20)

#delete_node(10)
#delete_node(15)
delete_node(20)
temp = head
print('출력: ')
while temp != None:
    print(temp.data, end=' ')
    temp = temp.link
```

![](https://velog.velcdn.com/images/dlsdud9098/post/8bafdc7a-5b0b-4758-985f-657b0387f10c/image.png)

---
## 💻 노드 출력

노드 출력은 간단하다.
head -> 노드 데이터 출력 -> 다음 노드
이것을 노드가 끝날 때까지 반복하면 된다.

```python
def print_node():
    global head
    
    temp = head
    while temp != None:
        print(temp.data, end=' ')
        temp = temp.link
```