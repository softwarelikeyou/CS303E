
#  File: DNA.py

#  Description: This program finds and print outs common DNA sequences. 

#  Student Name: Courtney Thomas

#  Student UT EID: cct685

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 25 March 2016

#  Date Last Modified: 26 March 2016
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
    file = open('DNA.txt', 'r')
    line = [line.strip() for line in file]
    file.close()
    print("Longest Common Sequences", end= "\n\n")
    num_pairs = int(line.pop(0))
    for i in range (0, num_pairs):
        seq_1 = line.pop(0).upper()
        seq_2 = line.pop(0).upper()
        if len(seq_1) > 80 or len(seq_2) > 80:
            print("Sequence cannot be longer than 80")
            break
        piece_1 = substr(seq_1)
        piece_2 = substr(seq_2)
    #find matches
        matches = []
        match_len = 0
        num_matches = 1
        for piece1 in piece_1:
            for piece2 in piece_2:
                if (piece1 == piece2):
                    if (len(piece1) >= match_len):
                        matches.append(piece1)
                        match_len = len(piece1)
        output = 'Pair ' + str(i + 1) + ':'                   
        if len(matches) == 0:
            print(output, "No Common Sequence Found")
        for pair in matches: 
            if (num_matches == 1):
                num_matches += 1
                print(output, pair)
            else:
                print(pair.rjust(12, " "))
        print(" ", end="\n")
main()
