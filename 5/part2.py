import collections
import copy

def solve():

  input = open('input.txt', 'r')
  
  lookup = collections.defaultdict(list)
  updates = []

  for line in input:
    if '|' in line:
      before, after = line.split('|')
      lookup[int(before)].append(int(after))
    elif ',' in line:
      trimmed = line.removesuffix('\n')
      numsAsStrings = trimmed.split(',')
      nums = [int(num) for num in numsAsStrings]
      updates.append(nums)
      
  invalidIndices = []
  for updateIndex in range(len(updates)):
    update = updates[updateIndex]
    valid = True
    after = []
    for i in range(len(update) -1, -1, -1):
      for num in after:
        if update[i] in lookup[num]:
          invalidIndices.append(updateIndex)
          valid = False
          break
      
      if not valid:
        break
      after.append(update[i])
      
  ans = 0
  for i in invalidIndices:
    update = updates[i]
    
    # reorder the list by bubbling entries which are 'too early' to the right, one index at a time,
    # repeatedly scanning through the list until it is valid
    valid = False
    while not valid:
      valid = True
      after = []
      for i in range(len(update) -1, -1, -1):
        for num in after:
          if update[i] in lookup[num]:
            # shift with val to the right
            update[i], update[i+1] = update[i+1], update[i]
            valid = False
            break
        if not valid:
          break
        after.append(update[i])
    
    midpoint = len(update) // 2
    ans += update[midpoint]
        
  print(ans)      

solve()