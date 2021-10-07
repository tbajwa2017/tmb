#Question 4 part 1
num_of_good_passports=0
with open("input4a.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    list1=stripped_line
    list1=list1.split()
    #print(list1)
    sub_list=list(list1)
    #print(sub_list)
    if any("byr" in word for word in sub_list) \
   and any("iyr" in word for word in sub_list) \
   and any("eyr" in word for word in sub_list) \
   and any("hgt" in word for word in sub_list) \
   and any("hcl" in word for word in sub_list) \
   and  any("ecl" in word for word in sub_list)\
   and any("pid" in word for word in sub_list):
      num_of_good_passports+=1 
     #print(sub_list)
print("Number of good passports is: ", num_of_good_passports)

