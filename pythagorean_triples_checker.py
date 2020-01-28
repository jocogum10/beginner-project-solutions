"""
### Pythagorean Triples Checker
- If you do not know how basic right triangles work, or what a Pythagorean Triple is read these articles on Wikipedia[¹](https://en.wikipedia.org/wiki/Right_triangle) [²](https://en.wikipedia.org/wiki/Pythagorean_triple).
- Allows the user to input the sides of any triangle in any order.
- Return whether the triangle is a Pythagorean Triple or not.
- Loop the program so the user can use it more than once without having to restart the program.
"""


def pythagorean_triples_check(v1, v2, v3):
    angles.append(int(v1))
    angles.append(int(v2))
    angles.append(int(v3))
    if int(angles[0])**2 == int(angles[1])**2 + int(angles[2])**2:
        print("a pythagorean triple: {0}, {1}, {2}".format(int(angles[0])**2, int(angles[1])**2, int(angles[2])**2))
    elif int(angles[1])**2 == int(angles[0])**2 + int(angles[2])**2:
        print("a pythagorean triple: {0}, {1}, {2}".format(int(angles[0])**2, int(angles[1])**2, int(angles[2])**2))
    elif int(angles[2])**2 == int(angles[1])**2 + int(angles[0])**2:
        print("a pythagorean triple: {0}, {1}, {2}".format(int(angles[0])**2, int(angles[1])**2, int(angles[2])**2))
    else:
        print("not a pythagorean triple: {0}, {1}, {2}".format(int(angles[0])**2, int(angles[1])**2, int(angles[2])**2))


if __name__ == '__main__':
    while(True):
        angles = []
        v1 = input("Enter the 1st value:")
        v2 = input("Enter the 2nd value:")
        v3 = input("Enter the 3rd value:")
        pythagorean_triples_check(v1, v2, v3) 
