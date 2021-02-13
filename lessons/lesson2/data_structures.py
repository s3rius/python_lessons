from typing import TypeVar, Generic

T = TypeVar("T")


class Queue(Generic[T]):
    """
    Queue means that you can push
    element at the end and then you can pop only
    the first elemet.
    """

    def __init__(self):
        self.mas = []

    def push(self, element: T) -> None:
        self.mas.append(element)

    def pop(self) -> T:
        return self.mas.pop(0)


class Stack(Generic[T]):
    """
    Stack means that you can push
    element at the end and then you can pop only
    the last elemet.
    """

    def __init__(self):
        self.mas = []

    def push(self, element: T) -> None:
        self.mas.append(element)

    def pop(self) -> T:
        return self.mas.pop(len(self) - 1)

    def __len__(self) -> int:
        return len(self.mas)
