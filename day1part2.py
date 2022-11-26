list1 = []
with open('day1part1.txt') as fh:
    for line in fh:
        list1.append(int(line.rstrip('\n')))
# the program asks to compare sums of every 3 values in the list. I found the sums of each 3 values and stored it, and used this stored
# value to compare to the sum of the next 3 values so i could see whether the sums were increasing or not. (sliding window)
def sumIncrease(list1):
    count  = 0
    most_recent_sum = list1[0] + list1[1] + list1[2]
    for each in range(0, len(list1)-2):
        sum = list1[each] + list1[each+1] + list1[each+2]
        if sum > most_recent_sum:
            count += 1
        most_recent_sum = sum
    return count
print (sumIncrease(list1))