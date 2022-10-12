# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  
  if root is None:
    return False
  
  if root.val==target:
    return True
    
  # lc=None
  # rc=None
  # cur_node=root
  
  
#   if cur_node.left:
#     lc=tree_includes(cur_node.left, target)
#   if cur_node.right:
#     rc=tree_includes(cur_node.right, target)
    
#   return lc or rc
    
  # return tree_includes(cur_node.left, target) or tree_includes(cur_node.right, target)
  # lc=tree_includes(cur_node.left, target)
  # rc=tree_includes(cur_node.right, target)
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)
#   left=tree_includes(root.left, target) 
#   if left:
#     return True
#   right=tree_includes(root.right, target)
#   if right:
#     return True
    

  # return False

  # if lc or rc:
  #   return True
  # else:
  #   return False

    
    
  