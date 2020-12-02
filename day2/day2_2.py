with open("input.txt", "r") as f:
    data = f.readlines()

numberValid = 0
for line in data:
    limits, letter, password = line.split(" ")
    letter = letter[0]
    minLim, maxLim = list(map(lambda x : int(x), limits.split("-")))
    if not minLim > 0 and minLim < maxLim <= len(password):
        print(f"{line} is a NOT valid password, index out of range")
    else:
        if((password[minLim - 1] == letter) != (password[maxLim - 1] == letter)):
            numberValid += 1
            print(f"{line} is a valid password")
        else:
            print(f"{line} is a NOT valid password")
print(numberValid)