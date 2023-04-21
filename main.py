from tkinter import *


window = Tk()
window.title("TIC-TAC-TOE")

#create the
board = Frame(window)
board.pack()

player = "X"
cells = []
for i in range(3):
    row = []
    for j in range(3):
        cell = Button(board, text="", font=("Arial", 40),
                      width=3, height=1, command=lambda row=i,
                      col=j: cell_click(row, col))
        cell.grid(row=i, column=j)
        row.append(cell)

    cells.append(row)


# Create a label to display whose turn it is
turn_label = Label(window, text="Player " + player + "'s turn")
turn_label.pack()

winner_label = Label(window, text="")
winner_label.pack()
def check_win():
    global winner, winner_label
    #check rows
    for i in range(3):
        if cells[i][0]["text"] == cells[i][1]["text"] == cells[i][2]["text"] != "":
            winner = cells[i][0]["text"]
            winner_label.config(text="Player " + winner + " wins")
            winner_label.update()
            print(winner)
            return
        if cells[0][i]["text"] == cells[1][i]["text"] == cells[2][i]["text"] != "":
            winner = cells[0][i]["text"]
            winner_label.config(text="Player " + winner + " wins")
            winner_label.update()
            print(winner)
            return

    if cells[0][0]["text"] == cells[1][1]["text"] == cells[2][2]["text"] != "":
        winner = cells[0][0]["text"]
        winner_label.config(text="Player " + winner + " wins")
        winner_label.update()
        print(winner)
        return
    if cells[0][2]["text"] == cells[1][1]["text"] == cells[2][0]["text"] != "":
        winner = cells[0][2]["text"]
        winner_label.config(text="Player " + winner + " wins")
        winner_label.update()
        print(winner)
        return
    if all(cells[i][j]["text"] != "" for i in range(3) for j in range(3)):
        winner = "Tie"
        winner_label.config(text="Tie game!")
        winner_label.update()
        print(winner)
        return

winner = None



# Define a function to handle player clicks
def cell_click(row, col):
    global player, winner

    #Ignore clicks on non-empty cells
    if cells[row][col]["text"] == "" and not winner:
        cells[row][col]["text"] = player
        if player == "X":
            player = "0"
        else:
            player = "X"
        turn_label.config(text="Player " + player + "'s turns")
        check_win()
        if winner:
            winner_label.config(text="Player " + winner + " wins")
            # Use the destroy method to remove the winner label and start a new game
            winner_label.update()

            reset_button = Button(window, text="New game", command=reset_game)
            reset_button.pack()
        elif all(cells[i][j]["text"] != "" for i in range(3) for j in range(3)):
            winner = "Tie"
            winner_label.config(text="Tie game!")
            # Use the destroy method to remove the winner label and start a new game
            winner_label.update()

            reset_button = Button(window, text="New game", command=reset_game)
            reset_button.pack()

def reset_game():
    global player, winner, winner_label
    player = "X"
    winner = None
    for row in range(3):
        for col in range(3):
            cells[row][col]["text"] = ""
    turn_label.config(text="Player " + player + " 's turn")
    if winner_label:
        winner_label.destroy()


window.mainloop()