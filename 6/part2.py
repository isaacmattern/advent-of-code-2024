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

  input = open('exampleInput.txt', 'r')
  
  grid = []
  for line in input:
    grid.append(line[:-1])
    
  i, j = getStart(grid)
  width = len(grid[0])
  height = len(grid)
  directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  currDirection = 0
  threeAgo = (-1, -1)
  twoAgo = (-1, -1)
  oneAgo = (-1, -1)
  validPlaceToPutObstacle = 0
  
  while True:
    newI = i + directions[currDirection][0]
    newJ = j + directions[currDirection][1]
    
    if inBounds(newI, newJ, width, height):
      if grid[newI][newJ] == '#':
        currDirection += 1
        if currDirection > 3:
          currDirection = 0 
          
        threeAgo = twoAgo
        twoAgo = oneAgo
        oneAgo = (i, j)
      else:
        
        if (i == threeAgo[0] and j == oneAgo[1]) or (i == oneAgo[0] and j == threeAgo[1]):
          print(newI, newJ)
          validPlaceToPutObstacle += 1
        
        i = newI
        j = newJ
        
    else:

      break
    

        
  print(validPlaceToPutObstacle)      

solve()