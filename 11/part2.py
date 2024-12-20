def solve():
  
  input = open('input.txt', 'r')
  
  stones = []
  for line in input:
    stones = line.split(' ')
  
  MULTIPLIER = 2024
  lookup = {}
  
  def count(stone: str, blinksLeft: int) -> int:
    if blinksLeft == 0:
      return 1
    
    result = 0
    
    if (stone, blinksLeft) in lookup:
      result = lookup[(stone, blinksLeft)]
    else:
      newStones = []
      result = 0
      if stone == "0":
        newStones = ["1"]
      elif len(stone) % 2 == 0:
        halfway = len(stone) // 2
        firstHalf = stone[:halfway:]
        secondHalf = stone[halfway::]
        
        # In the case where "999044" gets split into "999" and "044", we want to append "999" and "44"
        secondHalfTrimmed = secondHalf
        while len(secondHalfTrimmed) > 1 and secondHalfTrimmed[0] == "0":
          secondHalfTrimmed = secondHalfTrimmed.removeprefix("0")
        
        newStones.append(firstHalf)
        newStones.append(secondHalfTrimmed)
      else:
        num = int(stone)
        multipliedNum = num * MULTIPLIER
        newStones.append(str(multipliedNum))
      for newStone in newStones:
        result += count(newStone, blinksLeft - 1)
      lookup[(stone, blinksLeft)] = result
      
    return result
      
  ans = 0
  for stone in stones:
    ans += count(stone, 75)
  print(ans)  

solve()