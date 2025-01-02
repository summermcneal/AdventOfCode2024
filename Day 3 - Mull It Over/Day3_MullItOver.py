import re

# Read the text file 
file = open("Day3Data.txt", "r")
text = file.read()

# Define Mul as the Multiplicaton of two integers
def mul(a, b):
  return a * b

# Finds the sum of Mul Pattern in the file based on Regex Input
def mulPatternScan(mul_pattern):
    result = 0
    state = "enabled"
    
    mul_match = re.findall(mul_pattern, text)
    
    for match in mul_match:   
        if (match == "don't()"):
            state = "disabled"
            continue
        
        elif (match == "do()"):
            state = "enabled"
            continue
            
        if (state == "enabled"):
            result += eval(match)
    
    return result

mul_pattern_part1 = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
mul_pattern_part2 = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
  
print("(PART 1) SUM OF MULS: ", mulPatternScan(mul_pattern_part1))
print("(PART 2) SUM OF DO() MULS: ", mulPatternScan(mul_pattern_part2))