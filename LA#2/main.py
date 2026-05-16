import input_validation as validate
import generate_password as generate

# def main():
    
#     length = validate.input_validation()
    
#     upper = validate.yes_no_validation("\nInclude uppercase letters? (yes/no): ")
#     lower = validate.yes_no_validation("\nInclude lowercase letters? (yes/no): ")
#     numbers = validate.yes_no_validation("\nInclude numbers? (yes/no): ")
#     symbols = validate.yes_no_validation("\nInclude symbols? (yes/no): ")
    
#     password = generate.generate_password(length, upper, lower, numbers, symbols)
    
#     if password == None:
#         print("\nNo character types selected. Please select at least one character type.")
        
#     else:
#         print("\nGenerated password:", password)
#         print(f"\nPassword generated with {length} length\n")
        
# if __name__ == "__main__":
#     main()

def main():
    
    while True:
        length = validate.input_validation()
    
        upper = validate.yes_no_validation("\nInclude uppercase letters? (yes/no): ")
        lower = validate.yes_no_validation("\nInclude lowercase letters? (yes/no): ")
        numbers = validate.yes_no_validation("\nInclude numbers? (yes/no): ")
        symbols = validate.yes_no_validation("\nInclude symbols? (yes/no): ")
    
        password = generate.generate_password(length, upper, lower, numbers, symbols)
    
        if password == None:
            print("\nNo character types selected. Please select at least one character type.")
        
        else:
            print("\nGenerated password:", password)
            print(f"\nPassword generated with {length} length\n")
    
        again = validate.yes_no_validation("\nGenerate another password? (yes/no): ")
        if again == "no":
            print("\nThank you for using the password generator. Goodbye!\n")
            break
        else:
            continue
    
        
if __name__ == "__main__":
    main()