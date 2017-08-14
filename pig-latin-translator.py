#/opt/bin/python
print "Welcome to the Pig Latin translator!"

pyg = 'ay'
#Starting code from here
original = raw_input("Enter a word: ")
if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word + first + pyg
	new_word = new_word[1:len(new_word)]
	print new_word
else:
	print "empty"
