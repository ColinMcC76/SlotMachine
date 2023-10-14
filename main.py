import random

MAX_LINES= 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    

def deposit(): 
    while True:
        amount = input("How much money would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")
    
    return amount

def get_num_of_lines():
    while True:
        lines = input("enter the number of lines you would like to bet on. (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Amount must be bewteen 1 and " + str(MAX_LINES) + ". ")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        bet = input("How much money would you like to bet?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet


def main():
    balance = deposit()
    lines = get_num_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(
                f"You do not have enough to money deposited to bet this amount, your current balane is ${balance}.")7
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet} ")
    

main()