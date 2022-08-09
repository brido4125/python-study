import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:  # 루트 노드가 비어 있으면 루트 노드 추가
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if current.data > data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                if current.data < data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right

    def postOrder(self, node=None):
        global answer
        if node is None:
            node = self.root
        if node.left is not None:
            self.postOrder(node.left)
        if node.right is not None:
            self.postOrder(node.right)
        answer.append(node.data)


tree = Tree()
while True:
    try:
        tree.add(int(input()))
    except:
        break

answer = []
tree.postOrder()
print('\n'.join(map(str, answer)))
