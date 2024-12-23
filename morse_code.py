#import lib
import time

morse_code_dict ={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'}

def translate_to_morse(text):
    morse_code=''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()]+' '
        else:
            morse_code+=char+' '
    return morse_code

#main
while True:
    print(''' Select an option from below:
          1.Translate English Text to morse code.
          2.Exit!!''')
        
    inp=int(input())

    if inp==1:
        english_text= input("Enter English Text: ")
        morse_code_text=translate_to_morse(english_text)
        print(morse_code_text)
        print("")
    
    elif inp==2:
        print("Exiting....")
        time.sleep(4)   #will wait for 4 sec to exit
        break


    
