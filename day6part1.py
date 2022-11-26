days_list_str = []
with open ("day6part1.txt") as fh:
    for a in fh:
        if a != "\n":
            days_list_str = a.strip("\n").split(",")
#print (days_list_str)
days_list = []
for each in days_list_str:
    days_list.append(int(each))

#print (days_list)
days_count = 0
while days_count < 256:
    print (days_count)
    for fish_days in days_list[:]:
        if fish_days == 0:
            #temp_fish_days = 6
            days_list.remove(fish_days)
            days_list.append(6)
            days_list.append(8)
        else:
            days_list.remove(fish_days)
            days_list.append(fish_days-1)
    days_count += 1
    #print (days_list)

print (len(days_list))


