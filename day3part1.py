list1 = []

with open('day3part1.txt') as fh:
    for line in fh:
        list1.append(line.strip("\n"))
length = len(list1[0])

gamma = ""
elipson = ""
for num in range(0,length):
    one_count = 0
    zero_count = 0
    for each in list1:
        if each[num] == "0":
            zero_count += 1
        else:
            one_count += 1
    if one_count > zero_count:
        gamma += "1"
        elipson += "0"
    else:
        gamma += "0"
        elipson += "1"
print(gamma)
print(elipson)
gamma_list = []
for a in gamma:
    gamma_list.append(int(a))
gamma_sum = 0
gamma_length = length -1
for value in gamma_list:
    gamma_sum += (value * pow(2,gamma_length))
    gamma_length -= 1
print (gamma_sum)


elipson_list = []
for a in elipson:
    elipson_list.append(int(a))
elipson_sum = 0
elipson_length = length -1
for value in elipson_list:
    elipson_sum += (value * pow(2,elipson_length))
    elipson_length -= 1
print (elipson_sum*gamma_sum)

