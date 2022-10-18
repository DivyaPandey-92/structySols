def lefty_nodes(root):
  # llist=[]
  return _lefty_nodes(root,0, [])
  # return llist

def _lefty_nodes(root, level_num, llist ):
  pass # todo
  if root is None:
    return []
  
  # level_set=set()
  # llist=[]
  # if llist.index() not in level_set:
  #   # level_set.add(level_num)
  #   llist.append(root.val)
  if len(llist)==level_num:
    llist.append(root.val)
  
  left= _lefty_nodes(root.left, level_num+1, llist)
  right=_lefty_nodes(root.right, level_num+1, llist)
  
  return  llist
  