
dict_commands = {"forward": 0, "depth": 0, "aim": 0}

with open('day2part1.txt') as fh:
    for line in fh:
        line_list = line.split(" ")
        if line_list[0] == "forward":
            dict_commands["forward"] = dict_commands["forward"] + int(line_list[1])
            dict_commands["depth"] = (dict_commands["aim"] * int(line_list[1])) + dict_commands["depth"]
        if line_list[0] == "down":
            dict_commands["aim"] = dict_commands["aim"] + int(line_list[1])
        if line_list[0] == "up":
            dict_commands["aim"] = dict_commands["aim"] - int(line_list[1])
print (dict_commands["forward"] * dict_commands["depth"])