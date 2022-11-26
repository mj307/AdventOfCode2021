list2 = []

with open('day3part1.txt') as fh:
    for line in fh:
        list2.append(line.strip("\n"))

list3 = []
for a in list2:
    list3.append(a)

for b in range(0, len(list2[0])):
    zero_index_list = []
    one_index_list = []
    count_zero = 0
    count_one = 0
    for a in range(0, len(list2)):
        if list2[a][b] == "1":
            count_one += 1
            one_index_list.append(a)
        else:
            count_zero += 1
            zero_index_list.append(a)
    if count_zero > count_one:
        temp_list = []
        for each in range(0,len(list2)):
            if each in one_index_list:
                x= 0
            else:
                temp_list.append(list2[each])
        list2 = temp_list
    else:
        temp_list = []
        for each in range(0, len(list2)):
            if each in zero_index_list:
                x = 0
            else:
                temp_list.append(list2[each])
        list2 = temp_list
    #print (list2)

#print ("####")
print (int(list2[0],2))
print ("########################################")

for b in range(0, len(list3[0])): # length of each binary number
    zero_index_list = []
    one_index_list = []
    count_zero = 0
    count_one = 0
    for a in range(0, len(list3)): # length of list
        if list3[a][b] == "1":
            count_one += 1
            one_index_list.append(a)
        else:
            count_zero += 1
            zero_index_list.append(a)
    #print (count_zero, count_one)
    if count_zero > count_one:
        temp_list = []
        for each in range(0,len(list3)):
            if each in zero_index_list:
                x= 0
            else:
                temp_list.append(list3[each])
        list3 = temp_list
    else:
        temp_list = []
        for each in range(0, len(list3)):
            if each in one_index_list:
                x = 0
            else:
                temp_list.append(list3[each])
        list3 = temp_list
    #print (list3)
    if len(list3) == 1:
        break

#print ("####")
print (int(list3[0],2))

print (int(list3[0],2) * int(list2[0],2) )