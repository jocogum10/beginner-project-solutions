"""
### Change Calculator
- Imagine that your friend is a cashier, but has a hard time counting back 
change to customers.
- Create a program that allows him to input a certain amount of change, and then
 print how how many quarters, dimes, nickels, and pennies are needed to make up 
 the amount needed.
Example: if he inputs 1.47, the program will say that he needs 5 quarters, 2 
dimes, 0 nickels, and 2 pennies.
- Subgoals:
  - So your friend doesn't have to calculate how much change is needed, allow 
  him to type in the amount of money given to him and the price of the item. 
  The program should then tell him the amount of each coin he needs like usual.
  - To make the program even easier to use, loop the program back to the top so 
  your friend can continue to use the program without having to close and open 
  it every time he needs to count change.
"""
def change_calculator(am):
    quarter_am = am//coins['quarter']
    am = am - (quarter_am*coins['quarter'])
    dime_am = am//coins['dime']
    am = am - (dime_am*coins['dime'])
    nickel_am = am//coins['nickel']
    am = am - (nickel_am*coins['nickel'])
    penny_am = round(am/coins['penny'])
    
    change_am['quarter'] = quarter_am
    change_am['dime'] = dime_am
    change_am['nickel'] = nickel_am
    change_am['penny'] = penny_am
    
    
if __name__ == '__main__':
    coins = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25}
    change_am = dict()
    while True:
        price = input('\nEnter price of item: ')
        amount = input('Enter amount given: ')
    
        price = float(price)
        amount = float(amount)
        val = amount - price
        if val > 0:
            change_calculator(val)
    
            print("Change:")
            for coin,val in change_am.items():
                print("\t{0} - {1}".format(coin, int(val)))
        else:
            print("Money given is not enough.\n")