def safe(nums: list[int]):
  if len(nums) == 1:
    return True
  
  increasing = True
  if nums[1] < nums[0]:
    increasing = False
    
  for i in range(1, len(nums)):
    diff = nums[i] - nums[i-1]
    if increasing:
      if not (0 < diff <= 3):
        return False
    else:
      if not (-3 <= diff < 0):
        return False
      
  return True

def solve():
  
  input = open('input.txt', 'r')
  
  ans = 0
  for line in input:
    nums = [int(num) for num in line.split(' ')]
    if safe(nums):
      ans += 1    
  
  print(ans)

solve()