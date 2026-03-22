import random
import time

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """Checks if the given player has won the game"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Checks if the game is a draw (no empty spaces left)"""
    return ' ' not in board

def user_move(board):
    """Handles the user's turn"""
    while True:
        try:
            move = input("Enter your move (1-9): ")
            move = int(move) - 1 # Convert 1-9 to 0-8 index
            
            if 0 <= move <= 8:
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("⚠️ That space is already taken! Try another one.")
            else:
                print("⚠️ Please enter a number between 1 and 9.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

def computer_move(board):
    """Handles the computer's turn using the random library"""
    print("Computer is thinking...")
    time.sleep(1) # Add a small delay to make it feel like it's "thinking"
    
    # Find all empty spots
    empty_spots = [i for i in range(9) if board[i] == ' ']
    
    # Choose a random empty spot
    if empty_spots:
        move = random.choice(empty_spots)
        board[move] = 'O'
        print(f"Computer placed an 'O' in position {move + 1}.")

def main():
    print("=" * 45)
    print("         TIC-TAC-TOE: YOU vs COMPUTER")
    print("=" * 45)
    print("The board positions are numbered 1-9 as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("You are 'X' and the Computer is 'O'.\n")
    
    board = [' ' for _ in range(9)]
    
    while True:
        # User Turn
        print_board(board)
        user_move(board)
        
        if check_win(board, 'X'):
            print_board(board)
            print("🎉 Congratulations! You win! 🎉")
            break
            
        if check_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break
            
        # Computer Turn
        computer_move(board)
        
        if check_win(board, 'O'):
            print_board(board)
            print("💻 Computer wins! Better luck next time!")
            break
            
        if check_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    main()
