import numpy as np
import re
##### HAS TO BE LESS THAN 5937
# Read the text file 
file = open("Day5TestData.txt", "r")
text = file.read()

rules = re.findall(r"[0-9]{1,2}\|[0-9]{1,2}", text)
pages = re.findall(r"[0-9]{1,2},.*", text)

correctlyOrderedPages = []
incorrectlyOrderedPages = []

def checkRules(page, rules, performCorrection):
    for num in page:
        
        # Find where numbers in page appear in rules
        for rule in rules:
            rule = [int(i) for i in rule.split('|')]
 
            # If the number in pages is in the right [1] column 
            if num == rule[1]:

                if rule[0] in page and page.index(num) < page.index(rule[0]):                  
                    print("Adding to Incorrect List")
                    incorrectlyOrderedPages.append(page)
                    return
                        
            if num == page[-1]:
                print("Last Item in List - Adding to Corrected List")
                correctlyOrderedPages.append(page)
                return
        
def addMiddlePageNumbers(pagesList):
    middlePageNumbers = []
    
    for page in pagesList:
        middleIndex = len(page) // 2
        
        # If the list has an odd number of elements return the middle element
        if len(page) % 2 == 1:
            middlePageNumbers.append(page[middleIndex])
        else:
            print("Error: Even lists have no Middle Page Number")
    
    total = sum(middlePageNumbers)
    return total

for page in pages:  
    page = [int(i) for i in page.split(',')]
    
    checkRules(page, rules, False)

print(addMiddlePageNumbers(correctlyOrderedPages))

    
