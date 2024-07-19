import os
import platform
import termcolor
import argparse

bannertext = """

 ▄████▄   ██▓ ██▓███   ██░ ██ ▓█████  ██▀███    ██████ ▓█████  ▄████▄  
▒██▀ ▀█  ▓██▒▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
▒▓█    ▄ ▒██▒▓██░ ██▓▒▒██▀▀██░▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒███   ▒▓█    ▄ 
▒▓▓▄ ▄██▒░██░▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
▒ ▓███▀ ░░██░▒██▒ ░  ░░▓█▒░██▓░▒████▒░██▓ ▒██▒▒██████▒▒░▒████▒▒ ▓███▀ ░
░ ░▒ ▒  ░░▓  ▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
  ░  ▒    ▒ ░░▒ ░      ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
░         ▒ ░░░        ░  ░░ ░   ░     ░░   ░ ░  ░  ░     ░   ░        
░ ░       ░            ░  ░  ░   ░  ░   ░           ░     ░  ░░ ░      
░                                                             ░    

"""

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt text using various ciphers.', epilog='''Example - python3 %(prog)s decrypt caesar "Kvu'a mvynla av mvssvd Fhzo0e01 vu NpaObi!" -s 7''')
    
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode: encrypt or decrypt')
    parser.add_argument('cipher', choices=['caesar', 'atbash', 'vigenere'], help='Cipher: caesar, atbash, or vigenere')
    parser.add_argument('text', help='Text to be processed')
    parser.add_argument('-s', '--shift', type=int, help='Shift Key for Caesar cipher')
    parser.add_argument('-k', '--key', help='key for Vigenere cipher')

    args = parser.parse_args()

    if args.cipher == 'caesar':
        if args.shift is None:
            parser.error('Caesar cipher requires --shift argument')
        result = caesar_cipher(args.text, args.shift, encrypt=args.mode == 'encrypt')
    elif args.cipher == 'atbash':
        result = atbash_cipher(args.text)
    elif args.cipher == 'vigenere':
        if args.key is None:
            parser.error('Vigenère cipher requires --key argument')
        result = vigenere_cipher(args.text, args.key, encrypt=args.mode == 'encrypt')

    print(result)

def caesar_cipher(plain_text, shift_key, encrypt=True):
    print(f'Text: {plain_text}')
    print('Cipher: Caesar Cipher')
    print(f'Shift Key: {shift_key}')
    result = ''
    if not encrypt:
        shift_key = -shift_key
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            index_num = (alphabets.index(char.lower()) + shift_key) % 26
            new_char = alphabets[index_num]
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    if not encrypt:
        print('Mode: Decrypt')
        return f'\nDecrypted Text: {result}'
    else:
        print('Mode: Encrypt')
        return f'\nEncrypted Text: {result}'
    

def atbash_cipher(plain_text):
    print(f'Text: {plain_text}')
    print('Cipher: Atbash Cipher')
    reversed_alphabets = alphabets[::-1]
    result = ''
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            index_num = alphabets.index(char.lower())
            new_char = reversed_alphabets[index_num]
            if is_upper:
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return f'\nEncrypted/Decrypted: {result}'

def vigenere_cipher(plain_text, key, encrypt=True):
    print(f'Text: {plain_text}')
    print('Cipher: Vigenere Cipher')
    print(f'Shift Key: {key}')
    if len(key) > len(plain_text):
        print("The key's length should be less than or equal to the length of the plaintext.")
    elif len(key) < len(plain_text):
        key = (key * len(plain_text))[:len(plain_text)]
    result = ''
    num = 0
    for char in plain_text:
        if char.isalpha():
            key_char = key[num]
            is_upper = char.isupper()
            key_index = alphabets.index(key_char.lower())
            if not encrypt:
                key_index = -alphabets.index(key_char.lower())
            index_num = (alphabets.index(char.lower()) + key_index) % 26
            new_char = alphabets[index_num]
            if is_upper:
                new_char = new_char.upper()
            result += new_char
            num += 1
        else:
            result += char
    if not encrypt:
        print('Mode: Decrypt')
        return f'\nDecrypted Text: {result}'
    else:
        print('Mode: Encrypt')
        return f'\nEncrypted Text: {result}'

alphabets = 'abcdefghijklmnopqrstuvwxyz'

description = "Encrypt/Decrypt text using various ciphers.\n"
dev_info = """
+------------------------------------------------------------+
|    v1.0                                                    |
|    Developed by: Yaswanth Kumar Koppanathi                 |
+------------------------------------------------------------+
"""

if platform.system() == 'Linux':
    os.system('clear')
elif platform.system() == 'Windows':
    os.system('cls')

colored_banner = termcolor.colored(bannertext, color='red')
print(colored_banner, end="")
print(termcolor.colored(description, 'white', attrs=['bold']), end="")
print(termcolor.colored(dev_info, 'green'))

if __name__ == '__main__':
    main()