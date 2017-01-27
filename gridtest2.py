def get_rmax(grid):
	
	# initialize placeholder for maximum product
	rmax = 0
	# get max product of horizontal (row) directions 
	for i in range(len(grid)):
		for j in range(len(grid[i]) - 3):
			# get block of 4 adjacent numbers
			block = grid[i][j:j+4]
			# get product
			prod = block[0] * block[1] * block[2] * block[3]
			# check if product is greater than max product
			if prod > rmax:
				rmax = prod
	return rmax

def main():
	
	# open file for reading
	in_file = open('grid.txt', 'r')
	
	# get dimension
	dim = int(in_file.readline().strip())
	
	# intialize grid
	grid = []
	
	# get each row
	for row in in_file:
		row = row.strip().split()
		# convert each row to int
		for i in range(len(row)):
			row[i] = int(row[i])
		# append each row now of ints to grid
		grid.append(row)
	
	
	rmax = get_rmax(grid)
	print(rmax)		
			
main()
