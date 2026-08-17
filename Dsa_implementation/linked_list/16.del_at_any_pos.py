def del_at_any_pos(head, pos):
    if head is None:
        return None

    if pos == 0:
        new_head = head.next
        head = None  # Optional: Free the memory of the old head node
        return new_head

    current = head
    for _ in range(pos - 1):
        if current is None or current.next is None:
            return head  # Position is out of bounds
        current = current.next

    if current.next is not None:
        temp = current.next
        current.next = temp.next
        temp = None  # Optional: Free the memory of the deleted node

    return head