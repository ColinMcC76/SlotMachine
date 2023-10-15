import random

# Constants
MAX_LINES = 9
MAX_BET = 200
MIN_BET = 5

ROWS = 3
COLS = 3

# Define the count and value of symbols
symbol_count = {
    "A": 3, 
    "B": 4,
    "C": 5,  
    "D": 6
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function to check winnings

def check_winnings(board, user_multiplier, bet, symbol_value):
    rows = len(board)
    cols = len(board)
    winnings = 0


    for i in range(rows):
        for j in range(cols):
            current_symbol = board[i][j]

            if current_symbol != ' ':
                # Check right neighbor
                if j + 2 < cols and board[i][j + 1] == current_symbol and board[i][j + 2] == current_symbol:
                    bet_multiplier = symbol_value[current_symbol]  
                    win_amount = bet * bet_multiplier * user_multiplier
                    winnings += win_amount - bet
                    


                # Check bottom neighbor
                if i + 2 < rows and board[i + 1][j] == current_symbol and board[i + 2][j] == current_symbol:
                    bet_multiplier = symbol_value[current_symbol]  
                    win_amount = bet * bet_multiplier *user_multiplier
                    winnings += win_amount - bet



                # Check bottom-right diagonal
                if i + 2 < rows and j + 2 < cols and board[i + 1][j + 1] == current_symbol and board[i + 2][j + 2] == current_symbol:
                    bet_multiplier = symbol_value[current_symbol]  
                    win_amount = bet * bet_multiplier *user_multiplier
                    winnings += win_amount - bet



                # Check bottom-left diagonal
                if i + 2 < rows and j - 2 >= 0 and board[i + 1][j - 1] == current_symbol and board[i + 2][j - 2] == current_symbol:
                    bet_multiplier = symbol_value[current_symbol]  
                    win_amount = bet * bet_multiplier * user_multiplier
                    winnings += win_amount - bet


    return winnings


# # Function to generate a random slot machine spin

# Refactored get_slot_machine_spin function using list comprehension
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [symbol for symbol, symbol_count in symbols.items() for _ in range(symbol_count)]

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

# Function to print the slot machine

def print_slot_machine(columns):
    board = []  # Initialize an empty board

    for row in range(len(columns[0])):
        board_row = []  # Initialize a row in the board
        for i, column in enumerate(columns):
            board_row.append(column[row])  # Append the element to the row
            end_character = " | " if i != len(columns) - 1 else ""
            print(column[row], end=end_character)

        board.append(board_row)  # Append the row to the board
        print()

    return board  # Return the transposed board


# Function to handle deposit
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
            print("Please enter a valid number.")
    
    return amount

# Function to get the number of lines to bet on
def get_num_of_lines():
    while True:
        lines = input(f"Enter the bet multiplier you would like? (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Amount must be between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")
    
    return lines

# Function to get the bet amount
def get_bet():
    while True:
        bet = input(f"How much money would you like to bet? (${MIN_BET}-${MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    
    return bet

# Function to handle a single spin of the slot machine
def spin(balance):
    lines = get_num_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"You do not have enough money deposited to bet this amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")

    return winnings - total_bet

# Main function to run the game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        game = input('Press enter to spin (q to quit): ')
        if game == "q":
            break
        balance += spin(balance)

# Run the game
main()
