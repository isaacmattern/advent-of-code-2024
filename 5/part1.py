import collections

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
      
  ans = 0
  for update in updates:
    valid = True
    after = []
    for i in range(len(update) -1, -1, -1):
      for num in after:
        if update[i] in lookup[num]:
          valid = False
          break
      
      if not valid:
        break
      after.append(update[i])
    
    if valid:
      midpoint = len(update) // 2
      ans += update[midpoint]
    
  print(ans)      

solve()