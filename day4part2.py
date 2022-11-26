num_list = []
# creates number list
with open('day4part1.txt') as fh:
    for line in fh:
        num_list = line.split(",")
        num_list[-1] = num_list[-1].strip("\n")
        break

all_board_list = []
# creates list with boards
with open('day4part1.txt') as fh:
    x = 0
    row_list = []
    board_list = []
    count = 0
    for line in fh:
        if x == 0:
            x = 1
        else:
            temp_mini_list = line.split(" ")
            mini_list = []
            for each in temp_mini_list:
                if each != "":
                    mini_list.append(each.strip("\n"))
            if len(mini_list) > 1:
                board_list.append(mini_list)
                count += 1
            if count == 5:
                all_board_list.append(board_list)
                board_list = []
                count = 0

for each in all_board_list:
    print (each)
print ("CODE OUTPUT BEGINS HERE")

def checkHorizontal(board_list):
    for each_row in board_list:
        x_count = 0
        for a in each_row:
            if a == "x":
                x_count += 1
        if x_count == 5:
            return True

def checkVertical(board_list):
    x_count = 0
    for col in range(0, len(board_list)):
        for row in range(0, len(board_list)):
            if board_list[row][col] == "x":
                x_count += 1
        if x_count == 5:
            return True
        else:
            x_count = 0


def changeX(number, board_list): # do this for each row in the master list of all boards
    for row in range(0,len(board_list)):
        for col in range(0, len(board_list)):
            if board_list[row][col] == number:
                board_list[row][col] = "x"



def result(each_board, number):
    sum = 0
    for row in range(0, len(each_board)):
        for col in range(0, len(each_board)):
            if each_board[row][col] != "x":
                if each_board[row][col] != "xt":
                    print ("each number added to sum:" + each_board[row][col].strip("t"))
                    sum += int(each_board[row][col].strip("t"))
    print(sum)
    print(number)
    return sum * int(number)

def check(temp_num_list, all_board_list):
    big_list_length = len(all_board_list)
    for number in temp_num_list:
        for each_board in all_board_list[:]:
            changeX(number, each_board)
            if checkVertical(each_board) == True:
                if len(all_board_list) == 1:
                    return (result(each_board, number))
                else:
                    all_board_list.remove(each_board)

            elif checkHorizontal(each_board) == True:
                if len(all_board_list) == 1:
                    return (result(each_board, number))
                else:
                    all_board_list.remove(each_board)




print("###")
print (check(num_list, all_board_list))

