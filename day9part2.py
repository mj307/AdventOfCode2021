num_list = []
with open("day9.txt") as fh:
    for num_string in fh:
        temp_list = []
        for each in num_string:
            if each != "\n":
                temp_list.append(int(each.strip("\n")))
        num_list.append(temp_list)

for a in num_list:
    print (a)
print ("")


def checkLeft(num_list,row,col):
    if col == 0:
        return True
    elif num_list[row][col] < num_list[row][col-1]:
        return True
    else:
        return False

def checkRight(num_list, row, col):
    if col == len(num_list[0])-1:
        return True
    elif num_list[row][col] < num_list[row][col+1]:
        return True
    else:
        return False

def checkUp(num_list,row,col):
    if row == 0:
        return True
    elif num_list[row][col] < num_list[row-1][col]:
        return True
    else:
        return False

def checkDown(num_list,row,col):
    if row == len(num_list)-1:
        return True
    elif num_list[row][col] < num_list[row+1][col]:
        return True
    else:
        return False


risk_sum = 0
lowpoint_list = []

for row in range(0,len(num_list)):
    for col in range(0,len(num_list[0])):
        if checkUp(num_list,row,col) == True:
            if checkDown(num_list, row, col) == True:
                if checkLeft(num_list, row, col) == True:
                    if checkRight(num_list, row, col) == True:
                        temp_list = [row,col]
                        lowpoint_list.append(temp_list)
'''
this is my grid
[2, 1, 9, 9, 9, 4, 3, 2, 1, 0]
[3, 9, 8, 7, 8, 9, 4, 9, 2, 1]
[9, 8, 5, 6, 7, 8, 9, 8, 9, 2]
[8, 7, 6, 7, 8, 9, 6, 7, 8, 9]
[9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
'''
print (lowpoint_list)
basin_list = []
basin_coordinates = []
def checkPoints(row,col,num_list,num): # row and col is the value of the low points
    if row < 0 or col < 0:
        return
    if row >= len(num_list) or col >= len(num_list[0]):
        return
    if num_list[row][col] == 9:
        return
    if num_list[row][col] >= num:
        if [row,col] in basin_coordinates:
            x = 0
        else:
            basin_list.append(num_list[row][col])
            basin_coordinates.append([row,col])
            num = num_list[row][col]
            checkPoints(row, col - 1, num_list, num)
            checkPoints(row, col + 1, num_list, num)
            checkPoints(row + 1, col, num_list, num)
            checkPoints(row - 1, col, num_list, num)
            temp_list = basin_list[:]
            return len(basin_list)
    else:
        return


basin_length_list = []
for each in lowpoint_list:
    print (each)
    basin_list = []
    l = checkPoints(each[0], each[1], num_list, num_list[each[0]][each[1]])
    print (l)
    basin_length_list.append(l)


print (basin_length_list)
sorted_basin_list = (sorted(basin_length_list))
print (sorted_basin_list)

print (sorted_basin_list[-1]*sorted_basin_list[-2]*sorted_basin_list[-3])




