def solve():

  input = open('input.txt', 'r')
  
  stream = None
  for line in input:
    stream = line

  disk = []
  for i in range(len(stream)):
    if i % 2 == 0:
      for _ in range(int(stream[i])):
        disk.append(str(i // 2))
    else:
      for _ in range(int(stream[i])):
        disk.append(".")
      
  l = 0
  r = len(disk) - 1
  
  while l < r:
    if disk[l] != ".":
      l += 1
    elif disk[r] == ".":
      r -= 1
    else: # l == '.' and r == some digit
      disk[l], disk[r] = disk[r], disk[l]
      l += 1
      r -= 1
      
  i = 0
  ans = 0
  while i < len(disk) and disk[i] != ".":
    ans += int(disk[i]) * i
    i += 1
    
  print(ans)      

solve()