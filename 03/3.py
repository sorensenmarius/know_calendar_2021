import requests
from nltk import ngrams

data = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBOdz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--31fa0c541c69eeb9063ccfc56e686f4768662004/input.txt?disposition=inline').text

for i in range(100, 0, -1):
    if i % 2 != 0: continue
    for j in ngrams(data, i):
        if j.count('J') == len(j) / 2:
            print(f"{len(j)}, {data.index(''.join(j))}")
            exit()
