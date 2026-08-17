def del_at_end(head):
    if head is None:
        return None

    if head.next is None:
        head = None  # Optional: Free the memory of the only node
        return None

    current = head
    while current.next.next is not None:
        current = current.next

    current.next = None  # Remove the last node
    return head