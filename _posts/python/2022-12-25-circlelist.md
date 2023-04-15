---
layout: post
title: Circle List(써클 리스트)
categories: [Coding, Python]
tags: [python]
---

<br>

# 📒 서클 리스트(Circle List)

## 💻 기본 구조

![](https://velog.velcdn.com/images/dlsdud9098/post/ec225776-3227-4b1f-8633-fee70ebacb7d/image.png)


---

## 💻 노드 넣기

노드를 넣는데에는 5가지 경우가 있다.

1. 첫 노드일 때
1-1. 노드가 있는 상태에서 헤드 다음으로 넣을 때
2. 중간에 넣을때
3. 마지막에 넣을때
3-1. 마지막 직전에 넣을 때

```python

def add_node(data):
    global head
    
    node = Node()
    node.data = data

    temp = head 
    # 노드가 없을때
    if not head:
        head = node
        node.link = head
        return
    # head 앞에 삽입할 때, 오름차순 정렬이기 때문에 
    # head의 데이터 즉 처음 데이터보다 작다는 것은
    # 가장 앞에 들어간다는 의미
    elif temp.data > node.data:
        node.link = temp
        # 가장 뒤에 있는 노드의 link를 가장 앞의 노드로 옮겨야 하기 때문에
        # 마지막 노드로 이동 후 마지막 노드.link를 현재 head앞에
        # 추가하는 노드와 연결한다.
        while temp.link != head:
            temp = temp.link

        temp.link = node
        head = node
        return
    
    temp = head
    while temp.link != head:
        # 노드 앞에 삽입
        if temp.data > node.data:
            prev.link = node
            node.link = temp
            return
        # 삽입 안함(다음으로 넘어가기)
        else:
            # 현재 노드
            prev = temp
            # 다음 노드로 넘어감
            temp = temp.link

    # 마지막 노드로 왔는데 마지막 노드의 데이터가 더 클때 앞에 넣음
    if temp.data > node.data:
        node.link = temp
        prev.link = node
    else:
        temp.link = node
        node.link = head
   ```
   
   ---
   
   ## 💻 노드 삭제
   
   노드 삭제에는 3가지 경우가 있다.
   
   1. 처음 노드일 때
   ![](https://velog.velcdn.com/images/dlsdud9098/post/8957cc26-69ed-459d-ace2-5116a9de1cd9/image.png)


   2. 중간 노드일 때
   ![](https://velog.velcdn.com/images/dlsdud9098/post/9fa857bb-210d-4f7a-973b-74d482952b44/image.png)

   3. 마지막 노드일 때
   ![](https://velog.velcdn.com/images/dlsdud9098/post/7ea79806-6138-46e5-8be4-cd9810c89435/image.png)


   
   ```python
   def delete_node():
    global head

    data = int(input(''))
    temp = head
    # 삭제할 노드가 처음 노드일 때
    if head.data == data:
        temp = head
        # 마지막 노드로 이동
        # 마지막 노드의 다음 노드가 헤드일 때 끝나므로
        # 마지막 노드의 다음 노드 즉 처음 노드를 삭제한다.
        while temp.link != head:
            temp = temp.link
        head = head.link
        del temp.link

        temp.link = head
        return

    # 삭제할 노드가 중간에 있을 때
    temp = head
    while temp.link != head:
        if temp.data == data:
            prev.link = temp.link
            del temp
            return
        prev = temp
        temp = temp.link

    # 삭제할 노드가 마지막일 때
    prev.link = temp.link
    del temp
 ```

---

## 💻 노드 출력


```python
def list_node():
    global head
    # cnt = 0
    temp = head
    while temp.link != head:
        print(temp.data)
        temp = temp.link
        if temp.link == head:
            print(temp.data)
   ```