#  File: ISBN.py

#  Description: Validate a collection of ISBNs

#  Student Name: Courntey C. Thomas

#  Student UT EID: cct685

#  Course Name: CS 303E

#  Unique Number: 1

#  Date Created: 4/2/2016

#  Date Last Modified: 4/2/2016

import os.path
import sys

def removeHyphens(line):
  result = []
  for char in line:
    if char != '-':
      result.append(groom(char))
  return result

def allNumeric(line):
  for char in line:
    if char.isdigit() == True:
      continue
    else:
      return False
  return True
    
def groom(char):
  if char.upper() == 'X':
    return '10'
  return char.upper()

def withInRange(line):
  for char in line:
    if int(char) < 0 or int(char) > 10:
      return False
  return True

def validateLength(line):
  if len(line) != 10:
    return False
  else:
    return True

def cummulativeSum(line):
  result = list()
  for i in range(0,10):
      if i == 0:
        result.insert(i, int(line[i]))
      else:
        result.insert(i, result[i-1] + int(line[i]))
  return result

def isDivisibleBy11(chechsum):
  if chechsum % 11 == 0:
    return True
  else:
    return False
    
def longest(lines):
  result = 0
  for line in lines:
    if len(line) > result:
      result = len(line)
  return result
  
def main():
  INFILE = 'isbn.txt'
  OUTFILE = 'isbnOut.txt'
  if os.path.exists(INFILE) == False:
    print('Please ensure', INFILE, 'is located in the same directory as this program')
    sys.exit()
  file = open(INFILE, 'r')
  lines = [line.strip() for line in file]
  file.close()

  # find longest for padding during printing
  padding = longest(lines)
  
  file = open(OUTFILE, 'w')
   
  for line in lines:
    groomed = removeHyphens(list(line))
    if validateLength(groomed) == False or allNumeric(groomed) == False or withInRange(groomed) == False:
      print(line.ljust(padding), ' invalid')
      file.write(line.ljust(padding) + ' invalid' + '\n')
      continue
      
    s1 = cummulativeSum(groomed)
    s2 = cummulativeSum(s1)

    if isDivisibleBy11(s2[9]) == False:
      print(line.ljust(padding), ' invalid')
      file.write(line.ljust(padding) + ' invalid' + '\n')
      continue
      
    print(line.ljust(padding), ' valid')
    file.write(line.ljust(padding) + ' valid' + '\n')
      
    ##print(groomed)
    ##print(s1)
    ##print(s2)
    ##print(isDivisibleBy11(s2[9]))

  file.close()

main()

##0-1315-2447-X  valid
##0-89237-010-9  invalid
