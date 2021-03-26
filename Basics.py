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
print("\nNumbers\n")

billions = 1_000_000_000      #use _ for clarity
print(billions+1)

#List
print("\nLists\n")
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



