def kind (a,b,c):
    # Uses the 3 inputs and formulas to return a number that will determine the triangle type
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 1
        elif a == b or b == c or a == c:
            return 2
        elif a**2 + b**2 == c**2:
            return 3
        elif a**2 + b**2 > c**2:
            return 4
        elif a**2 + b**2 < c**2:
            return 5
    return 0

def name(k):
    # Prints back the type of triangle depending on what was returned from the kind function
    if k == 0:
        print("    0  no triangle")
    if k == 1:
        print("    1  equilateral")
    if k == 2:
        print("    2  isosceles")
    if k == 3:
        print("    3  right")
    if k == 4:
        print("    4  acute")
    if k == 5:
        print("    5  obtuse")
        
# Main function where the program starts
def main():
    print("Categorize Triangles")
    print()
    # Defined variables for the sides of the triangles
    a = 100
    b = 100
    c = 100
    # While loop that asks for inputs and stops if any of the sides are equal to 0
    while a >= 1 and b >= 1 and c >= 1:
        a = int(input("First side: "))
        if a == 0:
            return print("Done!")
        b = int(input("Second side: "))
        if b == 0:
            return print("Done!")
        c = int(input("Third side: "))
        if c == 0:
            return print("Done!")
        # Sorts the sides with a being the smallest and c being the largest
        sides = [a,b,c]
        for x in range(3):
            for y in range(3):
                if sides[x] < sides[y]:
                    temp = sides[x] 
                    sides[x] = sides[y] 
                    sides[y] = temp
        # Sets a variable equal to the output of the kind function and sends it to the name function
        triangle = kind(sides[0], sides[1], sides[2])
        print(str(a) + "," + str(b) + "," + str(c) , end=" ")
        name(triangle)
        print()
        
                
# Calls the main function    
main()