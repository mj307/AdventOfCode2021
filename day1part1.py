list1 = []
with open('day1part1.txt') as fh:
    for line in fh:
        list1.append(int(line.rstrip('\n')))

def increase(list1):
    count = 0
    most_recent_value = list1[0]
    for each in list1:
        if each > most_recent_value:
            count += 1
        most_recent_value = each
    return count
print (increase(list1))
