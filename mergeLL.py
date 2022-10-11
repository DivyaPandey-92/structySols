class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  pass # todo
  # tail=None
  cur1=head_1
  cur2=head_2
  head=Node(None)
  tail=head
  
  while cur2 is not None and cur1 is not None:
    
    if cur1.val < cur2.val:
      tail.next=cur1
      cur1=cur1.next
    
    else:
      tail.next=cur2
      cur2=cur2.next
    tail=tail.next
    
    if cur1 is not None:
      tail.next=cur1
      
    if cur2 is not None:
      tail.next=cur2
    
  return head.next