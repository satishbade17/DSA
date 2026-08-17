def del_at_begin(head):
    if head is None:
        return None

    new_head = head.next
    head = None  # Optional: Free the memory of the old head node
    return new_head