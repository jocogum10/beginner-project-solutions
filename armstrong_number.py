"""
Armstrong Number
- Learn about armstrong numbers [here](https://en.wikipedia.org/wiki/Narcissistic_number).
- Define a function that allows the user to check whether a given number is armstrong number or not.
- Hint: To do this, first determine the number of digits of the given number. Call that n. Then take every digit in the number and raise it to the nth power. Add them, and if your answer is the original number then it is an Armstrong number.
- Example: Take 1634. Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634. So 1634 is an Armstrong number.
- Tip: All single digit numbers are Armstrong numbers.
"""

def armstrong_number(num):
    n = len(num)
    sum = 0
    for i in range(n):
        sum += int(num[i])**n
    if sum == int(num):
        return True
    else:
        return False

if __name__ == '__main__':
    number = input("Enter a number:")
    print(armstrong_number(number))