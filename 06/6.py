import requests
import numpy as np
from math import ceil, floor
any = np.any

gifts = requests.get('https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBallDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--20b29549a475416a15aa81ff11b00da4c4103e67/pakker.txt?disposition=inline').text.splitlines()
gifts = [(int(g.split(',')[0]), int(g.split(',')[1])) for g in gifts]

grid = np.zeros((1, 20))

fallen_counter = 0

for gift in gifts:
    whole_gift = slice(gift[0], gift[0] + gift[1])
    left_half = slice(gift[0], gift[0] + ceil(gift[1] / 2))
    right_half = slice(gift[0] + floor(gift[1] / 2), gift[0] + gift[1])
    for r, row in enumerate(grid):
        if any(row[whole_gift]):
            if any(row[left_half]) and any(row[right_half]):
                if r == 0:
                    grid = np.insert(grid, 0, np.zeros((20)), axis=0)
                    grid[r, whole_gift] = 1
                else:
                    grid[r - 1, whole_gift] = 1
            else:
                fallen_counter += 1
            break
        if r == len(grid) - 1:
            grid[r, whole_gift] = 1
            break

print(f"{fallen_counter} packages fell down")
