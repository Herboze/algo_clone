from lab4.utils import Node


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def Enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def Dequeue(self):
        if self.isEmpty():
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_data

    def display(self) -> str:
        if self.isEmpty():
            return ""
        res = ""
        current = self.front
        while current:
            res += f"{current.data} -> "
            current = current.next
        res += "None"
        return res


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    def display(self):
        if self.isEmpty():
            return
        current = self.top
        res = ""
        while current:
            res += f"{current.data} -> "
            current = current.next
        res += "None"
        return res
