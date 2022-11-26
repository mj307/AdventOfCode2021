input_list = []
with open("day5.txt") as fh:
    for line in fh:
        if line != "/n":
            input_list.append(line.strip("\n"))
print (input_list)
dict_input = {}


x = input_list[-1]
temp_x = x.split(" -> ")
print (temp_x)
temp_list  = []
for a in temp_x:
    temp_list.append(a.split(","))
print (temp_list)

print ("************************************")
num1 = int(temp_list[0][0])
num2 = int(temp_list[0][1])
while num1 <= int(temp_list[1][0]):
    #print (num1, num2)
    num1 += 1
    num2 += 1

def slope(x1,y1,x2,y2):
    return ((y2-y1)/(x2-x1))

for each in input_list:
    temp_x = each.split(" -> ")
    #print(temp_x)
    temp = []
    for a in temp_x:
        temp.append(a.split(","))
    # this checks for horizontal
    if temp[0][1] == temp[1][1]:
        if int(temp[0][0]) > int(temp[1][0]):
            for i in range(int(temp[1][0]),int(temp[0][0])+1):
                print (i, temp[0][1])
                add_value = str(i) + "," + temp[0][1]
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
        else:
            for i in range(int(temp[0][0]),int(temp[1][0])+1):
                print (i, temp[0][1])
                add_value = str(i) + "," + temp[0][1]
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
    # this checks for vertical
    elif temp[0][0] == temp[1][0]:
        if int(temp[0][1]) > int(temp[1][1]):
            for i in range(int(temp[1][1]),int(temp[0][1])+1):
                print (temp[1][0],i)
                add_value = temp[1][0] + "," + str(i)
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
        else:
            for i in range(int(temp[0][1]), int(temp[1][1]) + 1):
                print(temp[1][0], i)
                add_value = temp[1][0] + "," + str(i)
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
    # this checks for diagonal
    elif slope(int(temp[0][0]),int(temp[0][1]),int(temp[1][0]),int(temp[1][1])) == 1:
        # this only works if the second x-cord is bigger than first i needa make it so that it checks both ways
        if int(temp[1][0]) > int(temp[0][0]):
            print ("first")
            #print (temp)
            num1 = int(temp[0][0])
            num2 = int(temp[0][1]) # the bigger x-coordinate
            while num1 <= int(temp[1][0]):
                print(num1, num2)
                add_value = str(num1) + "," + str(num2)
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
                num1 += 1
                num2 += 1
        else:
            print("sec")
            #print (temp)
            num1 = int(temp[0][0])
            num2 = int(temp[0][1])  # the bigger x coordinate
            while num1 >= int(temp[1][0]):
                print(num1, num2)
                add_value = str(num1) + "," + str(num2)
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
                num1 -= 1
                num2 -= 1
    elif slope(int(temp[0][0]), int(temp[0][1]), int(temp[1][0]), int(temp[1][1])) == -1:
        if int(temp[1][0]) > int(temp[0][0]):
            #print("third")
            #print (temp)
            num1 = int(temp[0][0])
            num2 = int(temp[0][1])  # the bigger x-coordinate
            while num1 <= int(temp[1][0]):
                print(num1, num2)
                add_value = str(num1) + "," + str(num2)
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
                num1 += 1
                num2 -= 1
        else:
            #print("fourth")
            #print(temp)
            num1 = int(temp[0][0]) #8
            num2 = int(temp[0][1])  #0 the bigger x-coordinate
            while num1 >= int(temp[1][0]):
                print(num1, num2)
                add_value = str(num1) + "," + str(num2)
                if add_value in dict_input:
                    dict_input[add_value] = dict_input[add_value] + 1
                else:
                    dict_input[add_value] = 1
                num1 -= 1
                num2 += 1
    print (temp)
    print (dict_input)
    print ("########")


sum = 0
for a in dict_input.values():
    if a > 1:
        sum += 1
print (sum)

