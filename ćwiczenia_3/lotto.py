import random

rand_num = set()

while len(rand_num) < 6:
    rand_num.add(random.randint(1,49))

sorted_list = sorted(rand_num)
str_list = [str(num) for num in sorted_list]
result = ' '.join(str_list)
    
print(result)