def getStart(grid: list[list[chr]]) -> tuple[int]:
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '^':
        return (i, j)
      
def inBounds(i, j, width, height) -> bool:
  if i < 0 or i >= height:
    return False
  elif j < 0 or j >= width:
    return False
  else:
    return True

def solve():

  input = open('input.txt', 'r')
  
  grid = []
  for line in input:
    grid.append(line[:-1])
    
  i, j = getStart(grid)
  width = len(grid[0])
  height = len(grid)
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  currDirection = 0
  seen = set[tuple]()
  
  while True:
    if (i, j) not in seen:
      seen.add((i, j))
    newI = i + directions[currDirection][0]
    newJ = j + directions[currDirection][1]
    
    if inBounds(newI, newJ, width, height):
      if grid[newI][newJ] == '#':
        currDirection += 1
        if currDirection > 3:
          currDirection = 0
      else:
        i = newI
        j = newJ
    else:
      break
        
  print(len(seen))      

solve()