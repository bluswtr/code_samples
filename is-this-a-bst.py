"""
Problem:
https://www.hackerrank.com/challenges/is-binary-search-tree/problem


# Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None   

"""


# Solution 1 - Traverse in order add to array, check if sorted
def traverse(root, arr):
    if root is None:
        return
    traverse(root.left, arr)
    arr.append(root.data)
    traverse(root.right, arr)
    
def check_binary_search_tree_(root):
   
    arr = []

    traverse(root, arr)
    # print(arr)
    for i in range(1,len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True


# Solution 2 - Write solution 1 but recursively traverse in order while remembering the previous node
prev = None

def check_binary_search_tree_(root):
    global prev
    if root is None:
        return True
    if check_binary_search_tree_(root.left) is False:
        return False
    if prev is not None and root.data <= prev:
        return False
    prev = root.data
    if check_binary_search_tree_(root.right) is False:
        return False
    return True


# Solution 3 - Recursively traverse in order and pass in what the minimum and maximum the current node could be
def isbst(root, min, max):
    if root is None: 
        return True
    
    if max is not None and root.data >= max or min is not None and root.data <= min:
        return False
        
    if isbst(root.left, min, root.data) is False or isbst(root.right, root.data, max) is False:
        return False

    return True
    
def check_binary_search_tree_(root):
    return isbst(root, None, None)