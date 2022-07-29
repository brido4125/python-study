# Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)

    def insert(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_node(self,index):
        node = self.head
        count = 0
        while count < index:
            count += 1
            node = node.next
        return node

    def delete_Node(self, index):
        if index == 0:
            del_node = self.head.data
            self.head = self.head.next
            return del_node
        node = self.get_node(index-1)
        del_node = node.next.data
        node.next = node.next.next
        return del_node

# 요시푸스 문제
N, K = map(int, input().split(' '))

num_list = [i for i in range(1, N + 1)]
answer_list = []

for i in range(N):
    k_index = K - 1
    if len(num_list) > K:
        answer_list.append(num_list[k_index])
        del num_list[k_index]
        front_list = num_list[:k_index]
        lear_list = num_list[k_index:]
        num_list = lear_list + front_list
    elif len(num_list) == 1:
        answer_list.append(num_list[0])
    else:
        k_index = (k_index % len(num_list))
        target = num_list[k_index]
        answer_list.append(target)
        num_list.remove(target)
        front_list = num_list[:k_index]
        lear_list = num_list[k_index:]
        num_list = lear_list + front_list

print('<',end='')
for i in range(len(answer_list) - 1):
    print(answer_list[i],end=', ')
print(answer_list[len(answer_list) - 1],end='')
print('>')
