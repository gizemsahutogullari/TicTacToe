import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text='', font=('normal', 20), width=6, height=3,
                                command=lambda i=i, j=j: self.on_click(i, j), bg='#3498db', fg='#ecf0f1')
                btn.grid(row=i, column=j)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_button(row, col)
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player} kazandı!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "Berabere!")
                self.reset_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state='disabled')

    def check_winner(self, row, col):
        # Dikey kontrol
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        # Yatay kontrol
        if all(self.board[row][j] == self.current_player for j in range(3)):
            return True
        # Çapraz kontrol
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                button = self.window.grid_slaves(row=i, column=j)[0]
                button.config(text='', state='normal')
                self.board[i][j] = ' '
        self.current_player = 'X'

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()




