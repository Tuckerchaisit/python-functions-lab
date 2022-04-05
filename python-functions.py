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

#Challenge3
def occurances(string, substr):
  return string.count(substr)
