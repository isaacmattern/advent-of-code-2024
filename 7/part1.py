
def validEquation(equation: list[int]) -> bool:
  """
  Args:
      equation (list[int]): List where the first int is the target total
      of the equation, and the rest of the numbers are supposed to create
      the total by adding operands '+' or '*' between them and reading the
      equation from left to right

  Returns:
      bool: False if not a valid equation, True if valid equation
  """
  
  # base case
  if len(equation) == 2:
    return equation[0] == equation[1]
  
  total = equation[0]
  nums = equation[1:]
    
  addFirstTwoNums = nums[0] + nums[1]
  multiplyFirstTwoNums = nums[0] * nums[1]
  remainingNums = []
  if len(nums) > 2:
    remainingNums = nums[2:]
  
  return (
    validEquation([total] + [addFirstTwoNums] + remainingNums)
    or validEquation([total] + [multiplyFirstTwoNums] + remainingNums)
  )

def solve():

  input = open('input.txt', 'r')
  
  equations = []
  for line in input:
    total, remaining = line.split(': ')
    remaining = remaining.removesuffix('\n') # cut off the newline character
    nums = [int(num) for num in remaining.split(' ')]
    equations.append([int(total)] + nums)
  
  ans = 0
  for equation in equations:
    if validEquation(equation):
      ans += equation[0]
    
    
  print(ans)      

solve()