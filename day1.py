list1 = [199,200,208,210,200,207,240,269,260,263]

def increase(list1):
    count = 0
    most_recent_value = list1[0]
    for each in list1:
        if each > most_recent_value:
            count +=1
        most_recent_value = each
    return count

print (increase(list1))