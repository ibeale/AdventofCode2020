from functools import reduce
from day3_1 import Forest

if __name__ == "__main__":
    SLOPES = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    numTrees = []
    for slope in SLOPES:
        forest = Forest(0, slope)
        forest.findNumTrees()
        numTrees.append(forest.treesEncountered)
    print(reduce(lambda x, y: x*y, numTrees))




