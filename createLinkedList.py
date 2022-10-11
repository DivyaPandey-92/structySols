class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  pass # todo
  
  head=Node(None)
  tail=head
  ind=0
  
  # while ind<len(values):
  for value in values:
    # current=Node(value)


    tail.next=Node(value)
    tail=tail.next
    
  return head.next



  #Using Recusrsion

  class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
def create_linked_list(values):
  
  return _create_linked_list(values,0)

def _create_linked_list(values, current_index):
  
  if len(values)==current_index:
    return None
    
  head=Node(values[current_index])
  head.next=_create_linked_list(values, current_index+1)
      
  return head