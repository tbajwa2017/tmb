#Question 4 part 2
import re
from re import search
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth" ] 
num_of_good_passports=0
with open("input4a.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    list1=stripped_line
    list1=list1.split()
    #print(list1)
    sub_list=list(list1)
    
    if any("byr" in word for word in sub_list) \
   and any("iyr" in word for word in sub_list) \
   and any("eyr" in word for word in sub_list) \
   and any("hgt" in word for word in sub_list) \
   and any("hcl" in word for word in sub_list) \
   and any("ecl" in word for word in sub_list) \
   and any("pid" in word for word in sub_list):
      Valid="Y"
      for x in range(len(sub_list)): 
         #print(sub_list[x])
         if search('byr', sub_list[x]):
           #print(sub_list[x])
           byr_list=sub_list[x].split(":")
           #print(byr_list[0], byr_list[1])
           if int(byr_list[1]) < 1920 or int(byr_list[1]) > 2002:
              Valid="N"
         if search('iyr', sub_list[x]):
           #print(sub_list[x])
           iyr_list=sub_list[x].split(":")
           #print(iyr_list[0], iyr_list[1])
           if int(iyr_list[1]) < 2010 or int(iyr_list[1]) > 2020:
              Valid="N"
           #print(sub_list,Valid)
         if search('eyr', sub_list[x]):
           #print(sub_list[x])
           eyr_list=sub_list[x].split(":")
           #print(iyr_list[0], iyr_list[1])
           if int(eyr_list[1]) < 2020 or int(eyr_list[1]) > 2030:
              Valid="N"
           #print(sub_list,Valid)
         if search('ecl', sub_list[x]):
           #print(sub_list[x])
           ecl_list=sub_list[x].split(":")
           #print(iyr_list[0], iyr_list[1])
           if ecl_list[1]  not in eye_colors:
              Valid="N"
           #print(sub_list,Valid)
           #print(sub_list[x])
         if search('pid', sub_list[x]):
           pid_list=sub_list[x].split(":")
           values = re.findall(r'\b\d{9,9}\b',pid_list[1] )
           if not values:
             Valid="N"
           #print(sub_list,Valid)
         if search('hgt', sub_list[x]):
           hgt_list=sub_list[x].split(":") 
           hgt_cm = re.findall(r'\d+cm', hgt_list[1])
           hgt_in = re.findall(r'\d+in', hgt_list[1])
           if not hgt_cm and not hgt_in:
              Valid="N"
           if hgt_cm:
            hgt_cm_num = re.findall(r'\d+', hgt_cm[0])
            if int(hgt_cm_num[0]) < 150 or int(hgt_cm_num[0]) > 193:
             Valid="N"
           if hgt_in:
            hgt_in_num = re.findall(r'\d+', hgt_in[0])
            if int(hgt_in_num[0]) < 59 or int(hgt_in_num[0]) > 76:
             Valid="N"
         if search('hcl', sub_list[x]): 
          hcl_list=sub_list[x].split(":")   
          check_hcl = re.findall(r'#[0-9a-f]{6,6}', hcl_list[1])
          if not check_hcl:
           Valid="N"
          #print(sub_list,Valid)
      if Valid == "Y":
       num_of_good_passports=num_of_good_passports+1 
 
print("Number of good passports is: ", num_of_good_passports)

