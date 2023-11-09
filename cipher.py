def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char
        
        encrypted_text += encrypted_char
    
    return encrypted_text

phrase = input("Enter phrase: ")
shift = 5
encrypted_phrase = caesar_cipher(phrase, shift)

print(f"Encrypted phrase: {encrypted_phrase}")
