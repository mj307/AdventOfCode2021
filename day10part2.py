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

#for a in lines_characters_list:
    #print (a)


def checkIllegal(character_list):
    legal_character_list = []
    for character in range(0,len(character_list)):
        #print ("####")
        #print (legal_character_list)
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





def removePairs(character_list):
    legal_character_list = []
    for character in range(0, len(character_list)):
        # print ("####")
        # print (legal_character_list)
        if character == 0:
            legal_character_list.append(character_list[character])
        else:
            if character_list[character] == "[" or character_list[character] == "{" or character_list[character] == "<" or character_list[character] == "(":
                legal_character_list.append(character_list[character])

            elif character_list[character] == "]":
                if legal_character_list[-1] == "[":
                    legal_character_list.pop()

            elif character_list[character] == "}":
                if legal_character_list[-1] == "{":
                    legal_character_list.pop()

            elif character_list[character] == ")":
                if legal_character_list[-1] == "(":
                    legal_character_list.pop()

            elif character_list[character] == ">":
                if legal_character_list[-1] == "<":
                    legal_character_list.pop()
    return legal_character_list

print ("")
l = ['[', '(', '{', '(', '<', '(', '(', ')', ')', '[', ']', '>', '[', '[', '{', '[', ']', '{', '<', '(', ')', '<', '>', '>']

incomplete_list = []
for each in lines_characters_list:
    if (checkIllegal(each)==None):
        incomplete_list.append(each)

scores_list = []
for each in incomplete_list:
    output = removePairs(each)
    print (output)
    output.reverse()
    print (output)
    score = 0
    for a in output:
        score *= 5
        if a == "(":
            score += 1
        elif a == "[":
            score += 2
        elif a == "{":
            score += 3
        elif a == "<":
            score += 4
    scores_list.append(score)

sorted_scores_list = sorted(scores_list)
print (sorted_scores_list)

print (sorted_scores_list[int(len(sorted_scores_list)/2)])
