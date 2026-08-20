class myQueue:
    def __init__(self):
        self.queue = []

    # Enqueue
    def push(self, x):
        self.queue.append(x)

    # Dequeue
    def pop(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)
    
q = myQueue()

q.push(10)
q.push(20)
q.push(30)

print(q.pop())   # 10
print(q.pop())   # 20

q.push(40)

print(q.pop())   # 30
print(q.pop())   # 40
print(q.pop())   # -1