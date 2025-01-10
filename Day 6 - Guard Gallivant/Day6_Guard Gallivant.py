import numpy as np

def createArrayFromText(filename):
    data = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        
        values = [val for val in line.rstrip('\n')]
              
        if line[len(line) - 1]:
            data.append(values)

    # Convert the list of lists to a NumPy array
    return np.array(data)

def findStartingPosition(grid, value):
    rows, cols = len(grid), len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
                if grid[row][col] == value:
                    return row, col
                    
    return None
    
def guardMap(grid):
    rows, cols = len(grid), len(grid[0])
    predictedMap = grid
    errorCount = 0

    def moveGuard(row, col, direction):
        nonlocal predictedMap
        
        if direction == 'up':
            while row > 0:    
                row -= 1
                
                if row <= 0 and grid[row][col] == '.':
                    predictedMap[row][col] = 'x'
                    print('No Obstacles! Exiting Map TOP')
                    
                elif grid[row][col] == '.':
                    predictedMap[row][col] = 'x'
                
                elif grid[row][col] == '#':
                    return moveGuard(row + 1, col, 'right')

        if direction == 'right':
            while col <= cols:    
                col += 1
                
                if col >= cols:
                    print('No Obstacles! Exiting Map RIGHT')
                    
                elif grid[row][col] == '.':
                    predictedMap[row][col] = 'x'
                
                elif grid[row][col] == '#':
                    return moveGuard(row, col - 1, 'down')
 
        if direction == 'down':
            while row < rows:    
                row += 1
               
                if row >= rows:
                    print('No Obstacles! Exiting Map DOWN')
                    
                elif grid[row][col] == '.':
                    predictedMap[row][col] = 'x'
                
                elif grid[row][col] == '#':
                    return moveGuard(row - 1, col, 'left')
                
        if direction == 'left':
            while col > 0:    
                col -= 1
                
                if col <= 0 and grid[row][col] == '.':
                    predictedMap[row][col] = 'x'
                    print('No Obstacles! Exiting Map LEFT')
                    
                elif grid[row][col] == '.':
                    predictedMap[row][col] = 'x'
                
                elif grid[row][col] == '#':
                    return moveGuard(row, col + 1, 'up')
    
    # PART 1: Predict the guard's (^) route, turning right when encountering an obstruction (#)
    stRow, stCol = findStartingPosition(grid, '^')
    # Mark starting postion with an 'x' since it is included in positions
    predictedMap[stRow][stCol] = 'x'
    
    # Move Guard (^) up, method continues moving Guard until it exits the map
    moveGuard(stRow,stCol,'up')
    
    totalPositions = np.count_nonzero(predictedMap == 'x')
    print("PART 1: Total amount of positions that the guard moved to in predicted map: ", totalPositions)

    # PART 2: Find the total amount of obstacles that can be placed to keep the Guard in a loop
    for row in range(rows):
    
        for col in range(cols):
        
            if grid[row][col] != '#':
                # Try placing an obstacle in every cell of the map
                try:
                    grid[row][col] = '#'
                    moveGuard(stRow, stCol, 'up')
                # Catch the Recursion errors (Guard getting caught in a loop) and count them   
                except Exception as e:
                    print("An error occurred:", e)
                    errorCount += 1
                
                # Change the obstacle back into a '.'
                grid[row][col] = '.'
                    
    print("PART 2: Total amount of obstacles that can be placed to keep the Guard in a loop: ", errorCount) 

grid = createArrayFromText("Day6Data.txt")
guardMap(grid)



