''' A python program that implements Caesar Cipher Technique- Cryptography'''

def encryption(string,key): #function definition
    ''' Function that encrypts the given string using caesar cipher technique
        Params: string, key
        Returns: encrypted_text
    '''
    encrypted_text=''
    for char in string:
        if char=='': 
            encrypted_text+=char
            #Encrypts Empty character

        elif char.isupper(): 
            encrypted_text= encrypted_text+ chr((ord(char) + key-65) % 26 + 65) 
            #Encrypts Upper case character
         
        else:
            encrypted_text=encrypted_text+ chr((ord(char) + key-97) % 26 + 97)
            #Encrypts lower case character
    
    return encrypted_text

if __name__== "__main__":
    string=input('Enter the text to be encrypted:')
    key=int(input('Enter the shift key:'))
    print('Text before Encryption:',string)
    print('Shift Key:',key)
    print('Encrypted text:',encryption(string,key)) #function calling

'''
Sample Output:
Enter the text to be encrypted:Alphabets ABCD
Enter the shift key:4
Text before Encryption: Alphabets ABCD
Shift Key: 4
Encrypted text: EptlefixwrEFGH

'''

