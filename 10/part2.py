import collections

def inBounds(point: tuple[int], grid: list[list[int]]):
  if point[0] < 0 or point[0] >= len(grid):
    return False
  if point[1] < 0 or point[1] >= len(grid[0]):
    return False
  
  return True

def getTrailheadScore(trailhead: tuple[int], grid: list[list[int]]) -> int:
  trailheadScore = 0
  queue = collections.deque()
  queue.append(trailhead)
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  
  # Breadth first search
  while queue:
    row, col = queue.popleft()
    val = grid[row][col]
    
    for direction in directions:
      newRow = row + direction[0]
      newCol = col + direction[1]
      
      if inBounds((newRow, newCol), grid):
        newVal = grid[newRow][newCol]
        if newVal - val == 1:
          if newVal == 9:
            trailheadScore += 1
          else:
            queue.append((newRow, newCol))
  
  return trailheadScore

def solve():

  input = open('input.txt', 'r')
  
  grid = []
  for line in input:
    trimmedLine = line.removesuffix('\n')
    newGridLine = [int(num) for num in trimmedLine]
    grid.append(newGridLine)
    
  ans = 0
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == 0:
        ans += getTrailheadScore((row, col), grid)
    
  print(ans)      

solve()