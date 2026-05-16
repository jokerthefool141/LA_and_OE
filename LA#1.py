name = input("Enter your name: ").title().strip()
section = input("Enter your section: ").strip()

hobby_list = []

while True:
    
    hobby = input("Enter your hobbies (press 'done' when finished): ").strip()
    
    if hobby.lower() == "done":
        break
   
    if hobby:
        hobby_list.append(hobby)

def display_info(name, section, hobbies):
    
    print("\n===MY INFORMATION===")
    print(f"Name: {name}")
    print(f"Section: {section}")
    print("Hobbies:")
    
    for h in hobbies:
        print(f"- {h.strip().capitalize()}")
    
    print()

display_info(name, section, hobby_list)
display_info(name, section, hobby_list)