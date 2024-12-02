def solve():
  
  input = open('input.txt', 'r')
  list1 = []
  list2 = []
  
  for line in input:
    newList1Entry, _, newList2Entry = line.rpartition('   ')
    list1.append(int(newList1Entry))
    list2.append(int(newList2Entry))
    
  occurrences = {}
  
  for num in list1:
    occurrences[num] = 0
    
  for num in list2:
    if num in occurrences.keys():
      occurrences[num] += 1
      
  ans = 0
  for num in list1:
    ans += num * occurrences[num]
    
  print(ans)   

solve()