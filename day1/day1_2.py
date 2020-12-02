with open("input.txt", "r") as f:
    data = f.readlines()

data = list(map(lambda x: int(x), data))
data.sort()
TARGET = 2020

for idx, curVal in enumerate(data):
    left = idx
    right = len(data) - 1
    while(data[left] + data[right] + curVal != TARGET and left < right):
        if data[left] + data[right] + curVal < TARGET:
            left += 1
        else:
            right -= 1
    if(data[left] + data[right] + curVal == TARGET):
        print(data[left], data[right], curVal)
        print(data[left] * data[right] * curVal)
