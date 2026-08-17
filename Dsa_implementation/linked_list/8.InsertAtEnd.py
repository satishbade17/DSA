class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def InserAtEnd(head, x):
    new_node = Node(x)

    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node

    return head


# Create Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Insert 40 at the end
head = InserAtEnd(head, 40)

# Print Linked List
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")