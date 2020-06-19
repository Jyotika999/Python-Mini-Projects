# this contains the code for readable password generator
# by reading the characters from a file 
#most importantly getting a big list of words from which you can select a particular word and then continue by creating a paragraph which contains a list of words which will be stored in a file
import random

wordslist = []

special_char = ['@','#','$','*','&']

with open("wiki.text.txt", "r") as file:
	data = file.readlines()

	for line in data:
		words = line.split()



		for item in words:
			if len(item)>5:
				wordslist.append(item.capitalize())  # for all the words present in the list having length greater than 5 will be appended in the wordslist 

# this way you are able to generate readable word 

word = random.choice(wordslist)
schar = random.choice(special_char)
num = str(random.randint(0,10000))

passw = word+schar+num
print(passw)



					#print(words)

	#data =file.readLines()

	#print(data)
#print("done")