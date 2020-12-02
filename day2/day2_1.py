with open("input.txt", "r") as f:
    data = f.readlines()

numberValid = 0
for line in data:
    limits, letter, password = line.split(" ")
    letter = letter[0]
    minLim, maxLim = list(map(lambda x : int(x), limits.split("-")))
    count = 0
    for character in password:
        if character == letter:
            count +=1
    if(minLim <= count <= maxLim):
        print(f"{line} is a valid password")
        numberValid += 1
    else:
        print(f"{line} is a NOT valid password")
print(numberValid)