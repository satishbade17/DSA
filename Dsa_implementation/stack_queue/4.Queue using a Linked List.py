class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue
    def push(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    # Dequeue
    def pop(self):
        if self.front is None:
            return -1

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

    # Peek
    def peek(self):
        if self.front is None:
            return -1
        return self.front.data

    # Check if queue is empty
    def isEmpty(self):
        return self.front is None

    # Display queue
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
q = MyQueue()

q.push(10)
q.push(20)
q.push(30)

q.display()
# 10 -> 20 -> 30 -> None

print(q.pop())    # 10
print(q.peek())   # 20

q.display()
# 20 -> 30 -> None

print(q.isEmpty())  # False