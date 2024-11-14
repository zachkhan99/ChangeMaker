""" ChangeMaker.py Program
    Zach Khan
    February 24, 2023
    Utlilizes user inputs of money
    and conversions to output necessary
    change into different quantities"""


price = (input("Price of the item: \n"))
price = float(price)
price = price * 100
price = int(price)

paid = input("Cash tendered: \n")
paid = float(paid)
paid = paid * 100
paid = int(paid)

""" the number the user inputs get converted to
    a floating point number for arithmetic
    and then as an integer"""

dollars = paid - price
dollars = dollars/100

change = paid - price


print("Change:",dollars)
print("Change Left:",change)

""" the change in pennies as an integer
    needs to be divided with no remainder
    to display the number of bills or
    coins for the correct change"""

twenties = change // int(2000)
print("twenties:",twenties)
twenties = change % int(2000)

tens = twenties // int(1000)
print("tens:",tens)
tens = twenties % int(1000)

fives = tens // int(500)
print("fives:",fives)
fives = tens % int(500)

ones = fives // int(100)
print("ones:",ones)
ones = fives % int(100)

quarters = ones // int(25)
print("quarters:", quarters)
quarters = ones % int(25)

dimes = quarters // int(10)
print("dimes:",dimes)
dimes = quarters % int(10)

nickles = dimes // int(5)
print("nickles:",nickles)
nickles = dimes % int(5)

""" the remainder from each caluculation
    is needed to do the calulations for
    the next bill or coin"""

pennies = nickles // int(1)
print("pennies:", pennies)