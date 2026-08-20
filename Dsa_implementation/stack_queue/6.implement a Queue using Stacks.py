class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Enqueue
    def push(self, x):
        self.s1.append(x)

    # Dequeue
    def pop(self):
        if not self.s1 and not self.s2:
            return -1

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    # Front element
    def peek(self):
        if not self.s1 and not self.s2:
            return -1

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    # Check if queue is empty
    def empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0
q = MyQueue()

q.push(10)
q.push(20)
q.push(30)

print(q.peek())    # 10
print(q.pop())     # 10
print(q.peek())    # 20
print(q.empty())   # False