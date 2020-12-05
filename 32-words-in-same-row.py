# check if all the letters in a word are present on the same row of the keyboard
# example tree - all the four letters are present in the same row in keyboard

def checkWord(word):
	count1, count2 ,count3 = 0, 0, 0
	length = len(word)
	for char in word.lower() :
		if char in 'qwertyuiop':
			count1 += 1
		elif char in 'asdfghkl':
			count2 += 1
		elif char in 'zxcvbnm':
			count3 += 1

	if any([length == count1,length == count2,length == count3]) :
		return True
	return False


print(checkWord('tree'))
