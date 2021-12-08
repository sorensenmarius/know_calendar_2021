import requests
import re

data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBak1DIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--d6d3984e0f603df1771ef6b699e6e86d6ee577a7/tree.txt?disposition=inline')
data.encoding = 'utf-8'
data = data.text
class Node():
  def __init__(self, name, l, r):
    self.name = name
    self.l = l
    self.r = r

def get_height(node):
  if node == None:
    return 0
  if (node.name == 'Grinch'):
    return 0 + max(get_height(node.l), get_height(node.r))
  else:
    return 1 + max(get_height(node.l), get_height(node.r))

def create_tree(d):
  if d == None:
    return None
  name, l, r = split_current(d)
  return Node(name, create_tree(l), create_tree(r))

def split_current(d):
  count = 0

  if '(' not in d:
    return d, None, None
  name = d[:d.index('(')]
  d = d[d.index('(')+1:-1]
  if '(' not in d:
    l, r = d.split(' ')
    return name, l, r
    
  for i, c in enumerate(d):
    if c == '(':
      count += 1
    elif c == ')':
      count -= 1
      if count == 0:
        return (name, d[:i+1], d[i+2:])

n = create_tree(data)
print(get_height(n) - 1)