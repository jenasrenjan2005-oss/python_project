# Tic-Tac-Toe Game

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [" "] * 9
        self.player1 = player1
        self.player2 = player2
        self.current_mark = "X"

    def print_position_guide(self):
        print("Position guide (use these numbers to play):")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")
        print()

    def print_board(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()

    def check_winner(self, mark):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],   
            [0, 4, 8], [2, 4, 6]               
        ]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == mark:
                return True
        return False

    def is_board_full(self):
        for cell in self.board:
            if cell == " ":
                return False
        return True

    def current_player_name(self):
        return self.player1 if self.current_mark == "X" else self.player2

    def get_valid_move(self):
        while True:
            move = input(f"{self.current_player_name()} ({self.current_mark}), enter a cell number (1-9): ")

            try:
                move = int(move)
            except ValueError:
                print("That's not a valid number. Please try again.")
                continue

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if self.board[move - 1] != " ":
                print("That cell is already taken. Choose another one.")
                continue

            return move - 1  

    def switch_turn(self):
        self.current_mark = "O" if self.current_mark == "X" else "X"

    def reset_board(self):
        self.board = [" "] * 9
        self.current_mark = "X"

    def play_round(self):
        self.reset_board()
        self.print_board()

        while True:
            move = self.get_valid_move()
            self.board[move] = self.current_mark
            self.print_board()

            if self.check_winner(self.current_mark):
                print(f"Congratulations {self.current_player_name()}! You won the game!")
                break

            if self.is_board_full():
                print("The game is a draw!")
                break

            self.switch_turn()


def main():
    print("Welcome to Tic-Tac-Toe!")

    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")

    game = TicTacToe(player1, player2)
    game.print_position_guide()

    while True:
        game.play_round()

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
