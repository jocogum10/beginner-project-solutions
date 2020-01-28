"""
### Mean, Median, and Mode
In a set of numbers, the mean is the average, the mode is the number that occurs
 the most, and if you rearrange all the numbers numerically, the median is the 
 number in the middle.
- Create three functions that allow the user to find the mean, median, and mode 
of a list of numbers. If you have access or know of functions that already 
complete these tasks, do not use them.
- Subgoals
  - In the mean function, give the user a way to select how many decimal places 
  they want the answer to be rounded to.
  - If there is an even number of numbers in the list, return both numbers that 
  could be considered the median.
  - If there are multiple modes, return all of them.
"""
import math

def mean(numbers):
    sum_of_num = 0
    len_of_list = len(numbers)
    for number in numbers:
        sum_of_num += number
    return(sum_of_num/len_of_list)
    
def mode(numbers):
    # count the number of occurence and store it in a dictionary
    count_dict = dict()
    prev_num = 0
    numbers = sorted(numbers)
    for number in numbers:
        if number != prev_num:
            count_dict[number] = 1
        elif number == prev_num:
            count_dict[number] += 1
        prev_num = number
    
    # determine the highest value of the dictionary
    values = count_dict.values()
    highest = max(values)
    mode = list()
    # check in the dictionary for values equal to the highest count, store the key(or number)
    for k,v in count_dict.items():
        if highest == v:
            mode.append(k)
    return(mode)
    
def median(numbers):
    numbers = sorted(numbers)
    count = len(numbers)/2
    if count%2 == 0:
        return (numbers[math.floor(count)-1],numbers[math.ceil(count)])
    else:
        return mylist[int(count)]
    
    
if __name__ == '__main__':
    list_of_numbers = list()
    # change to for loop
    number = input("Input the number and then enter: ")
    number += ' '           # add space at the end of string
    a = ''
    for i in number:
        if i == ' ':        # to satisfy this condition and last number will be stored
            list_of_numbers.append(float(a))
            a = ''
        else:
            a += i

    mean_of_num = mean(list_of_numbers)
    mode_of_num = mode(list_of_numbers)
    median_of_num = median(list_of_numbers)
    print(sorted(list_of_numbers))
    
    dec_places = input("How many decimal places for the mean value? ")
    dec_places = int(dec_places)
    print("mean: {0}, mode: {1}, median: {2} ".format(round(mean_of_num, dec_places), mode_of_num, median_of_num))
    