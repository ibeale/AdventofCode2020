with open("input.txt", "r") as f:
    data = f.readlines()

data = list(map(lambda x: int(x), data))
data.sort()
TARGET = 2020

left = 0
right = len(data) - 1

while(data[left] + data[right] != TARGET):
    if data[left] + data[right] < TARGET:
        left += 1
    else:
        right -= 1
if(data[left] + data[right] == TARGET):
    print(left, right)
    print(data[left] * data[right])
else:
    print("No solution found")
