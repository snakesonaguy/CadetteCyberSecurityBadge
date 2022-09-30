import hashlib
import os
import getpass
from pprint import pprint



PASSWORDS = []

PASS_HASH = {}



os.system('clear')

def print_hashes():

    os.system('clear')

    for k, v in PASS_HASH.items():
        print('-----------------------------------------------')
        print('Password: {}'.format(k))
        print('Hash: {}'.format(v))
        
    print('')
    input('Press the return key to continue.')

def test_password():
    
    os.system('clear')

    password = getpass.getpass('Enter a Password: ')
    m = hashlib.sha1()
    m.update(password.encode('utf-8'))
    print('')
    print("Your password's hash is: ")
    print(m.hexdigest())
    print('')
    print("Let's check if your password is in the hash table!")
    input('Press the return key to continue.')

    os.system('clear')

    in_table = False
    cracked = ''

    for k, v in PASS_HASH.items():
        if v == m.hexdigest():
            in_table = True
            cracked = k
            break
    
    if in_table == True:
        print('Your password is in my hash table. Your password is: ')
        print(cracked)
    else:
        print('Your password was not in my hash table.')

    input('Press the return key to continue.')

    

def main():

    with open('password_file.txt', 'r') as in_file:
        for line in in_file:
            PASSWORDS.extend(line.split())        

    for password in PASSWORDS:
        m = hashlib.sha1()
        m.update(password.encode('utf-8'))

        PASS_HASH[password] = m.hexdigest()

    choice = 0

    while choice != 3:
        os.system('clear')
        print('-----------------------------------------------------------')
        print('Welcome to the Password Cracker Program!')
        print('-----------------------------------------------------------')
        print('Please make a selection: ')
        print('')
        print('1 to print the Passwords and Hashes.')
        print('2 to test a Password against the Hashes')
        print('3 to Exit the program')
        print('')
        
        choice = int(input('Selection: '))

        if choice == 1:
            print_hashes()
        elif choice == 2:
            test_password()
        elif choice == 3:
            os.system('clear')
            continue

if __name__ == '__main__':
    main()




