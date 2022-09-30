import getpass
import os

def get_offset():

    valid = False

    offset = 0

    while not valid:
        candidate = input('Please input an offset (key) between 1 and 9: ')

        if candidate.isnumeric() and int(candidate) < 10:
            offset = candidate
            valid = True
    
    return int(offset)


def get_cipher_text():

    os.system('clear')

    offset = get_offset()
    print('')
    plain_text = getpass.getpass('Please enter your plain text: ').upper()
    print('')
    cipher_text = ''

    for char in plain_text:
        cipher_char = ord(char) + offset
        cipher_text = cipher_text + chr(cipher_char)

    print('Your Cipher Text is: ' + cipher_text)
    print('')
    input('Press the return key to continue.')
    

def get_plain_text():
    os.system('clear')

    offset = get_offset()
    print('')
    cipher_text = input('Please enter your cipher text: ')
    print('')

    plain_text = ''

    for char in cipher_text:
        plain_char = ord(char) - offset
        plain_text = plain_text + chr(plain_char)

    print('Your Plain Text is: ' + plain_text)
    print('')
    input('Press the return key to continue.')

def main():

    choice = 0

    while choice != 3:
        os.system('clear')
        print('-----------------------------------------------------------')
        print('Welcome to the Caeser Cipher Encryption/Decryption Program!')
        print('-----------------------------------------------------------')
        print('Please make a selection: ')
        print('')
        print('1 to Encrypt a message.')
        print('2 to Decrypt a message')
        print('3 to Exit the program')
        print('')

        choice = int(input('Selection: '))

        if choice == 1:
            get_cipher_text()
        elif choice == 2:
            get_plain_text() 
        elif choice == 3:
            os.system('clear')
            continue

if __name__ == '__main__':
    main()