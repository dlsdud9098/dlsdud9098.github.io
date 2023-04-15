---
layout: post
title: Double Linked List(더블 링크드 리스트)
categories: [Coding, Python]
tags: [python]
---

<br>

# 📙더블 링크드 리스트

## 💻더블 링크드 리스트

더블 링크드 리스트(Double Linked List)는 한 쪽으로밖에 갈 수 없는 단순 리스트(Linked list)를 보안하혀 만들어졌다.

한 번 시작하면 한 쪽으로밖에 갈 수 없는 것에 비해 더블 링스드 리스트는 앞과 뒤의 위치가 저장되어 데이터 정의에 용이하다.

---

## 💻 기본 형태

![](https://velog.velcdn.com/images/dlsdud9098/post/ed9f50b6-6757-4c98-a180-4ad98e6a52b8/image.png)

---

## 💻 노드 생성

노드 생성은 단순 연결 리스트와 같다.

```python
class Node:
    def __init__(self):
        self.prev = None
        self.data = None
        self.next = None
```

현재 노드를 기준으로 이전 노드를 저장할 prev와 다음 노드를 저장할 next를 가지고있다.

---

## 💻 노드 삽입

노드 삽입은 3가지 경우가 있다.

1. head 앞 일때
2. 노드 사이일 때
3. 마지막일 때

4. 헤드가 앞에 있을 때

![](https://velog.velcdn.com/images/dlsdud9098/post/0218c7fe-69a3-467e-81fc-514b5b978241/image.png)

2. 노드 사이일 때

![](https://velog.velcdn.com/images/dlsdud9098/post/97e0d6ca-1926-4d61-bc4d-31755ee1d2e9/image.png)

3. 마지막일 때

![](https://velog.velcdn.com/images/dlsdud9098/post/c20c7716-ef22-4fbb-934c-7e3421744c09/image.png)

```python
def add_node(data):
    global head, tail

    node = Node()
    node.data = data

    # 노드가 없을 때
    if head == None:
        head = node
        tail = node
        return

    temp = head
    while temp != None:
        # 노드 앞에 삽입
        if temp.data > node.data:
            # 노드 앞이 head일 때
            if temp == head:
                node.next = temp
                temp.prev = node
                head = node
                return
            # 노드와 노드 사이일 때
            else:
                prev.next = node
                node.prev = prev
                node.next = temp
                temp.prev = node
                return
        # 다음으로 넘어감
        else:
            if temp.next == None:
                break
            prev = temp
            temp = temp.next

    # 마지막 노드 뒤에 삽입
    if temp.next == None:
        temp.next = node
        node.prev = temp
        tail = node
        return
```

---

## 💻 노드 제거

노드 제거에도 3가지 경우가 있다.

1. 헤드 다음 노드일 때
2. 노드와 노드 사이일 때
3. 마지막일 때

```python
def delete_node(data):
  global head, tail

  temp = head
  while temp != None:
      # 이름을 찾음
      if data in temp.data:
          print('찾음')
          # 가장 처음일 때
          if temp == head:
              head = temp.next
              temp.next.prev = None
              del temp
              return

          # 가장 뒤에 있을 때
          elif temp.next == None:
              prev.next = None
              tail = prev
              del temp
              return

          # 중간에 있을 때
          else:
              prev.next = temp.next
              temp.next.prev = prev
              del temp
              return

      else:
          prev = temp
          temp = temp.next
```

---

## 💻 노드 출력

노드 출력에는 두가지 경우가 있다.

1. head에서부터(처음부터) 출력할 때
2. tail에서부터(마지막부터) 출력할 때

```python
def list_node():
    global head, tail

    temp = head
    temp_tail = tail
    print()
    print('정방향 출력: ', end=' ')
    while temp != None:
        print(f'{temp.data}', end='\t')
        temp = temp.next

    print()

    print('역방향 출력: ', end=' ')
    while temp_tail != None:
        print(f'{temp_tail.data}', end='\t')
        temp_tail = temp_tail.prev
    print()
```
