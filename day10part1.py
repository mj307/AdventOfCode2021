lines_list = []
with open("day10.txt") as fh:
    for line in fh:
        if line != "\n":
            lines_list.append(line.strip("\n"))

for a in lines_list:
    print (a)

lines_characters_list = []
for each in lines_list:
    temp_list = []
    for character in each:
        temp_list.append(character)
    lines_characters_list.append(temp_list)



tlist = ['{', '(', '[', '(', '<', '{', '}', '[', '<', '>', '[', ']', '}', '>', '{', '[', ']', '{', '[', '(', '<', '(', ')', '>']
# all the illegal values will start out at 0
def checkIllegal(character_list):
    legal_character_list = []
    for character in range(0,len(character_list)):
        print ("####")
        print (legal_character_list)
        if character == 0:
            legal_character_list.append(character_list[character])
        else:
            if character_list[character] == "[" or character_list[character] == "{" or character_list[character] == "<" or character_list[character] == "(":
                legal_character_list.append(character_list[character])

            elif character_list[character] == "]":
                if legal_character_list[-1] == "[":
                    legal_character_list.pop()
                elif legal_character_list[-1] == "{" or legal_character_list[-1] == "(" or legal_character_list[-1] == "<":
                    return "]"

            elif character_list[character] == "}":
                if legal_character_list[-1] == "{":
                    legal_character_list.pop()
                elif legal_character_list[-1] == "[" or legal_character_list[-1] == "(" or legal_character_list[-1] == "<":
                    return "}"

            elif character_list[character] == ")":
                if legal_character_list[-1] == "(":
                    legal_character_list.pop()
                elif legal_character_list[-1] == "{" or legal_character_list[-1] == "[" or legal_character_list[-1] == "<":
                    return ")"

            elif character_list[character] == ">":
                if legal_character_list[-1] == "<":
                    legal_character_list.pop()
                elif legal_character_list[-1] == "{" or legal_character_list[-1] == "(" or legal_character_list[-1] == "[":
                    return ">"
    return

#print (checkIllegal(tlist))
inc = ['[', '(', '{', '(', '<', '(', '(', ')', ')', '[', ']', '>', '[', '[', '{', '[', ']', '{', '<', '(', ')', '<', '>', '>']
#print (checkIllegal(inc))



illegal_dict = {"]":0, "}":0, ">":0, ")":0}
for each in lines_characters_list:
    print ("#####")
    print (each)
    print (checkIllegal(each))
    if checkIllegal(each) == "]":
        print ("here ]")
        illegal_dict["]"] += 1

    if checkIllegal(each) == "}":
        print("here }")
        illegal_dict["}"] += 1

    if checkIllegal(each) == ")":
        print("here )")
        illegal_dict[")"] += 1

    if checkIllegal(each) == ">":
        print("here >")
        illegal_dict[">"] += 1

print (illegal_dict)
sum = (illegal_dict["]"]*57) + (illegal_dict["}"]*1197) + (illegal_dict[")"]*3) + (illegal_dict[">"]*25137)
print (sum)
