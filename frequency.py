import sys
import pprint
import os

freq = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
    'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
    'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}

def analyze_ct(ct):

    for char in ct:
        if ord(char) < 65 or ord(char) > 90:
            continue
        else:
            freq[char] = freq[char] + 1

def display_analysis():
    os.system('clear')
    pprint.pprint(freq)
    print('')
    input('Press the return key to continue...')


def make_guess():
    os.system('clear')
    
    target_char = input('Enter the Character you wish to replace : ').upper()
    guess_char = input('Enter the Character you want replace the {} with: '.format(target_char)).lower()
    
    if type(freq[target_char]) == int:
        print("Replacing '{}, with '{}".format(target_char, guess_char))
        freq[target_char] = guess_char
    else:
        print('You already made a guess for {}.'.format(target_char))

    input('Press the return key to continue...')


def print_decrypt(ct):

    decrypt = ''

    for char in ct:
        if ord(char) < 65 or ord(char) > 90:
            decrypt = decrypt + char
        elif type(freq[char]) == int:
            decrypt = decrypt + char
        else:
            decrypt = decrypt + freq[char]

    print(decrypt)
    input('Press the return key to continue...')


def reset_all():
    return

def main():
    
    in_file = sys.argv[1]

    i = open(in_file, 'r')

    ct = i.read()

    analyze_ct(ct)

    choice = 0

    while choice != 5:
        os.system('clear')
        print('-----------------------------------------------------------')
        print('Welcome to the Frequency Attack Program!')
        print('-----------------------------------------------------------')
        print('Please make a selection: ')
        print('')
        print('1 to display analysis.')
        print('2 to make a guess')
        print('3 print current decrypt text')
        print('4 to reset the analysis')
        print('5 to exit the program')
        print('')
        
        choice = int(input('Selection: '))

        if choice == 1:
            display_analysis()
        elif choice == 2:
            make_guess()
        elif choice == 3:
            print_decrypt(ct)
        elif choice == 4:
            reset_all()
        elif choice == 5:
            os.system('clear')
            continue


if __name__ == '__main__':
    main()