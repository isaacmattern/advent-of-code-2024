def solve():
  
  input = open('input.txt', 'r')
  list1 = []
  list2 = []
  
  for line in input:
    newList1Entry, _, newList2Entry = line.rpartition('   ')
    list1.append(int(newList1Entry))
    list2.append(int(newList2Entry))
  
  list1.sort()
  list2.sort()
  
  ans = 0
  for i in range(len(list1)):
    ans += abs(list1[i] - list2[i])
  
  print(ans)

solve()