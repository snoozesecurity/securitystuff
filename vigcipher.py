# See blog post at https://snoozesecurity.blogspot.com/2020/12/ill-take-some-vigenere-with-my-caesar.html

from itertools import cycle
import string
alpha = string.ascii_lowercase

plainText = input("Enter your plaintext to be encrypted: ")
userKey = input("Enter your alphabetical key; exits on invalid character: ").lower()
cipherText = ''
cycKey = cycle(userKey)

# Caesar/ROT Function

def rotateChar(s: str, rotate: int):
	out = ''
	boolUpper = s.isupper()
	s = s.lower()
	if s not in alpha:
		out = s
	elif s in alpha and alpha.index(s) + rotate > 25:
		if boolUpper:
			out = alpha[((alpha.index(s) + rotate) - 25) - 1].upper()
		else:
			out = alpha[((alpha.index(s) + rotate) - 25) - 1]
	else:
		if boolUpper:
			out = alpha[alpha.index(s) + rotate].upper()
		else:
			out = alpha[alpha.index(s) + rotate]
	return out

# Check validity of key; for demonstration purposes I only accept alphabet characters

for char in userKey:
	if char.lower() not in alpha:
		print("Invalid key; quitting.")
		quit()

# Create nested list(s) with the proper ROT number for each string in the plaintext

refList = []

for char, rot in zip([char for char in plainText if char.lower() in alpha], cycKey):
	if char.lower() in alpha:
		refList.append([char, alpha.index(rot)])

# Iterate through original plaintext and rotate when a legal character is at index 0 of refList then pop index 0.

for char in plainText:
	if refList and char == refList[0][0]:
		cipherText += rotateChar(char, refList[0][1])
		refList.pop(0)
	else:
		cipherText += char

print("Ciphertext:", cipherText)
