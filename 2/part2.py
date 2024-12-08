def safe(nums: list[int]):
  for i in range(len(nums)):
    trimmedNums = nums[0:i] + nums[i+1:]
    
    if len(trimmedNums) < 2:
      return True
    
    increasing = True
    if trimmedNums[1] < trimmedNums[0]:
      increasing = False
    
    for i in range(1, len(trimmedNums)):
      diff = trimmedNums[i] - trimmedNums[i-1]
      if increasing:
        if not (0 < diff <= 3):
          break
      else:
        if not (-3 <= diff < 0):
          break
        
      if i == len(trimmedNums) - 1:
        return True
      
  return False

def solve():
  
  input = open('input.txt', 'r')
  
  ans = 0
  for line in input:
    nums = [int(num) for num in line.split(' ')]
    if safe(nums):
      ans += 1    
  
  print(ans)

solve()