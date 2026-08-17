def removeNthFromEnd(self, head,n):
        if not head:
            return None

        slow=head
        fast=head
        count=0

        while count<n:
            fast=fast.next
            count +=1

        if fast is None:
            return head.next

        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head