import random

def generate_password(length, upper, lower, numbers, symbols):
    
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    number_characters = "0123456789"
    symbol_characters = "'!@#$%^&*:;,.<>?~][}{_+-="
    
    all_characters = ""
    
    if upper == "yes":
        all_characters += uppercase_letters
    
    if lower == "yes":
        all_characters += lowercase_letters
    
    if numbers == "yes":
        all_characters += number_characters
        
    if symbols == "yes":
        all_characters += symbol_characters
        
    if all_characters == "":
        return None
        
    password = "".join(random.choices(all_characters, k=length))
    
    return password
    
    
            
    