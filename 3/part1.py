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
  while stream:
    next = stream.find('mul(')
    if next != -1:
      stream = stream[next+4:]
      ans += getProduct(stream)
      # We don't need to know where the mul() call ends,
      # we can just go to the next valid sequence after slicing off a single character
      if stream:
        stream = stream[1:]

    else:
      break
    
  print(ans)      

solve()