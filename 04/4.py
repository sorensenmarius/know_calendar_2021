all_steps = [1079, 10079, 100079, 10000079]

for steps in all_steps:
  current = (0, 0)
  north = True
  for i in range(steps):
    if north:
      current = (current[0], current[1] + 1)
      if current[1] % 5 != 0 and current[1] % 3 == 0:
        north = False
    else:
      current = (current[0] + 1, current[1])
      if current[0] % 5 == 0 and current[0] % 3 != 0:
        north = True
  print(current)