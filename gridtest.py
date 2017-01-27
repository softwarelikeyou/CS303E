#function that finds product
def max_prod (a):
  max_p = a[0] * a[1]
  for i in range (1, len(a) - 1):
    prod = a[i] * a[i + 1]
    if (prod > max_p):
      max_p = prod
  return max_p

def main():
    #open file for reading
    file = 'testcase1.txt'
    ##file = 'grid.txt'
    file = 'testcase2.txt'
    file = 'testcase3.txt'
    in_file = open(file, "r")
    #read the dimension of the grid
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)
    #create an empty grid and populate it
    grid = []
    for i in range (dim):
        row = in_file.readline()
        row = row.strip()
        row = row.split()
        for j in range (dim):
            row[j] = int(row[j])
        grid.append(row)
    in_file.close()

    maximum = 0;
    
    # find horizontal max
    for row in grid:
      for i in range (0, len(row) - 3):
        product = 1
        for j in range (i, i+ 4):
          product *= int(row[j])
          if product > maximum:
            maximum = product

    # find vertical max, but first rotate grid 90 degrees to the left
    rotated = []
    for j in range(dim):
      row = []
      for i in range(dim):
        row.append(int(grid[i][j]))
      rotated.append(row)
    for row in rotated:
      for i in range (0, len(row) - 3):
        product = 1
        for j in range (i, i+ 4):
          product *= int(row[j])
          if product > maximum:
            maximum = product

    # find diagonal max left to right
    i = 0
    while i < dim - 3:
      for k in range(dim-3 - i):
        product = 1
        for j in range(k, k+4):
          product *= grid[j+i][j]
          if product > maximum:
            maximum = product
      i += 1
    i = 0
    while i < dim - 3:
      for k in range(dim-3 - i):
        product = 1
        for j in range(k, k+4):
          product *= grid[j][j+i]
          if product > maximum:
            maximum = product
      i += 1

    # find diagonal max right to left
    i = 0
    while i < dim - 3:
      for k in range(dim-3 - i):
        product = 1
        for j in range(k, k+4):
          product *= grid[j+i][dim-1-j]
          if product > maximum:
            maximum = product
      i += 1
    i = 0
    while i < dim - 3:
      for k in range(dim-3-i):
        product = 1
        for j in range(k, k+4):
          product *= grid[j][dim-1-j-i]
          if product > maximum:
            maximum = product
      i += 1

    print('The greatest product is', maximum, end='.')
  
main()
                
        
