from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")

playerA = StringVar()
playerB = StringVar()
playerC = StringVar()
playerD = StringVar()

player1_name = Entry(tk, textvariable=playerC, bd=5)
player1_name.grid(row=1, column=1)
player2_name = Entry(tk, textvariable=playerD, bd=5)
player2_name.grid(row=2, column=1)

bclick = True
flag = 0

def disableButton():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)

def btnClick(buttons):
    global bclick, flag
    if buttons["text"] == " " and bclick:
        buttons["text"] = "X"
        bclick = False
        checkforwin()
        flag += 1
    elif buttons["text"] == " " and not bclick:
        buttons["text"] = "O"
        bclick = True
        checkforwin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("TicTacToe", "Button already clicked")

def checkforwin():
    win_conditions = [
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button5, button9),
        (button3, button5, button7),
        (button1, button2, button3),
        (button2, button5, button8),
        (button7, button6, button9)
    ]

    for a, b, c in win_conditions:
        if a["text"] == b["text"] == c["text"] and a["text"] != " ":
            if a["text"] == "X":
                tkinter.messagebox.showinfo("Tic Tac Toe", playerC.get() + " Wins!")
            else:
                tkinter.messagebox.showinfo("Tic Tac Toe", playerD.get() + " Wins!")
            disableButton()
            return

    if flag == 8:
        tkinter.messagebox.showinfo("Tic Tac Toe", "It is a Tie")
        disableButton()

buttons = StringVar()
Label(tk, text="Player1: ", font="Times 20 bold", bg="white", fg="purple", height=1, width=8).grid(row=1, column=0)
Label(tk, text="Player2: ", font="Times 20 bold", bg="white", fg="purple", height=1, width=8).grid(row=2, column=0)

button1 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=" ", font="Times 20 bold", bg="purple", fg="white", height=1, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
