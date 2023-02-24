pi = 3.14


def menu():
    print("\nThis program will find the area of a shape for you.")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Square")
    print("4. Circle")
    print("5. Quit")
    choice = int(input("Please enter the number of your selection: "))

    return choice


def rectangle(width, height):
    return width * height


def triangle(base, height):
    return (base * height) / 2


def square(side):
    return side * side


def circle(radius):
    return pi * (radius * radius)


def main():
    while True:
        choice = menu()

        if choice == 1:
            width = int(input("Enter the rectangles width in cm: "))
            height = int(input("Enter the rectangles height in cm: "))
            area = rectangle(width, height)
            print("The area of the rectangle is {:.2f} square cm\n". format(area))

        elif choice == 2:
            base = int(input("Enter the base of the triangle in cm: "))
            height = int(input("Enter the height of the triangle in cm: "))
            area = triangle(base, height)
            print("The area of a triangle is {:.2f} square cm\n". format(area))

        elif choice == 3:
            side = int(input("Enter the length of one side of the square in cm: "))
            area = square(side)
            print("The area of a square is {:.2f} square cm\n". format(area))

        elif choice == 4:
            radius = int(input("Please enter the radius of the circle in cm: "))
            area = circle(radius)
            print("The area of a circle is {:.2f} square cm\n". format(area))

        elif choice == 5:
            print("Goodbye")
            break

        else:
            print("This isn't a valid selection")


main()
