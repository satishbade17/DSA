def del_node_in_DLL(head, x):
    if head is None or x<=0:
        return head
    
    if x==1:
        head=head.next
        return head
    if head:
        head.prev=None
        return head
    current=head
    count=1
    while current and count<x:
        current=current.next
        count+=1
    if current is None:
        return head
    
    if current.next:
        current.next.prev=current.prev
    if current.prev:
        current.prev.next=current.next
    
    current=None
    return head
    