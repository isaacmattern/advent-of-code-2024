def inGrid(i: int, j: int, grid: list[list[int]]) -> int:
  validI = 0 <= i < len(grid)
  validJ = 0 <= j < len(grid[0])
  
  return validI and validJ

def startOfXmas(i: int, j: int, grid: list[list[int]]) -> int:
  if grid[i][j] != 'X':
    return 0
  
  total = 0
  directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
  remaining = ['M', 'A', 'S']
  
  for direction in directions:
    newI, newJ = i, j
    valid = True
    for letter in remaining:
      newI = newI + direction[0]
      newJ = newJ + direction[1]
      
      if (not inGrid(newI, newJ, grid)) or grid[newI][newJ] != letter:
        valid = False
        break
      
    if valid:
      total += 1
  
  return total

def solve():

  input = open('input.txt', 'r')
  
  grid = []
  for line in input:
    grid.append(line[:-1])
    
  ans = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      ans += startOfXmas(i, j, grid)
    
  print(ans)      

solve()