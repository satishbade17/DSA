class mystack:
    def __init__(self):
        self.arr = []

    # Push operation
    def push(self, data):
        self.arr.append(data)

    # Pop operation
    def pop(self):
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()
    
s = mystack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())   # 30
print(s.pop())   # 20
print(s.pop())   # 10
print(s.pop())   # -1 (Stack is empty)