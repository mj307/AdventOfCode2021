energy_level_list = []
with open("day11.txt") as fh:
    for line in fh:
        temp_level_list = []
        if line != "\n":
            for number in line:
                if number != "\n":
                    temp_level_list.append(int(number.strip("\n")))
            energy_level_list.append(temp_level_list)

for a in energy_level_list:
    print (a)


#for i in range(0,10):
# only goes in this function if a value is greater than 9. this function will do the update on values surrounding the 9 value and will update other values
# that reach up to 9 in the process. it will stop once there are no more values that are greater than 9
def checkEnergy(row,col,num_list, flashed_storage):
    if row < 0 or col < 0:
        return
    if row >= len(num_list) or col >= len(num_list[0]):
        return
    if num_list[row][col] <= 9:
        if [row,col] not in flashed_storage:
            num_list[row][col] +=1

    if num_list[row][col] > 9:
        num_list[row][col] = 0
        flashed_storage.append([row,col])
        #flashCount += 1
        checkEnergy(row + 1, col, num_list, flashed_storage) # checks value above
        checkEnergy(row - 1, col, num_list, flashed_storage) # checks value below
        checkEnergy(row, col + 1, num_list, flashed_storage) # check value to right
        checkEnergy(row, col - 1, num_list, flashed_storage) # checks value to left
        checkEnergy(row + 1, col - 1, num_list, flashed_storage) # checks value to upper-left
        checkEnergy(row - 1, col - 1, num_list, flashed_storage)  # checks value to lower-left
        checkEnergy(row + 1, col + 1, num_list, flashed_storage)  # checks value to upper-right
        checkEnergy(row - 1, col + 1, num_list, flashed_storage)  # checks value to lower-right
        return flashCount

print ("##################################")
flashCount = 0
loopCount = 1
while loopCount <= 100:
    flashed_storage = []
    for row in range(0, len(energy_level_list)):
        for col in range(0, len(energy_level_list[0])):
            if energy_level_list[row][col] == 9:
                checkEnergy(row, col, energy_level_list, flashed_storage)
            else:
                if [row,col] not in flashed_storage:
                    energy_level_list[row][col] += 1
    for a in energy_level_list:
        print (a)
        for b in a:
            if b == 0:
                flashCount +=1

    print ("")
    loopCount += 1

print (flashCount)




