"""
### Multiplication Table
- Create a program that prints out a multiplication table for the numbers 1 
through 9.
- It should include the numbers 1 through 9 on the top and left axises, and it 
should be relatively easy to find the product of two numbers. Do not simply 
write out every line manually (ie print('7 14 21 28 35 49 56 63') ).
- Subgoals:
  - As your products get larger, your columns will start to get crooked from the
  number of characters on each line. Clean up your table by evenly spacing 
  columns so it is very easy to find the product of two numbers.
  - Allow the user to choose a number to change the size of the table (so if 
  they type in 12, the table printed out should be a 12x12 multiplication table).
"""
def multiplication_table(r):
    row = [i for i in range(1,(r+1))]
    column = [i for i in range(1,(r+1))]
    for r in range(len(row)):
        for c in range(len(column)):
            print("{0:<3}".format(column[c]*row[r]), end=' ')
        print()


if __name__ == '__main__':
    my_range = input("Enter the size of the table: ")
    my_range = int(my_range)
    multiplication_table(my_range)