class Forest:
    def __init__(self, startX, slope):
        with open("input.txt", "r") as f:
            self.forest = list(map(lambda x: x.strip(), f.readlines()))
        self.curX = startX
        self.slope = slope
        self.height = len(self.forest)
        self.width = len(self.forest[0])
        self.treesEncountered = 0

    def findNumTrees(self):
        print(self.width)
        for i in range(0, self.height, self.slope[1]):
            if self.forest[i][self.curX] == "#":
                print(f"hit tree at position {self.curX} on line {i}")
                print("".join([" " if x != self.curX else "*" for x in range(self.width)]))
                print(self.forest[i])
                self.treesEncountered += 1
            else:
                print(f"no tree at position {self.curX} on line {i}")
                print("".join([" " if x != self.curX else "*" for x in range(self.width)]))
                print(self.forest[i])
            if self.curX + self.slope[0] >= self.width:
                self.curX = self.slope[0] - (self.width - self.curX)
            else:
                self.curX += self.slope[0]

if __name__ == "__main__":
    forest = Forest(0, (3,1))
    forest.findNumTrees()
    print(forest.treesEncountered)




