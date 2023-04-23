l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 
	
	##OUTPUT######
#	Input a letter of the alphabet: S
#    S is a consonant.
#  Input a letter of the alphabet:a
#  a is a vowel