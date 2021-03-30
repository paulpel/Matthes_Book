import random
print('Functions\n')

#3 ways to pass arguments
#1
def describe_person(name,age):
    print(f'{name} is {age} years old.')

describe_person('Paul',23)
describe_person(21,'Paul') #order is important

#2
describe_person(age=30,name='Criss') #can change order

#3 setting deffault value
def describe_person(age,name='Stranger'):  #defaul argument after non-default, cant be the oposite
    print(f'{name} is {age} years old.')

describe_person(age=23)

#optional arguments
def get_formated_name(first_name,last_name,middle_name=''):
    '''Returns formated name and last name'''
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = get_formated_name('jimmy','hendrix')
print('\n'+musician)
musician = get_formated_name('john','hooker','lee')
print(musician)


#changing elems in function is perma
print('\n')
def transfer(untransfered,completed):
    while untransfered:
        current = untransfered.pop()
        print(f'Transfering: {current}')
        completed.append(current)

def show_completed(completed):
    print('\nFollowing transfers have been completed: ')
    for transfer in completed:
        print(transfer)

untransfered = [1,22,232,12,56,12]
completed_transfers = []

transfer(untransfered,completed_transfers)
show_completed(completed_transfers)

#how to forbid function to make changes, pass copy, but it uses more memory etc
print('\n')
list_of_numbers = [random.randint(1,2) for i in range(15)]

def remove_val_from_lsit(val,lis):
    while val in lis:
        lis.remove(val)
    return lis

new_list = remove_val_from_lsit(2,list_of_numbers[:])
print(list_of_numbers,new_list)

#any number of arguments, but this param needs to be at the end
def make_pizza(*topings):
    print('\nMaking pizza with following ingriedients')
    for toping in topings:
        print(f'- {toping}')

make_pizza('cheese')
make_pizza('cheese','ham','mushrooms')

def make_pizza(size,*topings):
    print(f'\nMaking {size} inch pizza with following ingriedients')
    for toping in topings:
        print(f'- {toping}')

make_pizza(30,'cheese')
make_pizza(40,'cheese','ham','mushrooms')

#passing key-value arguments - ** double stars (kwargs)
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('paul','pelar',location='cieszyn',age='22')
print(user_profile)

#empty
def build_profile(**user_info):
    return user_info

user_profile = build_profile(location='cieszyn',age='22',first_name='paul')
print(user_profile)

#modules
from random import randint as random_integer #can change names of functions

print(random_integer(69,70))
