import numpy as np

initialState = [8, 1, 3, 4, 0, 2, 7, 6, 5]
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
#Dictionary for available moves for the blank space; keys indicate the position index
dictNeighbors = {0:[1,3],1:[0,2,4],2:[1,5],3:[4,0,6],4:[3,5,1,7],5:[4,2,8],6:[7,3],7:[6,8,4],8:[7,5]}

class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval
    
    def makeChild(self):
        index = self.findZero(self.data)
        a = dictNeighbors[index]
        children = []
        for i in a:
#             print("Index to be moved to" +str(i))
            child = self.move(self.data, i, index)
#             print("Data"+str(self.data))
#             print("Child value up there"+str(child))
            childNode = Node(child, self.level+1, 0)
            #childNode.fval = fValue(childNode)
            children.append(childNode)
        return children
    
    def move(self, state, i, index):
        temp = []
        temp = self.copyList(state)
        temp2 = temp[i]
        temp[i] = temp[index]
        temp[index] = temp2
        return temp

    def copyList(self, state):
        temp = []
        for i in state:
            temp.append(i)
        return temp  
    def findZero(self, state):
        for i in range(0, 9):
            if state[i] == 0:
                return i

def manDist(state, goal):
    return sum((abs(state // 3 - goal // 3) + abs(state % 3 - goal % 3))[1:])
#Function to put the indexes of elements in a list
def coordinations(state):
    c = np.array(range(9))
    for x, y in enumerate(state):
        c[y] = x
    return c

goalCoord = coordinations(goalState)

def fValue(state):
    return manDist(coordinations(state.data), goalCoord) + state.level

oPeN = []
closed = []

initial = Node(initialState, 0 , 0)
initial.fval = fValue(initial)
oPeN.append(initial)

counter = 0
while True:
    current = oPeN[0]
    
    print("\n")
    print("CURRENT STATE: "+ str(current.data)) #+ "\nFVALUE OF CURRENT: " +str(current.fval))
    currentCoord = coordinations(current.data)
    if manDist(currentCoord, goalCoord) == 0:
        print("Found in " + str(counter) + " moves!")
        break
    for i in current.makeChild():
        i.fval = fValue(i)
#         print("Fval of children:   "+str(i.fval))
#         print("Child"+str(i.data))
        oPeN.append(i)
    closed.append(current)
    del oPeN[0]
    oPeN.sort(key = lambda x:x.fval, reverse=False)
    counter += 1