import random

class SudokuSolver:
    def __init__(self, board=None):
        self.board = board if board else [[0] * 9 for _ in range(9)]
    
    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.board[i][j] == num:
                    return False
        
        return True
    
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True
    
    def generate(self, difficulty=40):
        for box in range(0, 9, 3):
            nums = list(range(1, 10))
            random.shuffle(nums)
            idx = 0
            for i in range(box, box + 3):
                for j in range(box, box + 3):
                    self.board[i][j] = nums[idx]
                    idx += 1
        
        self.solve()
        
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        for i, j in cells[:difficulty]:
            self.board[i][j] = 0
    
    def display(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j] if self.board[i][j] != 0 else ".", end=" ")
            print()

if __name__ == "__main__":
    print("\n=== SUDOKU SOLVER & GENERATOR ===")
    
    while True:
        print("\n" + "="*40)
        print("1. Generate New Sudoku")
        print("2. Solve Sudoku")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            difficulty = int(input("Enter difficulty (20-50, higher=harder): "))
            sudoku = SudokuSolver()
            print("\nGenerating puzzle...")
            sudoku.generate(difficulty)
            print("\nGenerated Sudoku:")
            sudoku.display()
        elif choice == '2':
            print("\nEnter your Sudoku puzzle (use 0 for empty cells)")
            board = []
            for i in range(9):
                while True:
                    row = input(f"Row {i+1} (9 digits, e.g., 530070000): ")
                    if len(row) == 9 and row.isdigit():
                        board.append([int(x) for x in row])
                        break
                    print("Invalid input! Enter 9 digits.")
            
            sudoku = SudokuSolver(board)
            print("\nOriginal Sudoku:")
            sudoku.display()
            
            print("\nSolving...")
            if sudoku.solve():
                print("\nSolved Sudoku:")
                sudoku.display()
            else:
                print("No solution exists!")
        elif choice == '3':
            break