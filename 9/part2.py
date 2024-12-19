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
        
  freeSpaces = []
  l = 0
  r = 0
  while l < len(disk):
    while l < len(disk) and disk[l] != ".":
      l += 1
    r = l
    while r < len(disk) and disk[r] == ".":
      r += 1
    size = r - l
    freeSpaces.append((size, l, r))
    l = r + 1
        
  while True:
    
    shiftOccurred = False
      
    r = len(disk) - 1
    l = len(disk) - 1
    while r >= 0 and not shiftOccurred:
      while r >= 0 and disk[r] == ".":
        r -= 1
      l = r - 1
      val = disk[r]
      while l >= 0 and disk[l] == val:
        l -= 1
      sizeOfFile = r - l
      
      for i in range(len(freeSpaces)):
        sizeOfSpace, spaceL, spaceR = freeSpaces[i]
        if spaceL > l:
          break
        if sizeOfSpace >= sizeOfFile:
          for j in range(sizeOfFile):
            disk[spaceL + j] = val
            disk[l + j + 1] = "."
          
          freeSpaces[i] = (sizeOfSpace - sizeOfFile, spaceL + sizeOfFile, spaceR)

          shiftOccurred = True
          break
      
      r = l
    
    if not shiftOccurred:
      break
          
  i = 0
  ans = 0
  
  while i < len(disk):
    if disk[i] != ".":
      ans += int(disk[i]) * i
    i += 1
    
  print(ans)      

solve()