class stackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class myclass:
    def __init__(self):
        self.head = None

    # Push operation
    def push(self, data):
        new_node = stackNode(data)
        new_node.next = self.head
        self.head = new_node

    # Pop operation
    def pop(self):
        if self.head is None:
            return -1

        pop_data = self.head.data
        self.head = self.head.next
        return pop_data

    # Peek operation
    def peek(self):
        if self.head is None:
            return -1
        return self.head.data

    # Check if stack is empty
    def isEmpty(self):
        return self.head is None

    # Display stack
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Driver Code
s = myclass()

s.push(10)
s.push(20)
s.push(30)

s.display()          # 30 20 10

print(s.pop())       # 30
print(s.peek())      # 20

s.display()          # 20 10