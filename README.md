# ChangeMaker Program

**Author:** Zach Khan  
**Date:** February 24, 2023  

This program calculates the change due after a purchase and breaks it down into different denominations. It takes the item price and cash tendered as inputs, then outputs the required change in twenties, tens, fives, ones, quarters, dimes, nickels, and pennies.

## Program Overview

The ChangeMaker program performs the following tasks:
- Prompts the user to enter the item price and the amount of cash provided.
- Calculates the change due in dollars.
- Breaks down the change into various denominations to provide the minimum number of bills and coins.

## Features

- **Flexible Change Calculation**: Allows users to enter any price and cash amount.
- **Detailed Breakdown**: Outputs the exact quantity of each bill and coin needed for the change.

## How It Works

The program takes user inputs for price and cash tendered, then:
1. Converts both values to cents for more accurate arithmetic with integers.
2. Calculates the total change due.
3. Divides the change by each denomination in descending order, outputting the count for each.

### Denominations Covered

- Bills: Twenties, Tens, Fives, Ones
- Coins: Quarters, Dimes, Nickels, Pennies

## Usage

To run the program, execute the following command:

```bash
python ChangeMaker.py
```

The program will prompt for:

Price of the item (e.g., $15.37) 
Cash tendered (e.g., $20.00) 

## Example Input
```bash
Price of the item: 
15.37
Cash tendered: 
20.00 
```

## Example Output
```bash
Change: 4.63
Change Left: 463
twenties: 0
tens: 0
fives: 0
ones: 4
quarters: 2
dimes: 1
nickles: 0
pennies: 3
```

This output shows the change amount and the quantity of each bill and coin needed.

## Future Improvements
- Add error handling for invalid inputs (e.g., if cash tendered is less than the price).
- Improve formatting of the output for better readability.
- Add support for different currencies or custom denominations.
