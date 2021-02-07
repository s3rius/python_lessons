from lessons.lesson2.data_structures import Queue, Stack


def test_queue():
    q = Queue()

    q.push(123)
    q.push("abc")

    assert q.pop() == 123
    assert q.pop() == "abc"


def test_stack():
    s = Stack()
    s.push(123)
    s.push("abc")

    assert s.pop() == "abc"
    assert s.pop() == 123
