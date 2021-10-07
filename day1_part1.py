#AUTHOR: Tahir Bajwa
from itertools import permutations



with open('input2.txt', 'r') as f:
    lines = f.readlines()

numbers =[int(e.strip()) for e in lines]



#print(len(numbers))


Total_2020_records = [pair for pair in permutations(numbers, 2) if sum(pair) == 2020]
output=[]
for elem in Total_2020_records:
    temp = elem[0]*elem[1]
    output.append(temp)

print(output[0])
