# ROT Encoder/Decoder with absolutely zero exception handling
# Code written by SnoozeSecurity (youtube.com/SnoozeSecurity)

import sys

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 
	"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
			
encOrDec = int(raw_input("Enter 1 to ENCODE, 2 to DECODE: "))
rotNum = int(raw_input("Enter numbers to ROTate, 1-25: "))
userStr = raw_input("Enter your string: ")

if encOrDec == 1:
	for i in range(len(userStr)):
		if userStr[i] == " ":
			sys.stdout.write(" ")
		else:
			for j in range(len(alphabet)):
				if userStr[i] == alphabet[j]:
					if j + rotNum > 25:
						diff = (j + rotNum) - 25
						sys.stdout.write(alphabet[diff - 1])
					else:
						sys.stdout.write(alphabet[j + rotNum])
						
elif encOrDec == 2:
	for i in range(len(userStr)):
		if userStr[i] == " ":
			sys.stdout.write(" ")
		else:
			for j in range(len(alphabet)):
				if userStr[i] == alphabet[j]:
					if j - rotNum < 0:
						diff = (j - rotNum) + 25
						sys.stdout.write(alphabet[diff + 1])
					else:
						sys.stdout.write(alphabet[j - rotNum])
						
print ""