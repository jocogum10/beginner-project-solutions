"""
### Coin Estimator By Weight
When some people receive change after shopping, they put it into a container and let it add up over time. 
Once they fill up the container, they'll roll them up in [coin wrappers](https://en.wikipedia.org/wiki/Coin_wrapper) 
which can then be traded in at a bank for what they are worth. While most banks will give away coin wrappers for free, 
it's convenient to have an idea of how many you will need. Instead of counting how many coins you have, it's easier to 
separate all of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you'll need.
For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have 
about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

Here is the [weight of each coin](https://en.wikipedia.org/wiki/Coins_of_the_United_States_dollar#Coins_in_circulation) 
and [how many fit inside each type of wrapper](https://en.wikipedia.org/wiki/Coin_wrapper#Amount_in_a_roll_in_the_United_States).
- Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
- Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their money.
- Subgoals:
  - Round all numbers printed out to the nearest whole number.
  - Allow the user to select whether they want to submit the weight in either grams or pounds.
"""
import math

type = ['pennies', 'nickels', 'dimes', 'quarters']
mass_grams = {'pennies': 2.50, 'nickels': 5.0, 'dimes': 2.268, 'quarters': 5.67}
coin_wrap_count = {'pennies': 50, 'nickels': 40, 'dimes': 50, 'quarters': 40}
my_coin_weight = dict()


def estimate_coin(my_coin_dict):
    num_of_coins = {'pennies': round((float(my_coin_dict['pennies'])/mass_grams['pennies'])), 'nickels': round((float(my_coin_dict['nickels'])/mass_grams['nickels'])), 'dimes': round((float(my_coin_dict['dimes'])/mass_grams['dimes'])), 'quarters': round((float(my_coin_dict['quarters'])/mass_grams['quarters']))}
    coin_wrap = {'pennies': math.floor((float(num_of_coins['pennies'])/coin_wrap_count['pennies'])), 'nickels': math.floor((float(num_of_coins['nickels'])/coin_wrap_count['nickels'])), 'dimes': math.floor((float(num_of_coins['dimes'])/coin_wrap_count['dimes'])), 'quarters': math.floor((float(num_of_coins['quarters'])/coin_wrap_count['quarters']))}
    
    for coin, number in num_of_coins.items():
        print("You have {0} {1} and would fill {2} wrappers.".format(number, coin, coin_wrap[coin]))


if __name__ == '__main__':
    for i in type:
        my_coin_weight[i] = input("input weight of {0}: ".format(i))
        
    estimate_coin(my_coin_weight)