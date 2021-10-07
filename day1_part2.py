#AUTHOR: Tahir Bajwa
from itertools import permutations



with open('input2.txt', 'r') as f:
    lines = f.readlines()

numbers =[int(e.strip()) for e in lines]



#print(len(numbers))


Total_2020_records = [triplelets for triplelets in permutations(numbers, 3) if sum(triplelets) == 2020]
output=[]
for elem in Total_2020_records:
    temp = elem[0]*elem[1]*elem[2]
    output.append(temp)

print(output[0])
