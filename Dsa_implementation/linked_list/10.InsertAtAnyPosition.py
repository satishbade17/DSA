class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def InsertAtPosition(head, x, pos):
    new_node = Node(x)

    if pos == 1:
        new_node.next = head
        return new_node

    current = head
    count = 1

    while current and count < pos - 1:
        current = current.next
        count += 1

    if current:
        new_node.next = current.next
        current.next = new_node

    return head