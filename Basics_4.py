with open('Files/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('Files/pi_digits.txt') as file_object:
    lines = file_object.readlines() #create list

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

with open('Files/pi_million_digits.txt') as file_object:
    lines = file_object.readlines() #create list

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(len(pi_string))

my_birthday = '15101998'
if my_birthday in pi_string:
    print('Yes!')
else:
    print('No')

print('\nEXCEPTIONS:\n')

print('Input two numbers to be divided.')
print('Input "q" to stop the programm.')
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break
    try:
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        print('Cant divide by zero!')
    except ValueError:
        print('Value error! Input only numbers!')
    else:
        print(answer)