import random
chars = ['!','£','"','$','%','^','&','*','(',')','-','_','@','~','#',"'",'<','>',',','.','?','/','|','¬','+','=',' ']
letts = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(letts)
random.shuffle(chars)
incCaps = False
incNums = False
incChar = False

i = 0

noChars = int(input('How many characters do you want in your password? (minimum 4)'))
caps = input('Do you want to include capital letters? (y/n)')
if caps == 'y':
    incCaps = True
nums = input('Do you want to include numbers? (y/n)')
if nums == 'y':
    incNums = True
char = input('Do you want to include special characters (y/n)')
if char == 'y':
    incChar = True

pwd = ''

while i < noChars:
    pwd += random.choice(letts)
    i += 1
    if incCaps and i < noChars:
        pwd += random.choice(letts).upper()
        i += 1
    if incNums and i < noChars:
        pwd += str(random.randint(0,10))
        i += 1
    if incChar and i < noChars:
        pwd += random.choice(chars)
        i += 1

random.shuffle(list(pwd))
pwd.join('')
print(pwd)