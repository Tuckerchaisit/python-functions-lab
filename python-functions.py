#Challenge1
def sum_to(num):
  sum = 0
  temp =1
  while temp<(num+1):
    sum+=temp
    temp+=1
  return sum

#Challenge2
def largest(num_list):
  num_list.sort()
  return num_list[len(num_list)-1]

print(largest([1,2,3,4,6,5]))

