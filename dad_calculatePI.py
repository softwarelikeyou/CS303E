#  File: CalculatePI.py

#  Description: 

#  Student Name: 

#  Student UT EID:

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import math
import random

def computePI (numThrows):
    hits = 0;
    for index in range(0, numThrows):
        xPos = random.uniform (-1.0, 1.0)
        yPos = random.uniform (-1.0, 1.0)
        if (math.hypot (xPos, yPos) < 1):
            hits = hits + 1
    return round(4*(hits/numThrows), 6)
  
def main ():
    length = 6
    throws = [100,1000,10000,100000,1000000,10000000]
    print('Computation of PI using Random Numbers\n')
    for index in range(0, length):
        CalculatedPI = computePI(throws[index])
        Difference = round(CalculatedPI - math.pi, 6)
        if (Difference > 0):
            DifferenceStr = str('+' + str(Difference))
        else:
            DifferenceStr = str(Difference)
        print('num =', str(throws[index]).ljust(10),
              'Calculated PI =', str(CalculatedPI).ljust(8, '0'), ' ',
              'Difference =', DifferenceStr)
            
main()
