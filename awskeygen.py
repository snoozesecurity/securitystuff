import random

chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","/","/"]
numIn = ''

# Function to print a 20 character string with all uppercase letters and no slashes as per the chars list above

def aws_id(x):
  for i in range(x):
    output = ''
    for i in range(20):
      choice = random.choice(chars[0:35])
      if choice.isdigit() == True:
        output += choice
      else:
        output += choice.upper()
  return output

# Function to print a 40 character string with random uppercase letters and occasional slashes	

def aws_key(y):
  for i in range(y):
    output = ''
    for j in range(40):
      ranUpper = random.choice(chars[0:25]).upper()
      output += random.choice([ranUpper, random.choice(chars)])
  return output
  
# Gets numeric input from user and wrapped in a while loop for lazy input validation

while numIn.isdigit() == False:
  numIn = raw_input("How many ID/Keys would you like to generate? ")

numIn = int(numIn)

# Generates ID/Key pair(s)

for i in range(numIn):
  print 'aws_access_key_id =', aws_id(numIn)
  print 'aws_secret_access_key =', aws_key(numIn)
