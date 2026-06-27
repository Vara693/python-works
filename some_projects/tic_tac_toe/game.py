import numpy as np

class game():
    def __init__(self):
        self.board = np.zeros((3,3), dtype=int)

    def add_ele(self, row, col, ele):
        if(self.board[row][col] == 0):
            self.board[row][col] = ele
            return 1
        else:
            return 0

    def print_board(self):
        flat = {0 : '   ', 1 : ' X ', 2:' O '}
        for row in self.board:
            print('|'.join(flat[val] for val in row))
            print('-'*11)

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if np.all(self.board[i,:] == 1) or np.all(self.board[:,i] == 1):
                return "X wins!"
            if np.all(self.board[i,:] == 2) or np.all(self.board[:,i] == 2):
                return "O wins!"
        
        # Check diagonals
        if np.all(np.diag(self.board) == 1) or np.all(np.diag(np.fliplr(self.board)) == 1):
            return "X wins!"
        if np.all(np.diag(self.board) == 2) or np.all(np.diag(np.fliplr(self.board)) == 2):
            return "O wins!"
        
        # No winner yet
        return "No winner"
    

board = game()
while(board.check_winner() == "No winner"):
    print("Player X:")
    row = int(input(("Enter row to add element: ")))
    col = int(input(("Enter col to add element: ")))
    while (row > 2 or col > 2 or board.add_ele(row, col, 1) != 1):
        print("Enter valid credentials to input an element!!")
        print("Player X:")
        row = int(input(("Enter row to add element: ")))
        col = int(input(("Enter col to add element: ")))
    board.print_board()

    if(board.check_winner() != "No winner"):
        print(board.check_winner())
        break

    print("Player O:")
    row = int(input(("Enter row to add element: ")))
    col = int(input(("Enter col to add element: ")))
    while (row > 2 or col > 2 or board.add_ele(row, col, 2) != 1):
        print("Enter valid credentials to input an element!!")
        print("Player O:")
        row = int(input(("Enter row to add element: ")))
        col = int(input(("Enter col to add element: ")))
    board.print_board()

    if(board.check_winner() != "No winner"):
        print(board.check_winner())
        break
