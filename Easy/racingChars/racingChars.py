import sys

lines = file(sys.argv[1], 'r')

class RaceTrack:
    def __init__(self, grid, i, j):
        self.grid = grid
        self.gridHeight = i
        self.gridWidth = j
        self.carXPos = None
        self.carYPos = None
        self.pathIndex = None

    def initializeRace(self):
        self.carYPos = self.gridHeight - 1
        for x in xrange(self.gridWidth):
            if grid[self.gridHeight - 1][x] == '_':
                self.carXPos = x
                break

    def startRace(self):
        while self.carYPos > 0:
            self.scanRoadAhead()
            self.moveCar()
        grid[self.carYPos][self.carXPos] = '|' # Leave final path mark
        
    def scanRoadAhead(self):
        if self.carXPos == 0:
            x = 0
        else:
            x = self.carXPos - 1
        while x <= self.carXPos + 1 and x < self.gridWidth:
            if grid[self.carYPos - 1][x] == 'C': # Checkpoint found
                self.pathIndex = x
                break
            elif grid[self.carYPos - 1][x] == '_': # Gate found
                self.pathIndex = x
            x += 1
            
    def moveCar(self):
        # Mark location of car with a path marker
        if self.carXPos - self.pathIndex == 1:
            grid[self.carYPos][self.carXPos] = '\\' # Turn left
        elif self.carXPos - self.pathIndex == 0:
            grid[self.carYPos][self.carXPos] = '|' # Go straight
        else:
            grid[self.carYPos][self.carXPos] = '/' # Turn right
        
        # Move car
        self.carYPos -= 1
        self.carXPos = self.pathIndex
        self.pathIndex = None

    def printPath(self):
        for row in self.grid:
            print ''.join(row)

numLines = 10 # Rows
width = 12 # Columns
grid = [[0 for j in xrange(width)] for i in xrange(numLines)] 
i = 0
j = 0

for line in lines: # Populate grid
    line = line.strip() # Remove newline char    
    while j < width:
        grid[i][j] = line[j]
        j += 1
    i += 1
    j = 0

track = RaceTrack(grid, numLines, width)
track.initializeRace()
track.startRace()
track.printPath()

