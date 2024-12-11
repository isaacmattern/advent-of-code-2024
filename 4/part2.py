def withinGridBorder(i: int, j: int, grid: list[list[int]]) -> int:
  validI = 1 <= i < len(grid) - 1
  validJ = 1 <= j < len(grid[0]) - 1
  
  return validI and validJ

def centerOfXmas(i: int, j: int, grid: list[list[int]]) -> bool:
  if grid[i][j] != 'A' or (not withinGridBorder(i, j, grid)):
    return 0
  
  # see scratchpad.txt in this folder
  valid = [['M', 'S', 'M', 'S'], ['M', 'M', 'S', 'S'], ['S', 'S', 'M', 'M'], ['S', 'M', 'S', 'M']]
  # the directions array is specifically ORDERED according to the 'valid' array
  # the order is: top-left, top-right, bottom-left, bottom-right 
  directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
  corners = []
  for direction in directions:
    newI = i + direction[0]
    newJ = j + direction[1]
    corners.append(grid[newI][newJ])
    
  return corners in valid

def solve():

  input = open('input.txt', 'r')
  
  grid = []
  for line in input:
    grid.append(line[:-1])
    
  ans = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if centerOfXmas(i, j, grid):
        ans += 1
    
  print(ans)      

solve()