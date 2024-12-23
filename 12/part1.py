from collections import deque

def inBounds(point: tuple[int], height, width) -> bool:
  if point[0] < 0 or point[0] >= height:
    return False
  elif point[1] < 0 or point[1] >= width:
    return False
  return True

def getRegion(point: tuple[int], garden: list[list[int]]) -> tuple[set, int, int]:
  """
  Args:
      point (tuple[int]): The point within a region to start searching
      garden: The entire grid / "garden"

  Returns:
      tuple[set, int, int]: A set of all the points in the region, the area of
      the region, and the perimeter of the region
  """
  # Constants
  height = len(garden)
  width = len(garden[0])
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  marker = garden[point[0]][point[1]]
  
  
  seen = set()
  perimeter = 0
  
  queue = deque()
  queue.append(point)
  seen.add(point)
  
  while queue:
    curr = queue.popleft()
    
    for direction in directions:
      newI = curr[0] + direction[0]
      newJ = curr[1] + direction[1]
      newPoint = (newI, newJ)
      
      if inBounds(newPoint, height, width) and garden[newI][newJ] == marker:
        if newPoint not in seen:
          queue.append(newPoint)
          seen.add(newPoint)
      else:
        perimeter += 1
  
  return seen, len(seen), perimeter
  

def solve():

  input = open('input.txt', 'r')
  
  garden = []
  for line in input:
    trimmedLine = line.removesuffix('\n')
    garden.append(trimmedLine)
  
  ans = 0
  seen = set()
  for i in range(len(garden)):
    for j in range(len(garden[0])):
      if (i, j) not in seen:
        newlySeen, area, perimeter = getRegion((i, j), garden)
        ans += area * perimeter
        
        for point in newlySeen:
          seen.add(point)

  print(ans)      

solve()