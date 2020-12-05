""" Print pascals Triangle
		 1
	   1   1
	  1  2  1
	1  3   3  1
"""
def printPascalsTriangle(triangle,rows):
	for row in triangle:
		row = list(map(str,row))			# converting into a list of numbers as a list of string
		temp = ' '.join(row)				# concatinating all numbers with a seperation of whitespace in btn
		print(temp.center(rows*2))

def createPascalsTriangle(rows):
	if rows <=0:
		return []
	triangle = [[1]]					# adding the first 1 manually
	for i in range(1,rows):				# iterating from 1 to rows  
		previous_row = triangle[i-1]	# getting the previous row
		current_row = [1]				# all the row starts with 1

		# to calculate the in between elements
		for j in range(1,i):			
			current_row.append(previous_row[j-1] + previous_row[j])
		
		current_row.append(1)			# all the row ends with 1
		triangle.append(current_row)
	return triangle


rows = 5
triangle = createPascalsTriangle(rows)
printPascalsTriangle(triangle,rows)
