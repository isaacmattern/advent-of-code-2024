def getProduct(stream: str) -> int:
  
  start = 0
  mid = stream.find(',')
  end = stream.find(')')
  
  if (
    (mid == -1 or end == -1)
    or (mid - start > 3 or end - mid > 4)):
    return 0
  
  first = 0
  second = 0
  for i in range(start, mid):
    if not stream[i].isnumeric:
      return 0
    
  for i in range(mid + 1, end):
    if not stream[i].isnumeric:
      return 0
    
  first = int(stream[start:mid])
  second = int(stream[mid+1:end])
    
  return first * second

def solve():
  
  input = open('input.txt', 'r')
  
  stream = ''
  for line in input:
    stream += line
    
  ans = 0
  do = True
  while stream:
    nextDo = stream.find('do()')
    nextDont = stream.find('don\'t()')
    nextMul = stream.find('mul(')
    
    if nextMul < nextDo and nextMul < nextDont:
      pass
    else:
      if nextDo < nextMul and nextDont < nextMul:
        if nextDo < nextDont:
          do = False
        else:
          do = True
      elif nextDo < nextMul:
        do = True
      elif nextDont < nextMul:
        do = False
        
    if nextMul == -1:
      break
    elif do:
      stream = stream[nextMul+4:]
      ans += getProduct(stream)
      # We don't need to know where the mul() call ends,
      # we can just go to the next valid sequence after slicing off a single character
      
    if stream:
      stream = stream[1:]
    
  print(ans)      

solve()