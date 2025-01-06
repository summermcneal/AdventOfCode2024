from collections import defaultdict
import re

# Read the text file 
file = open("Day5Data.txt", "r")
text = file.read()

rules = re.findall(r"[0-9]{1,2}\|[0-9]{1,2}", text)
pages = re.findall(r"[0-9]{1,2},.*", text)

correctlyOrderedPages = []
incorrectlyOrderedPages = []
newCorrectlyOrderedPages = []
setBeforePages = defaultdict(set)

# Puts a page in the Correct or Incorrectly Ordered Lists
def markPageAsCorrectOrIncorrect(page):

    for index, num in enumerate(page):
        # The Length of numbers that come before "num" AND are included on the page
        # This Length determines the order (or index) that the numbers should be in
        orderOfNumOnPage = len(setBeforePages[num] & set(page))
            
        if index != orderOfNumOnPage:
            incorrectlyOrderedPages.append(page)
            return  
  
    correctlyOrderedPages.append(page)
    
# Adds the middle index value of multiple lists
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

# Create dictonary of rules where every number in rules is a key with a set of numbers that comes before it
for rule in rules:           
    rule = [int(i) for i in rule.split('|')]
    comesBefore, comesAfter = int(rule[0]), int(rule[1])
    setBeforePages[comesAfter].add(comesBefore)
    
# PART 1: Find Correctly Ordered Updates (Pages) 
for page in pages:
    page = [int(i) for i in page.split(',')]
    markPageAsCorrectOrIncorrect(page)
    
print("PART 1: Sum of Middle Numbers in Correctly Ordered Updates: ", addMiddlePageNumbers(correctlyOrderedPages))

# PART 2: Correct Order of Incorrectly Ordered Updates (Pages)
for page in incorrectlyOrderedPages:
    newPage = []

    for i in range(len(page)):
        for num in page:
            # The Length of numbers that come before "num" AND are included on the page
            # This Length determines the order (or index) that the numbers should be in
            orderOfNumOnPage = len(setBeforePages[num] & set(page))
            
            if i == orderOfNumOnPage:
                newPage.append(num)
                break

    newCorrectlyOrderedPages.append(newPage)
            
print("PART 2: Sum of Middle Numbers in Newly Corrected Ordered Updates: ", addMiddlePageNumbers(newCorrectlyOrderedPages))


    
