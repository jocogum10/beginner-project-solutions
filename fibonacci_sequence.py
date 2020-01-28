"""
### Fibonacci Sequence
If you do not know about the Fibonacci Sequence, read about it [here]
(https://en.wikipedia.org/wiki/Fibonacci_number).
- Define a function that allows the user to find the value of the nth term in 
the sequence.
- To make sure you've written your function correctly, test the first 10 numbers 
of the sequence.
- You can assume either that the first two terms are 0 and 1 or that they are 
both 1.
- There are two methods you can employ to solve the problem. One way is to solve 
it using a loop and the other way is to use recursion.
- Try implementing a solution using both methods.

In mathematics, the Fibonacci numbers, commonly denoted Fn form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the two 
preceding ones, starting from 0 and 1
F0 = 0, F1 = 1
Fn = Fn-1 + Fn-2
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765

"""

def fibonacci_sequence_sequence(n_term):
    if n_term == 0:     # base case F0
        return 0
    elif n_term == 1:   # base case F1
        return 1
    else:
        n_term = fibonacci_sequence_sequence(n_term-1) + fibonacci_sequence_sequence(n_term-2)
        return n_term


def fibonacci_sequence_loop(n_term):
    if n_term == 0:
        return 0
    elif n_term == 1:
        return 1
    else:
        F0 = 0
        F1 = 1
        i = 1
        while(i != n_term):
            Fn = F1 + F0                # Fn = Fn-1 + Fn-2
            F0 = F1                     # change Fn-2 to Fn-1 for the next iteration
            F1 = Fn                     # change Fn-1 to Fn for the next iteration
            i += 1
        return Fn


if __name__ == '__main__':
    for i in range(15):
        a = fibonacci_sequence_sequence(i)
        b = fibonacci_sequence_loop(i)
        print(a,b)