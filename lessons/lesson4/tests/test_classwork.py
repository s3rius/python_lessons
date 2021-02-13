from typing import List
from lessons.lesson4.classwork import LinkedList, Node


def list_to_linked(values: List[int]) -> LinkedList:
    head_node = Node(values.pop(0))
    tmp_node = head_node
    for item in values:
        tmp_node.next = Node(item)
        tmp_node = tmp_node.next
    return LinkedList(head_node)


def test_linked_list_len():
    l = list_to_linked([1, 2, 3])
    print(l)
    assert len(l) == 3


def test_linked_list_itemgetter():
    l = list_to_linked([1, 2, 3, 4, 5])
    assert l[4] == 5


def test_delete_first():
    l = list_to_linked([4, 3, 2, 1])

    l.delete_first()

    assert len(l) == 3
    assert l.head.value == 3


def test_delete_last():
    l = list_to_linked([4, 3])

    l.delete_last()

    assert len(l) == 1
    assert l.head.next == None
    assert l.head.value == 4


def test_append():
    l = list_to_linked([1, 2])
    l.append(Node(44))
    assert len(l) == 3
    assert l.head.next.next.value == 44


def test_reverse():
    l = list_to_linked([3, 2, 1])
    l.reverse()
    assert len(l) == 3
    assert l.head.value == 1
    assert l.head.next.value == 2
    assert l.head.next.next.value == 3
