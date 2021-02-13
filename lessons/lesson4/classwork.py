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
            index -=1
        return node.value 

    def append(self, node: Node):
        ...

    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        ...

    def reverse(self):
        ...