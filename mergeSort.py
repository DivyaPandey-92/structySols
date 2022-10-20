def merge_sort(nums):
  pass # todo
  if len(nums)<2:
    return nums
  else:
    mid=len(nums)//2
    first_half=nums[:mid]
    second_half=nums[mid:]
    # _merged_sort(first_half)
    soretd_left = merge_sort(first_half)
    sorted_right = merge_sort(second_half)
    return _merged_sort(soretd_left, sorted_right)
    
    
    
  
def _merged_sort(sorted_left, sorted_right):
  index1=0
  index2=0
  sorted_merge=[]
  while index1< len(sorted_left) and index2<len(sorted_right):
    if sorted_left[index1]<sorted_right[index2]:
      sorted_merge.append(sorted_left[index1])
      index1+=1
    else:
      sorted_merge.append(sorted_right[index2])
      index2+=1
  # if index1:
  sorted_merge=sorted_merge+sorted_left[index1:]
  # if index2:
  sorted_merge=sorted_merge+sorted_right[index2:]
  return sorted_merge
      
      
# print(_merged_sort([10, 4, 42, 5, 8], [100, 5, 6, 12, 40] ))
# print(_merged_sort([10, 4, 42, 5, 8], [100, 5, 6, 12, 40] ) )

merged_lists = _merged_sort([1, 2,  4], [3,5, 6, 7, 8])
print(merged_lists)       
  
  
  
  
  
  