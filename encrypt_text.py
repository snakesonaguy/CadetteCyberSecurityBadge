
import sys

def encrypt(pt, offset):

    ct = ''

    for char in pt:
        
        if ord(char) < 65 or ord(char) > 90:
            ct = ct + char
        else:
            crypto_char = chr(ord(char) + offset)
            ct = ct + crypto_char
    
    return(ct)


def main():

    in_file = sys.argv[1]
    offset = int(sys.argv[2])
    
    f = open(in_file, 'r')

    plain_text = f.read().upper()
    f.close()

    crypto_text = encrypt(plain_text, offset=offset)

    o = open('cryptotext.txt', 'w')
    o.write(crypto_text)
    o.close()



if __name__ == '__main__':
    main()