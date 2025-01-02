import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C://Users//Summer//Documents//Advent of Code 2024//Day1Data.csv')

# Access the column as a list
list1 = df['Col1'].tolist()
list2 = df['Col2'].tolist()

list1.sort()
list2.sort()

sumDifference = 0

# PART 1: Loop through lists and get difference in each row
for i in range(len(list1)):
    sumDifference += abs(list1[i] - list2[i])
    
print(sumDifference)

multiplier = 0
sumSimilarity = 0

# Part 2: Loop through lists and get similarity score
for int1 in list1:
    print("int1: ", int1)
    
    for int2 in list2:
        print("int2: ", int2)
        
        if int1 == int2:
            multiplier += 1
            
    print("multiplier: ", multiplier)
    
    sumSimilarity += int1 * multiplier
    multiplier = 0
    
print(sumSimilarity)
            