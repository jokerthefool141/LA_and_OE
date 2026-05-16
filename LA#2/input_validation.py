def isdigit(string):
    if not string:
        return False
    
    digits = "0123456789"
    for characters in string:
        if characters not in digits:
            return False
    return True

def input_validation():
    
    while True:
        
        print()
        length = input("Enter the desired password length (8-128): ")
        
        if isdigit(length):
            
            length = int(length)
            
            if 8 <= length <= 128:
                return length
            else:
                print("\nInvalid input. Please enter a number between 8 and 128. ")
                
        else:
            print("\nInvalid input. Please enter a valid number. ")
            
        
def yes_no_validation(message):
    
    while True:
        
        answer = input(message).lower()
        
        if answer == "yes" or answer == "no":
            return answer
        
        else:
            print("\nInvalid input. Please enter (yes/no).")
            
        