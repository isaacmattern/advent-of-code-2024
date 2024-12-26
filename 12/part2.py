from collections import deque

def inBounds(point: tuple[int], height, width) -> bool:
  if point[0] < 0 or point[0] >= height:
    return False
  elif point[1] < 0 or point[1] >= width:
    return False
  return True

def getNumSides(perimeterPoints: set[tuple[int]], garden: list[list[int]]) -> int:
  sideToSide = [(0, -1), (0, 1)]
  upAndDown = [(-1, 0), (1, 0)]
  sides = set()
  
  for point in perimeterPoints:
    for setOfDirections in [sideToSide, upAndDown]:
      
      side = set()
      side.add(point)
      
      sideQueue = deque()
      sideQueue.append(point)
      
      seen = set()
      seen.add(point)
      
      while sideQueue:
        curr = sideQueue.popleft()

        for direction in setOfDirections:
          newI = curr[0] + direction[0]
          newJ = curr[1] + direction[1]
          newPoint = (newI, newJ)
          
          if newPoint in perimeterPoints and newPoint not in seen:
            seen.add(newPoint)
            side.add(newPoint)
            sideQueue.append(newPoint)
          
      if len(side) > 1:
        frozenSide = frozenset(side)
        if frozenSide not in sides:
          sides.add(frozenSide)
        
  for side in sides:
    print(side)
  return len(sides)

def getRegion(point: tuple[int], garden: list[list[int]]) -> tuple[set, int, int]:
  """
  Args:
      point (tuple[int]): The point within a region to start searching
      garden: The entire grid / "garden"

  Returns:
      tuple[set, int, int]: A set of all the points in the region, the area of
      the region, and the number of sides of the region
  """
  # Constants
  height = len(garden)
  width = len(garden[0])
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
  marker = garden[point[0]][point[1]]
  
  seen = set()
  queue = deque()
  queue.append(point)
  seen.add(point)
  
  perimeterPoints = deque()
  
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
        perimeterPoints.append(newPoint)
        
  numSides = getNumSides(perimeterPoints, garden)
  
  return seen, len(seen), numSides
  

def solve():

  input = open('exampleInput.txt', 'r')
  
  garden = []
  for line in input:
    trimmedLine = line.removesuffix('\n')
    garden.append(trimmedLine)
  
  ans = 0
  seen = set()
  for i in range(len(garden)):
    for j in range(len(garden[0])):
      if (i, j) not in seen:
        newlySeen, area, numSides = getRegion((i, j), garden)
        print(area, numSides)
        ans += area * numSides
        
        for point in newlySeen:
          seen.add(point)

  print(ans)      

solve()