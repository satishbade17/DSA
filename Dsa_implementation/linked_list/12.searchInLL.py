def searchinll(head,h,n,key):
    current=head
    while current not in None:
        if current.data==key:
            return True
        current=current.next
    return False
searchinll()