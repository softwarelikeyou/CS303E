#  File: DNA.py

#  Description: Print the longest sequence of nucleotides for given the DNA sequence pairs

#  Student Name: Courntey C. Thomas

#  Student UT EID: cct685

#  Course Name: CS 303E

#  Unique Number: 1

#  Date Created: 3/25/2016

#  Date Last Modified: 3/26/2016

import os.path
import sys

def substr (st):
  pieces = []
  wnd = len (st)
  while (wnd > 0):
    start_idx = 0
    while ((start_idx + wnd) <= len(st)):
      piece = st[start_idx : start_idx + wnd]
      pieces.append(piece)
      start_idx += 1
    wnd = wnd - 1
  return pieces

def main():
   if os.path.exists('DNA.txt') == False:
     print('Please ensure DNA.txt is located in the same directory as this program')
     sys.exit()
   file = open('DNA.txt', 'r')
   lines = [line.strip() for line in file]
   file.close()
   numberOfPairs = int(lines.pop(0))
   print('Longest Common Sequences', end='\n\n')
   for index in range(0,numberOfPairs):
        sequence1 = lines.pop(0).upper()
        sequence2 = lines.pop(0).upper()
        if len(sequence1) > 80 or len(sequence2) > 80:
            print('Sequence nucleotide count cannot be greater than 80')
        pieces1 = substr(sequence1)
        pieces2 = substr(sequence2)
        
        matches = []
        matchesLength = 0
        matchesCount = 1
        for piece1 in pieces1:
            for piece2 in pieces2:
                if piece1 == piece2:
                    if len(piece1) >= matchesLength:
                        matches.append(piece1)
                        matchesLength = len(piece1)
                        
        description = 'Pair ' + str(index+1) + ':'
        if len(matches) == 0:
            print(description, 'No Common Sequence Found')
            
        for match in matches:
            if matchesCount == 1:
                matchesCount += 1
                print(description, match)
            else:
                print(match.rjust(12, ' '))
        print(' ', end='\n')
main()

##Longest Common Sequences
##
##Pair 1: TCG
##
##Pair 2: TGAT
##        GGAC
##
##Pair 3: No Common Sequence Found

##3
##GAAGGTCGAA
##CCTCGGGA
##ATGATGGAC
##GTGATAAGGACCC
##AAATTT
##GGGCCC
