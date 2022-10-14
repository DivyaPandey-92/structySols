# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
def all_tree_paths(root):
  return  _all_tree_paths(root,[[]])

def _all_tree_paths(root, llist):
  pass # todo
  # llist=[[]]
  
  if root is None:
    return []
  
  # llist.append(root.val)
  left=[root.val]+_all_tree_paths(root.left, llist)
  right=[root.val]+_all_tree_paths(root.right, llist)
  ways=left.append(right)
  llist.append(ways)
  return llist
  