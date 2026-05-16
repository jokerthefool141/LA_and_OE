stars = int(input("Enter number of stars: "))

def print_spaces(spaces):
    if spaces <= 0:
        return
    print(" ", end="")
    print_spaces(spaces - 1)

def print_stars(star):
    if star <= 0:
        return
    print("* ", end="")
    print_stars(star - 1)

def create_pyramid(rows, current_row=1):
    if current_row > rows:
        return

    print_spaces(rows - current_row)
    print_stars(current_row)
    print()
    create_pyramid(rows, current_row + 1)

create_pyramid(stars)
print(f"Done pyramid with {stars} * base!")