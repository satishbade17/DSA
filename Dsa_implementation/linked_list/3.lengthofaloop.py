def count_nodes_in_loop(head):
    slow = head
    fast = head

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Count the number of nodes in the loop
            count = 1
            temp = slow.next

            while temp != slow:
                count += 1
                temp = temp.next

            return count

    return 0  # No loop found