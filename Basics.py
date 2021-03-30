import random

#Revision of basics, only forgetable stuff mentioned here
#Strings, usefull functions to remember
print("STRINGS\n")

name = "paul pelar"
print(name.title())     #change first letter of each word to capital
print(name.upper())     #all capitals
print(name.lower())     #all lower
print(f"Hi, {name.title()}!")

word = " python "
print(word)
print(word.rstrip())        #delete whitespaces right
print(word.lstrip())        #left
print(word.strip())         #both sides

#Numbers
print("\nNUMBERS\n")

billions = 1_000_000_000      #use _ for clarity
print(billions+1)

#List
print("\nLISTS\n")
alphabet = ["a",'b','c','e']
alphabet.insert(3,"d")      #index where to instert, what to insert
print(alphabet)

del alphabet[-1]        #can be used to delete indexed element, cant use it later(the elem)
print(alphabet)

last_letter = alphabet.pop()        #same as del but can keep popped item into variable
print(last_letter)
print(alphabet)
any_index = alphabet.pop(0)         #can pop any index
print(any_index)
print(alphabet)

alphabet.append("b")
alphabet.remove("b")        #used to remove specific value, BUT only first occurance
print(alphabet)

cars = ["VW",'BMW','Audi','Mercedes']
cars.sort()
print(cars)
cars.sort(reverse=True)     #permamently sorted
print(cars)

print(sorted(cars))         #temporarily, can add arg revesrse as well
cars.reverse() #can reverse order (any order)
print(cars)
print(len(cars))

for car in cars:
    print(car)

for i in range(1,10,2):      #start,stop,step
    print(i)

odd_numbers = list(range(1,31,2))
print(odd_numbers)
print(min(odd_numbers))
print(max(odd_numbers))
print(sum(odd_numbers))

#better way to arrange lists

squares = []
for i in range(1,11):
    square = i**2
    squares.append(square)
print(squares)

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

milion = [value for value in range(1,1000001)]
print(sum(milion))

szescian = [value**3 for value in range(1,11)]
print(szescian)

#slicing
playerrs = ['paul','mike','jaga','jaco','mati']

for elem in playerrs[-2:]:          #can use slicing in for loops
    print(elem.title())

#copying lists
foods = ['pizza','pasta','lody']
foods_2 = foods
foods.append("apple")
print(foods,foods_2)    #same list two different names

foods = ['pizza','pasta','lody']
foods_2 = foods[:]      #here is the copy
foods.append("apple")
print(foods,foods_2)    #now it works

dimensions = (100,200,300,400)
dimensions2 = dimensions[-2:]
print(dimensions2)
try:
    dimensions[1] = 0
except:
    print("tuples are immutable")

#dictionaries
print("\nDICTIONARIES\n")

alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

del alien_0['points']
print(alien_0)

#good way to create long dictionaries
fav_languge = {
    'janek':'python',
    'paweł':'python',
    'jose':'c',
}

language = fav_languge['paweł'].title()
print(f'My fav language is {language}')

print(alien_0)
try:
    print(alien_0['points'])
except KeyError as k:
    print(f'{k} is not in dictionary')

#get function (1 arg what to take, 2 arg what to gigve if arg not in dictionary)
alien_0 = {
    'color':'blue',
    'speed':'fast',
    'race':'marsylian',
    'sex':'female',
}

sex = alien_0.get('sex','Sex not specified!')
print(sex)
age = alien_0.get('age','Age not specified!') #if second arg not given - None is default
print(age)

#iteration through dictionary
for key,value in alien_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

print('\n')
for k in alien_0.keys():
    print(k)
print('\n')
for v in alien_0.values():
    print(v)
print('\n')
for elem in alien_0:  #default key
    print(elem)

print(sorted(alien_0))
print(sorted(alien_0.values()))

dic_language = {
    '1': 'python',
    '2': 'c',
    '3': 'ruby',
    '4': 'python',
}

for lang in sorted(set(dic_language.values())):   #set to eliminate duplicates
    print(lang)

#nesting
print('\nNESTING\n')

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print(f'Total number of aliens {len(aliens)}')

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'moderate'

for alien in aliens[:5]:
    print(alien)

print('\nInput\n')

prompt = 'Personalized message!'
prompt += '\nWhat is your name? '

#name = input(prompt)   #to not stop the program
name = 'Paul'
print(f'Witaj, {name.title()}!')

print('\nWHILE LOOP\n')

prompt = 'Here is your blog, type anything you have on your mind:'
prompt += '\nType \'koniec\' if you want to end the blog. '
message = 'koniec'  #change to empty string if you want to test
while message != 'koniec':
    message = input(prompt)
    print(message)

#flag
prompt = 'Guess the number: '

active = True
while active:
    #message = int(input(prompt))
    message = 1     #delete this line if u want to test, and uncomment previous
    if message == 1:
        print('Yes!')
        active = False
    else:
        print('Wrong!')

#break
prompt = 'Guess the number: '

while True:
    #message = int(input(prompt))
    message = 1 #delete this line if you want to test, uncomment previous
    if message == 1:
        print('Yes!')
        break
    else:
        print('Wrong!')

#continue
#print only odd numbers

current_number = 0
while current_number<=10:
    current_number+=1
    if current_number%2 == 0:
        continue

    print(current_number)

random_numbers = [random.randint(1,5) for _ in range(20)]
print(random_numbers)

while 2 in random_numbers:
    random_numbers.remove(2)

print(random_numbers)
