import keyboard
import time
import os
import random

## Make grid larger than people can see so its easier to add shapes and the shapes can be turned without problem

class Game:
    #private
    grid = list()
    curShape = []
    curShapeName = ''
    curShapeO = ''
    score = 0

    def createGrid(self, x, y):
        #TODO: Do this a more efficient way
        for i in range(x + 5):
            self.grid.append(list())
            for j in range(y):
                if (j == 0 or j == y - 1):
                    self.grid[i].append('|')
                elif (i == x + 4):
                    self.grid[i].append('_')
                else:
                    self.grid[i].append(' ')

        self.printGrid()


    def printGrid(self):
        os.system("printf '\033c'")
        ind = 0
        for i in self.grid:
            if (ind > 4): 
                line = ''
                for j in i:
                    line = line + j
                if (ind == 5):
                    line = line + '    rows: ' + str(self.score) 
                print(line)
            ind = ind + 1


    def isGameOver(self):
        for val in self.grid[4]:
            if val == 'X':
                return True
        return False


    def moveDown(self):
        for i in range(len(self.curShape)):
            self.grid[self.curShape[i][0]][self.curShape[i][1]] = ' '
            self.curShape[i][0] = self.curShape[i][0] + 1
        
        for i in range(len(self.curShape)):
            self.grid[self.curShape[i][0]][self.curShape[i][1]] = 'X'

        self.printGrid()


    def moveRight(self):
        if self.canMoveSideways(1):
            for i in range(len(self.curShape)):
                self.grid[self.curShape[i][0]][self.curShape[i][1]] = ' '
                self.curShape[i][1] = self.curShape[i][1] + 1

            for i in range(len(self.curShape)):
                self.grid[self.curShape[i][0]][self.curShape[i][1]] = 'X'

        self.printGrid()


    def moveLeft(self):
        if self.canMoveSideways(-1):
            for i in range(len(self.curShape)):
                self.grid[self.curShape[i][0]][self.curShape[i][1]] = ' '
                self.curShape[i][1] = self.curShape[i][1] - 1

            for i in range(len(self.curShape)):
                self.grid[self.curShape[i][0]][self.curShape[i][1]] = 'X'

        self.printGrid()


    def isInShape(self, x, y):
        for part in self.curShape:
            if x == part[0] and y == part[1]:
                return True
        return False


    def isNotBlank(self, x, y):
        return self.grid[x][y] == 'X' or self.grid[x][y] == '_' or self.grid[x][y] == '|'


    def canMoveDown(self):
        for part in self.curShape:
            x = part[0] + 1
            y = part[1]
            if not self.isInShape(x, y) and self.isNotBlank(x, y):
                return False
        return True


    def canMoveSideways(self, value):
        for part in self.curShape:
            x = part[0]
            y = part[1] + value
            if not self.isInShape(x, y) and self.isNotBlank(x, y):
                return False
        return True


    def addRightL(self):
        self.grid[0][3] = 'X'
        self.grid[0][4] = 'X'
        self.grid[0][5] = 'X'
        self.grid[1][3] = 'X'
        self.curShape = [[0,3],[0,4],[0,5],[1,3]]
        self.curShapeName = 'rightL'
        self.curShapeO = 'd'


    def addLeftL(self):
        self.grid[0][3] = 'X'
        self.grid[0][4] = 'X'
        self.grid[0][5] = 'X'
        self.grid[1][5] = 'X'
        self.curShape = [[0,3],[0,4],[0,5],[1,5]]
        self.curShapeName = 'leftL'
        self.curShapeO = 'd'


    def addStick(self):
        self.grid[0][3] = 'X'
        self.grid[0][4] = 'X'
        self.grid[0][5] = 'X'
        self.grid[0][6] = 'X'
        self.curShape = [[0,3],[0,4],[0,5],[0,6]]
        self.curShapeName = 'stick'
        self.curShapeO = 'h'


    def addRightStair(self):
        self.grid[1][3] = 'X'
        self.grid[1][4] = 'X'
        self.grid[0][4] = 'X'
        self.grid[0][5] = 'X'
        self.curShape = [[1,3],[1,4],[0,4],[0,5]]
        self.curShapeName = 'rightStair'
        self.curShapeO = 'h'


    def addLeftStair(self):
        self.grid[0][3] = 'X'
        self.grid[0][4] = 'X'
        self.grid[1][4] = 'X'
        self.grid[1][5] = 'X'
        self.curShape = [[0,3],[0,4],[1,4],[1,5]]
        self.curShapeName = 'leftStair'
        self.curShapeO = 'h'


    def addMidStair(self):
        self.grid[0][4] = 'X'
        self.grid[0][5] = 'X'
        self.grid[0][6] = 'X'
        self.grid[1][5] = 'X'
        self.curShape = [[0,4],[0,5],[0,6],[1,5]]
        self.curShapeName = 'midStair'
        self.curShapeO = 'd'


    def turnShape(self):
        newCoords = []
        newO = ''
        if self.curShapeName == 'rightL':
            if self.curShapeO == 'd':
                newO = 'l'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] - 1], [self.curShape[3][0] - 2, self.curShape[3][1]]]
            
            elif self.curShapeO == 'l':
                newO = 'u'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] - 1], [self.curShape[3][0], self.curShape[3][1] + 2]]

            elif self.curShapeO == 'u':
                newO = 'r'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1] - 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] + 1], [self.curShape[3][0] + 2, self.curShape[3][1]]]

            else:
                newO = 'd'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] - 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] + 1], [self.curShape[3][0], self.curShape[3][1] - 2]]

        elif self.curShapeName == 'leftL':
            if self.curShapeO == 'd':
                newO = 'l'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] - 1], [self.curShape[3][0], self.curShape[3][1] - 2]]

            elif self.curShapeO == 'l':
                newO = 'u'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] - 1], [self.curShape[3][0] - 2, self.curShape[3][1]]]

            elif self.curShapeO == 'u':
                newO = 'r'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1] - 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] + 1], [self.curShape[3][0], self.curShape[3][1] + 2]]

            else:
                newO = 'd'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] - 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] + 1], [self.curShape[3][0] + 2, self.curShape[3][1]]]


        elif self.curShapeName == 'stick':
            if self.curShapeO == 'h':
                newO = 'v'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] - 1], [self.curShape[3][0] + 2, self.curShape[3][1] - 2]]

            else:
                newO = 'h'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1] - 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] + 1], [self.curShape[3][0] - 2, self.curShape[3][1] + 2]]


        elif self.curShapeName == 'rightStair':
            if self.curShapeO == 'h':
                newO = 'v'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] + 1], [self.curShape[3][0] + 2, self.curShape[3][1]]]

            else:
                newO = 'h'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1]], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] - 1], [self.curShape[3][0] - 2, self.curShape[3][1]]]


        elif self.curShapeName == 'leftStair':
            if self.curShapeO == 'h':
                newO = 'v'
                newCoords = [[self.curShape[0][0], self.curShape[0][1] + 2], [self.curShape[1][0] + 1, self.curShape[1][1] + 1], [self.curShape[2][0], self.curShape[2][1]], [self.curShape[3][0] + 1, self.curShape[3][1] - 1]]

            else:
                newO = 'h'
                newCoords = [[self.curShape[0][0], self.curShape[0][1] - 2], [self.curShape[1][0] - 1, self.curShape[1][1] - 1], [self.curShape[2][0], self.curShape[2][1]], [self.curShape[3][0] - 1, self.curShape[3][1] + 1]]


        else:
            if self.curShapeO == 'd':
                newO = 'l'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] - 1], [self.curShape[3][0] - 1, self.curShape[3][1] - 1]]

            elif self.curShapeO == 'l':
                newO = 'u'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1] + 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] - 1], [self.curShape[3][0] - 1, self.curShape[3][1] + 1]]

            elif self.curShapeO == 'u':
                newO = 'r'
                newCoords = [[self.curShape[0][0] + 1, self.curShape[0][1] - 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] - 1, self.curShape[2][1] + 1], [self.curShape[3][0] + 1, self.curShape[3][1] + 1]]

            else:
                newO = 'd'
                newCoords = [[self.curShape[0][0] - 1, self.curShape[0][1] - 1], [self.curShape[1][0], self.curShape[1][1]], [self.curShape[2][0] + 1, self.curShape[2][1] + 1], [self.curShape[3][0] + 1, self.curShape[3][1] - 1]]

        
        for coord in newCoords:
            if coord[0] < 0 or coord[0] > 10 or coord[1] < 0 or coord[1] > 10 or (not self.isInShape(coord[0], coord[1]) and self.isNotBlank(coord[0], coord[1])):
                return

        for i in range(len(self.curShape)):
            self.grid[self.curShape[i][0]][self.curShape[i][1]] = ' '

        self.curShape = newCoords
        self.curShapeO = newO

        for i in range(len(self.curShape)):
            self.grid[self.curShape[i][0]][self.curShape[i][1]] = 'X'

        self.printGrid()

        return


    def dealWithFullRows(self):
        scoreDelta = 0
        row = self.findLowestFull()
        while(row > -1):
            self.moveDownRowsAbove(row)
            scoreDelta = scoreDelta + 1
            row = self.findLowestFull()

        self.printGrid()
        return scoreDelta


    def findLowestFull(self):
        for i in range(len(self.grid) - 2):
            r = len(self.grid) - i - 2
            isFull = True
            for j in range(len(self.grid[r])):
                if self.grid[r][j] == ' ':
                    isFull = False
            if isFull:
                return r
        return -1


    def moveDownRowsAbove(self, row):
        for i in range(row):
            r = row - i
            for j in range(len(self.grid[r])):
                self.grid[r][j] = self.grid[r - 1][j]

        self.grid[0] = ['_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_']


    def makeMoves(self):
        keyboard.add_hotkey('left', self.moveLeft)
        keyboard.add_hotkey('right', self.moveRight)
        keyboard.add_hotkey('up', self.turnShape)
        start = time.time()
        while time.time() - start < 1.0:
            i = 0


        keyboard.clear_all_hotkeys()


    def playGame(self):
        self.createGrid(10, 10)

        while(not self.isGameOver()):
            i = random.uniform(0,1)
            
            if i < 1.0/6.0:
                self.addRightL()

            elif i < 1.0/3.0:
                self.addLeftL()

            elif i < 0.5:
                self.addStick()
                
            elif i < 2.0/3.0:
                self.addRightStair()

            elif i < 5.0/6.0:
                self.addLeftStair()

            else:
                self.addMidStair()

            while(self.canMoveDown()):
                self.makeMoves()
                self.moveDown()

            self.score = self.score + self.dealWithFullRows()

        print("Game over, score: " + str(self.score)) 


game = Game()

game.playGame()

