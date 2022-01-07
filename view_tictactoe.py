# Qizhou Fang
# qsfang
# 77491862
# it is responsible for the window and buttons and labels in it to
# interact with users
import tkinter as tk
import controller_tictactoe

window = tk.Tk(className="Tic Tac Toe")
# create 3 labels as headers
lbl_1 = tk.Label(master=window, text="Number of games played: 0")
lbl_2 = tk.Label(master=window, text="Number of wins for Player X: 0")
lbl_3 = tk.Label(master=window, text="Number of wins for Player O: 0")
lbl_1.grid(row=0, column=0, columnspan=3)
lbl_2.grid(row=1, column=0, columnspan=3)
lbl_3.grid(row=2, column=0, columnspan=3)
# make sure the board shift size as window size change
window.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=50)
window.columnconfigure([0, 1, 2], weight=1, minsize=50)
# create 9 buttons representing 9 squares on the board
# when clicked, call the move method in controller
btn_1 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(1, btn_1, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_1.position = 1
btn_1.grid(row=3, column=0, sticky="nsew")
btn_2 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(2, btn_2, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_2.position = 2
btn_2.grid(row=3, column=1, sticky="nsew")
btn_3 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(3, btn_3, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_3.position = 3
btn_3.grid(row=3, column=2, sticky="nsew")
btn_4 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(4, btn_4, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_4.position = 4
btn_4.grid(row=4, column=0, sticky="nsew")
btn_5 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(5, btn_5, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_5.position = 5
btn_5.grid(row=4, column=1, sticky="nsew")
btn_6 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(6, btn_6, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_6.position = 6
btn_6.grid(row=4, column=2, sticky="nsew")
btn_7 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(7, btn_7, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_7.position = 7
btn_7.grid(row=5, column=0, sticky="nsew")
btn_8 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(8, btn_8, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_8.position = 8
btn_8.grid(row=5, column=1, sticky="nsew")
btn_9 = tk.Button(master=window, width=10, height=5,
                  command=lambda: controller_tictactoe.move(9, btn_9, lbl_1, lbl_2, lbl_3,
                                                            btn_list), text="-", fg="blue")
btn_9.position = 9
btn_9.grid(row=5, column=2, sticky="nsew")
btn_list = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]
# create new game button and bind it to new_game method in controller
btn_new = tk.Button(master=window, command=lambda: controller_tictactoe.new_game(btn_list), text="New Game")
btn_new.grid(row=6, column=0, columnspan=3)
# listen for events
window.mainloop()
