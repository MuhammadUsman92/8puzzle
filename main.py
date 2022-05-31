# 412305678
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.lis = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        if data['s'] not in self.lis:
            self.queue.append(data)
            self.lis.append(data['s'])

    # for popping an element based on Priority
    def delete(self):
        try:
            minCount = 0
            for i in range(len(self.queue)):
                if self.queue[i]["k"] < self.queue[minCount]["k"]:
                    minCount = i
            item = self.queue[minCount]
            del self.queue[minCount]
            return item
        except IndexError:
            print()
            exit()


def countMissPlace(dis):
    count = 0
    for key, value in dis.items():
        if key != value:
            count += 1
    if count == 1:
        return 0
    return count


def getKeyByValue(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "value doesn't exist"


def moveRight(index, state):
    new_state = state.copy()
    new_state[index], new_state[str(int(index) + 1)] = new_state[str(int(index) + 1)], new_state[index]
    return new_state


def moveLeft(index, state):
    new_state = state.copy()
    new_state[index], new_state[str(int(index) - 1)] = new_state[str(int(index) - 1)], new_state[index]
    return new_state


def moveUp(index, state):
    new_state = state.copy()
    new_state[index], new_state[str(int(index) - 3)] = new_state[str(int(index) - 3)], new_state[index]
    return new_state


def moveDown(index, state):
    new_state = state.copy()
    new_state[index], new_state[str(int(index) + 3)] = new_state[str(int(index) + 3)], new_state[index]
    return new_state


def goalAchieve(state):
    goal = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '0'}
    return goal == state


def performOperations(state):
    keyOfSpace = getKeyByValue('0', state)
    if keyOfSpace == '1':
        newRight = moveRight(keyOfSpace, state)
        rightCount = countMissPlace(newRight)
        newDown = moveDown(keyOfSpace, state)
        downCount = countMissPlace(newDown)
        myQueue.insert({"k": rightCount, 's': newRight})
        myQueue.insert({"k": downCount, 's': newDown})
        return myQueue.delete()

    elif keyOfSpace == '2':
        newRight = moveRight(keyOfSpace, state)
        rightCount = countMissPlace(newRight)
        newLeft = moveLeft(keyOfSpace, state)
        leftCount = countMissPlace(newLeft)
        newDown = moveDown(keyOfSpace, state)
        downCount = countMissPlace(newDown)
        myQueue.insert({"k": rightCount, 's': newRight})
        myQueue.insert({"k": leftCount, 's': newLeft})
        myQueue.insert({"k": downCount, 's': newDown})
        return myQueue.delete()

    elif keyOfSpace == '3':
        newLeft = moveLeft(keyOfSpace, state)
        leftCount = countMissPlace(newLeft)
        newDown = moveDown(keyOfSpace, state)
        downCount = countMissPlace(newDown)
        myQueue.insert({"k": leftCount, 's': newLeft})
        myQueue.insert({"k": downCount, 's': newDown})
        return myQueue.delete()

    elif keyOfSpace == '4':
        newRight = moveRight(keyOfSpace, state)
        rightCount = countMissPlace(newRight)
        newDown = moveDown(keyOfSpace, state)
        downCount = countMissPlace(newDown)
        newUp = moveUp(keyOfSpace, state)
        upCount = countMissPlace(newUp)
        myQueue.insert({"k": rightCount, 's': newRight})
        myQueue.insert({"k": upCount, 's': newUp})
        myQueue.insert({"k": downCount, 's': newDown})
        return myQueue.delete()

    elif keyOfSpace == '5':
        newRight = moveRight(keyOfSpace, state)
        rightCount = countMissPlace(newRight)
        newLeft = moveLeft(keyOfSpace, state)
        leftCount = countMissPlace(newLeft)
        newDown = moveDown(keyOfSpace, state)
        downCount = countMissPlace(newDown)
        newUp = moveUp(keyOfSpace, state)
        upCount = countMissPlace(newUp)
        myQueue.insert({"k": rightCount, 's': newRight})
        myQueue.insert({"k": leftCount, 's': newLeft})
        myQueue.insert({"k": downCount, 's': newDown})
        myQueue.insert({"k": upCount, 's': newUp})
        return myQueue.delete()

    elif keyOfSpace == '6':
        newLeft = moveLeft(keyOfSpace, state)
        leftCount = countMissPlace(newLeft)
        newDown = moveDown(keyOfSpace, state)
        downCount = countMissPlace(newDown)
        newUp = moveUp(keyOfSpace, state)
        upCount = countMissPlace(newUp)
        myQueue.insert({"k": leftCount, 's': newLeft})
        myQueue.insert({"k": downCount, 's': newDown})
        myQueue.insert({"k": upCount, 's': newUp})
        return myQueue.delete()

    elif keyOfSpace == '7':
        newRight = moveRight(keyOfSpace, state)
        rightCount = countMissPlace(newRight)
        newUp = moveUp(keyOfSpace, state)
        upCount = countMissPlace(newUp)
        myQueue.insert({"k": rightCount, 's': newRight})
        myQueue.insert({"k": upCount, 's': newUp})
        return myQueue.delete()

    elif keyOfSpace == '8':
        newRight = moveRight(keyOfSpace, state)
        rightCount = countMissPlace(newRight)
        newLeft = moveLeft(keyOfSpace, state)
        leftCount = countMissPlace(newLeft)
        newUp = moveUp(keyOfSpace, state)
        upCount = countMissPlace(newUp)
        myQueue.insert({"k": rightCount, 's': newRight})
        myQueue.insert({"k": leftCount, 's': newLeft})
        myQueue.insert({"k": upCount, 's': newUp})
        return myQueue.delete()

    elif keyOfSpace == '9':
        newLeft = moveLeft(keyOfSpace, state)
        leftCount = countMissPlace(newLeft)
        newUp = moveUp(keyOfSpace, state)
        upCount = countMissPlace(newUp)
        myQueue.insert({"k": leftCount, 's': newLeft})
        myQueue.insert({"k": upCount, 's': newUp})
        return myQueue.delete()


def boardPrint(state):
    print("new move")
    print("___________")
    print(f"| {state['1']}  {state['2']}  {state['3']} |")
    print(f"| {state['4']}  {state['5']}  {state['6']} |")
    print(f"| {state['7']}  {state['8']}  {state['9']} |")
    print("___________")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputValue = {'1': '5', '2': '3', '3': '2', '4': '6', '5': '0', '6': '8', '7': '7', '8': '1', '9': '4'}
    myQueue = PriorityQueue()
    while not goalAchieve(inputValue):
        inputValue = performOperations(inputValue)['s']
        boardPrint(inputValue)
