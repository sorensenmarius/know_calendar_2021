import requests
import re

# data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBak1DIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--d6d3984e0f603df1771ef6b699e6e86d6ee577a7/tree.txt?disposition=inline')
# data.encoding = 'utf-8'
# data = data.text

data = 'Aurora(Toralv(Grinch(Kari Robinalv) Alvborg) Grinch(Alva(Alve-Berit Anna) Grete(Ola Hans)))'

def split_current(d):
  count = 0

  if not d.contains('('):
    return None
  name = d[:d.index('(')]
  d = d[d.index('(')+1:-1]
  for i, c in enumerate(d):
    if c == '(':
      count += 1
    elif c == ')':
      count -= 1
      if count == 0:
        return (name, d[:i+1], d[i+2:])

depth = 0
while True:
  current = split_current(data)
  if current is None:
    break
  if current[0] != 'Grinch':
    depth += 1
  data = current[2]

print(depth)