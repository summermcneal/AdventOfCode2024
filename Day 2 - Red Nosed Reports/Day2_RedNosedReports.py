import pandas as pd
import numpy as np
import math

# Read the CSV file into a DataFrame
df = pd.read_csv('Day2Data.csv')

totalSafeReports = 0
totalSafeReportsWithDampener = 0

# PART 1: Mark reports as Safe if level differences meet requirements
def safetyCheck(report):  

    levelDiffs = np.diff(report)
    print(levelDiffs)
    
    if np.all(levelDiffs >= 1) and np.all(levelDiffs <= 3):
        return True
        
    elif np.all(levelDiffs <= -1) and np.all(levelDiffs >= -3):
        return True
  
    else:
        return False

# PART 2: Allow one bad level per Report with Problem Dampener
def allowSingleBadLevel(report):

    reportSafetyBeforeDampener = safetyCheck(report)
    print(report)
    
    if reportSafetyBeforeDampener == False:
        
        for level in range(len(report)):
            
            if safetyCheck(np.delete(report, [level])):
                return True
    
        return False
                
    return reportSafetyBeforeDampener

# Get the total number of rows (Reports)
numOfReports = len(df)

for report in range(numOfReports):
    print("-------------------REPORT------------------->", report)
    
    # Convert the row (Report) to a list
    reportList = df.iloc[report].tolist()
    
    # Remove null values from ReportList
    reportList = [x for x in reportList if not math.isnan(x)]

    totalSafeReports += safetyCheck(reportList)
    totalSafeReportsWithDampener += allowSingleBadLevel(reportList)

print("(PART 1) TOTAL SAFE REPORTS: ", totalSafeReports)
print("(PART 2) TOTAL SAFE REPORTS WITH PROBLEM DAMPENER: ", totalSafeReportsWithDampener)