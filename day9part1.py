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

risk_sum = 0

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



for row in range(0,len(num_list)):
    for col in range(0,len(num_list[0])):
        if checkUp(num_list,row,col) == True:
            if checkDown(num_list, row, col) == True:
                if checkLeft(num_list, row, col) == True:
                    if checkRight(num_list, row, col) == True:
                        risk_sum += num_list[row][col] + 1
print (risk_sum)