import numpy as np
"""
Vigenere Cipher
"""
def vigenereCipherToString(text, key):
    #to Uppercase
    key = key.upper()
    #convert key to match length of text
    key = (key * (int(len(text)/len(key)) + 1))[:len(text)]
    #convert to numbers
    text_to_num = [ord(char) - ord('A') if char.isalpha() else char if char.isdigit() else ord(char) for char in text.upper()]
    key_to_num = [ord(char) - ord('A') if char.isalpha() else int(char) if char.isdigit() else ord(char) for char in key]
    encrypted_values = []
    for i in range(len(text_to_num)):
        if isinstance(text_to_num[i], int):
            if text[i].isupper():
                encrypted_values.append(chr((text_to_num[i] + key_to_num[i]) % 26 + ord('A')))
            elif text[i].islower():
                encrypted_values.append(chr((text_to_num[i] + key_to_num[i]) % 26 + ord('a')))
            else:
                encrypted_values.append(chr(text_to_num[i]))
        else:
            encrypted_values.append((int(text_to_num[i]) + key_to_num[i]) % 10)
    return ''.join(str(i) for i in encrypted_values)

def vigenereCipherDecryption(text, key):
    #to Uppercase
    key = key.upper()
    #convert key to match length of text
    key = (key * (int(len(text)/len(key)) + 1))[:len(text)]
    #convert to numbers
    text_to_num = [ord(char) - ord('A') if char.isalpha() else char if char.isdigit() else ord(char) for char in text.upper()]
    key_to_num = [ord(char) - ord('A') if char.isalpha() else int(char) if char.isdigit() else ord(char) for char in key]
    encrypted_values = []
    for i in range(len(text_to_num)):
        if isinstance(text_to_num[i], int):
            if text[i].isupper():
                if (temp_value := (text_to_num[i] - key_to_num[i]) % 26 + ord('A')) < 0:
                    temp_value += 26
                encrypted_values.append(chr(temp_value))
            elif text[i].islower():
                if (temp_value := (text_to_num[i] - key_to_num[i]) % 26 + ord('a')) < 0:
                    temp_value += 26
                encrypted_values.append(chr(temp_value))
            else:
                encrypted_values.append(chr(text_to_num[i]))
        else:
            if (temp_value := (int(text_to_num[i]) - key_to_num[i]) % 10) < 0:
                    temp_value += 10
            encrypted_values.append(temp_value)
    return ''.join(str(i) for i in encrypted_values)

"""
Caesar Cipher 
"""
def caesarCiphertoString(text, key):
    key = int(key)
    text_to_num = [ord(char) - ord('A') if ord(char) - ord('A') >= 0 and ord(char) - ord('A') < 26 else char for char in text.upper()]
    encrypted_values = []
    for i in range(len(text_to_num)):
        if isinstance(text_to_num[i], int):
            if text[i].isupper():
                encrypted_values.append(chr((text_to_num[i] + key) % 26 + ord('A')))
            else:
                encrypted_values.append(chr((text_to_num[i] + key) % 26 + ord('a')))
        else:
            encrypted_values.append(text_to_num[i])
    return ''.join(str(i) for i in encrypted_values)

def caesarCipherDecryption(text, key):
    key = int(key)
    text_to_num = [ord(char) - ord('A') if ord(char) - ord('A') >= 0 and ord(char) - ord('A') < 26 else char for char in text.upper()]
    encrypted_values = []
    for i in range(len(text_to_num)):
        if isinstance(text_to_num[i], int):
            if text[i].isupper():
                if (temp_value := (text_to_num[i] - key) % 26 + ord('A')) < 0:
                    temp_value += 26
                encrypted_values.append(chr(temp_value))
            else:
                if (temp_value := (text_to_num[i] - key) % 26 + ord('a')) < 0:
                    temp_value += 26
                encrypted_values.append(chr(temp_value))
        else:
            encrypted_values.append(text_to_num[i])
    return ''.join(str(i) for i in encrypted_values)
"""
XOR Cipher
"""
def xorCiphertoString(text, key):
    key = (key * (int(len(text)/len(key)) + 1))[:len(text)]
    text_to_num = [ord(char) for char in text]
    key_to_num = [ord(char) for char in key]
    #BIG OOPSIE!!  if ord(char) - ord('A') >= 0 and ord(char) - ord('A') < 26 or ord(char) - ord('a') >= 0 and ord(char) - ord('a') < 26  else char 
    encrypter_values = []
    for i in range(len(text)):
        if isinstance(text_to_num[i], int):
            binary_of_text_letter = str(format(int(text_to_num[i]),'08b'))
            binary_of_key_letter = str(format(int(key_to_num[i]), '08b'))
            new_binary_value = ''
            for j in range(len(binary_of_text_letter)):
                if binary_of_text_letter[j] == binary_of_key_letter[j]:
                    new_binary_value += '0'
                else:
                    new_binary_value += '1'
            encrypter_values.append(chr(int(new_binary_value, 2)))
        else:
            encrypter_values.append(text[i])
    return ''.join(str(i) for i in encrypter_values)

def xorCipherDecryption(text, key):
    key = (key * (int(len(text)/len(key)) + 1))[:len(text)]
    text_to_num = [ord(char) for char in text]
    key_to_num = [ord(char) for char in key]

    encrypter_values = []
    for i in range(len(text)):
        if isinstance(text_to_num[i], int):
            binary_of_text_letter = str(format(int(text_to_num[i]),'08b'))
            binary_of_key_letter = str(format(int(key_to_num[i]), '08b'))
            new_binary_value = ''
            for j in range(len(binary_of_text_letter)):
                if binary_of_text_letter[j] == binary_of_key_letter[j]:
                    new_binary_value += '0'
                else:
                    new_binary_value += '1'
            #print(new_binary_value)
            encrypter_values.append(chr(int(new_binary_value, 2)))
        else:
            encrypter_values.append(text[i])
    return ''.join(str(i) for i in encrypter_values)

if __name__ == "__main__":
    print(xorCipherDecryption(xorCiphertoString('I Hate This Class 123!!', 'HE!P M!3'), 'HE!P M!3'))
    print(caesarCipherDecryption(caesarCiphertoString('I Hate This Class 123!!', '3'), '3'))
    print(vigenereCipherDecryption(vigenereCipherToString('I Hate This Class 123!!', 'HE!P M3'), 'HE!P M3'))
    print(vigenereCipherToString('Math 101', 'is fun'))
    print(vigenereCipherDecryption('Usmm 489', 'is fun'))
    