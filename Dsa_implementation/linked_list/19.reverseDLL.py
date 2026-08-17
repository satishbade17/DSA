def reverseDLL(head):
    if head is None:
        return None

    current = head
    prev = None

    while current is not None:
        # Swap the next and prev pointers
        next_node = current.next
        current.next = prev
        current.prev = next_node

        # Move to the next node in the original list
        prev = current
        current = next_node

    # After the loop, prev will be the new head of the reversed list
    return prev