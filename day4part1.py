num_list = []
# creates number list
with open('day4part1.txt') as fh:
    for line in fh:
        num_list = line.split(",")
        num_list[-1] = num_list[-1].strip("\n")
        print (num_list)
        break

#print (num_list)
print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

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
                #print (number, row, col)
                #print (board_list[row][col])



#temp_num_list = ['7', '4', '9', '5', '11', '17', '23', '2', '0', '14', '21',"24","10", "16"]
def check(temp_num_list, all_board_list):
    for number in temp_num_list:
        for each_board in all_board_list:
            changeX(number, each_board)
            if checkVertical(each_board) == True:
                print ("Vertical Winner")
                sum = 0
                for row in range(0, len(each_board)):
                    for col in range(0, len(each_board)):
                        if each_board[row][col] != "x":
                            sum += int(each_board[row][col])
                #print(sum)
                return sum * int(number)
            elif checkHorizontal(each_board) == True:
                print ("Horizontal Winner")
                sum = 0
                for row in range(0, len(each_board)):
                    for col in range(0, len(each_board)):
                        if each_board[row][col] != "x":
                            sum += int(each_board[row][col])
                #print(sum)
                return sum * int(number)

print (check(num_list, all_board_list))

