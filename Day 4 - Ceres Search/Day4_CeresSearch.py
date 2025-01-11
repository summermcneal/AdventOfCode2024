import numpy as np

data = np.genfromtxt("Day4Data.txt", delimiter=1, dtype='str')

allDirections = [-1, 0, 1]
diagDirections = [-1, 1]

# Searches for a word in a grid, including diagonals and reverse.
def wordSearch(grid, word, directions, searchType):
    rows, cols = len(grid), len(grid[0])
    countWordsFound = 0
    coordinates = []
    centerX = 'None'
    centerY = 'None'
    
    # Check if the word exists starting with (row, col) in directions (dRow, dCol).
    def checkDirection(row, col, word, dRow, dCol):
        
        # For search type "X-Mas Puzzle" store coordinates of "A" in successfully found words. 
        if word == "":
            nonlocal centerX, centerY
        elif word[0] == 'A':
            centerX, centerY = row, col
        
        # Word Found: If a word is found it will be sliced down to zero
        if len(word) == 0:
            print("-----WORD FOUND-----> row,col: ", row, ", ",col)
            coordinates.append([centerX, centerY])
            return True
        
        # Incorrect Letter: Return to search in a different direction
        elif row < 0 or row >= rows or col < 0 or col >= cols:
            print("-----OUT OF BOUNDS-----> row,col: ", row, ", ",col)
            return False
        
        # Out of Bounds: Return to search in a different direction
        elif grid[row][col] != word[0]:
            print("-----INCORRECT LETTER-----> row,col: ", row, ", ",col)
            return False
        
        newRow = row + dRow
        newCol = col + dCol
        
        # After a letter is found, slice it and continue searching in other directions
        return checkDirection(newRow, newCol, word[1:], dRow, dCol)

    for row in range(rows):
        for col in range(cols):
            for dRow in directions:
                for dCol in directions:
                    if dRow == 0 and dCol == 0:
                        continue  # Skip - Not Moving
                    if checkDirection(row, col, word, dRow, dCol):
                        countWordsFound += 1

    if searchType == "Puzzle":     
        # Find unique "A" coodinates and count how many times they appear 
        uniqueCoords, counts = np.unique(coordinates, axis=0, return_counts=True)
        # If any "A" coordinates are the same, they have crossed to make the "X-Mas Puzzle"
        duplicateCoords = np.count_nonzero(counts > 1)
        
        return duplicateCoords

    if searchType == "Word":
        return countWordsFound
        
# PART 1: Searches for a word in a grid, including diagonals and reverse.
word = "XMAS"
xmasWordSearch = wordSearch(data, word, allDirections, "Word")

# PART 2: Searches for two instances of the same word in a grid that cross one another to make an "X" shape.
puzzle = "MAS"
xmasPuzzleSearch = wordSearch(data, puzzle, diagDirections, "Puzzle")

print("(PART 1) TOTAL TIMES 'XMAS' APPEARS: ", xmasWordSearch)
print("(PART 2) TOTAL TIMES 'X-MAS' APPEARS: ", xmasPuzzleSearch)
