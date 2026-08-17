class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def InsertAtBeginning(head, x):
    new_node = Node(x)

    if not head:
        return new_node

    new_node.next = head
    head = new_node

    return head