import collections

def inBounds(point: tuple[int], height: int, width: int) -> bool:
  if point[0] < 0 or point[0] >= height:
    return False
  if point[1] < 0 or point[1] >= width:
    return False
  
  return True

def solve():

  input = open('input.txt', 'r')
  
  grid = []
  for line in input:
    trimmedLine = line.removesuffix('\n')
    grid.append(trimmedLine)
    
  height = len(grid)
  width = len(grid[0])
  
  antennaLists = collections.defaultdict(list)
  
  for i in range(height):
    for j in range(width):
      character = grid[i][j]
      if character != '.':
        antennaLists[character].append((i, j))
  
  # overlapping antinodes only count as one 'space' in the answer:
  # "How many unique locations within the bounds of the map contain an antinode?"
  antinodeSet = set()
  for character in antennaLists.keys():
    antennas = antennaLists[character]
    for a in range(len(antennas) - 1):
      for b in range(len(antennas)):
        if a != b:
          antenna1 = antennas[a]
          antenna2 = antennas[b]
          
          diff = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
          antinode1 = (antenna2[0] + diff[0], antenna2[1] + diff[1])
          antinode2 = (antenna1[0] - diff[0], antenna1[1] - diff[1])
          
          if inBounds(antinode1, height, width):
            antinodeSet.add(antinode1)
          if inBounds(antinode2, height, width):
            antinodeSet.add(antinode2)
          
  print(len(antinodeSet))      

solve()