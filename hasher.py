# Write a function called hashMe that takes a password string input and assigns it a hash value.
# Write a function called saltMe that adds a random element to the input.
# Demonstrate that two of the same input result in a different final hash.
# More info at https://snoozesecurity.blogspot.com/

import hashlib
import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 
  "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def hashMe(str):
  return hashlib.md5((raw_input("Enter a password, get a hash: ")) + str).hexdigest()
  
def saltMe(saltSize):
  saltStr = ''
  for i in range(saltSize):
    saltStr += random.choice(alphabet)
  print "Salting with", saltStr
  return saltStr

try:
  userSaltSize = int(raw_input("Enter desired salt size ranging from 1-999: "))
  if not (1 <= userSaltSize <= 999):
    raise ValueError()
except ValueError:
  print "Invalid salt size, retry ranging from 1-999."
else:
  print hashMe(saltMe(userSaltSize))