list1 = []
dict_commands = {"forward": 0, "down": 0, "up": 0}

with open('day2part1.txt') as fh:
    for line in fh:
        line_list = line.split(" ")
        if line_list[0] == "forward":
            dict_commands["forward"] = dict_commands["forward"] + int(line_list[1])
        if line_list[0] == "down":
            dict_commands["down"] = dict_commands["down"] + int(line_list[1])
        if line_list[0] == "up":
            dict_commands["up"] = dict_commands["up"] + int(line_list[1])
print (dict_commands)
depth = dict_commands["down"] - dict_commands["up"]
print (dict_commands["forward"]*depth)


