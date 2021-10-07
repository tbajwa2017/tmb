with open("input.txt", "r") as a_file:
  num_of_good_passwords=0
  for line in a_file:
    stripped_line = line.strip()
    list1=stripped_line
    list1=list1.split()
    str1=list1[1].rstrip(":")
    #print(list1[2].count(str1))
    #sub_list1=list(list1[2])
    #print(sub_list1)
    #print(list1[2])
    list_min_max=(list1[0].split('-'))
    #print(list_min_max[0], list_min_max[1])
    if  list1[2].count(str1) >= int(list_min_max[0]) and list1[2].count(str1) <= int(list_min_max[1]):
      num_of_good_passwords+=1
  print("Number of good passwords is: ", num_of_good_passwords)
