"""
99 Bottles
- Create a program that prints out every line to the song "99 bottles of beer on the wall."
- Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
- Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
- Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

sample:
99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall...
"""

for i in range(99,0,-1):
    if i == 1:
        print("{0} bottle of beer on the wall, {0} bottle of beer.\nTake one down, pass it around, {1} bottles of beer on the wall...".format(i, i-1))
    else:
        print("{0} bottles of beer on the wall, {0} bottles of beer.\nTake one down, pass it around, {1} bottles of beer on the wall...".format(i, i-1))