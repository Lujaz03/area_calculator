

def start():
    welcome_messages = print('''
    ==================
    Area Calculator 📐
    ==================
    ''')

    print(welcome_messages)

    shape = int(input('1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n\nSelect Shape: '))

    while True:
        if shape == 1:
            base=float(input('Base: '))
            height=float(input('Height: '))
            triangle_formula = int(base*height/2)
            print(f'The area is : {triangle_formula}')
            break
        elif shape == 2:
            length=float(input('Length: '))
            width=float(input('Width: '))
            rectangle_formula = length*width
            print(f'The area is: {rectangle_formula}')
            break
        elif shape == 3:
            length=float(input('Length: '))
            square_formula=length*2
            print(f'The area is: {square_formula}')
            break
        elif shape == 4:
            radius=float(input('Radius: '))
            circle_formula = 3.14*(radius**2) # phi = 3.14
            print(f'The area is: {circle_formula}')
            break
        elif shape == 5:
            print('Thank You For Using Our Program\n')
            break
        else:
            print('Your choice is Invalid!\n')
            break

if __name__ == "__main__":
    start()