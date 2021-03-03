from collections import deque

d = deque()

d.append(1)
d.appendleft(1)

d.pop()
d.popleft()

class Node:
    def __init__(self, value, next_node=None):
        self.next = next_node
        self.value = value


class LinkedList:
    def __init__(self, head_node: Node):
        self.head = head_node

    def __len__(self) -> int:
        node = self.head
        length = 1
        while node.next != None:
            length += 1
            node = node.next
        return length

    def __getitem__(self, index):
        node = self.head
        while index != 0:
            node = node.next
            index -= 1
        return node.value

    def append(self, node: Node):
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next

        tmp.next = node

    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        tmp = self.head
        while tmp.next.next is not None:
            tmp = tmp.next
        tmp.next = None

    def reverse(self):
        curr = self.head
        previous = None
        while curr is not None:
          next_el = curr.next
          curr.next = previous
          previous = curr
          curr = next_el
        self.head = previous