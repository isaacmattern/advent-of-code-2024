def blink(stones: list[str]):
  MULTIPLIER = 2024
  newStones = []
  for stone in stones:
    if int(stone) == 0:
      newStones.append("1")
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
  
  return newStones

def solve():

  input = open('input.txt', 'r')
  
  stones = []
  for line in input:
    stones = line.split(' ')
  
  for i in range(25):
    stones = blink(stones)
  
  print(len(stones))      

solve()