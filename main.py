import tkinter as tk
import random as rn
import pygame
from tkinter import messagebox


def close():
    window.destroy()


def key_generate():
    code = arg_input.get()
    if len(code) != 5:
        tk.messagebox.showwarning('Error', 'Incorrect Code')
    else:
        try:
            code = int(code, 16)
            key = ['', '', '']

            symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for num in range(12):
                index = rn.randint(0, 35)
                key[num//4] += str(symbols[index])

            for block in range(3):
                pos = rn.randint(0, 3)
                key[block] = (key[block][:pos]
                              +str(code)[block]
                              +key[block][pos:])

            key = (key[0] + '-'
                   +key[1] + '-'
                   +key[2] + ' '
                   +str(code)[-2]
                   +str(code)[-1])
            lbl_result.configure(text=key)
        except:
            tk.messagebox.showwarning('Error', 'Incorrect Code')


window = tk.Tk()
window.title('GTA SA Key Generator')
icon = tk.PhotoImage(file = "icon.png")
window.iconphoto(True, icon)
window.geometry('650x490')
window.resizable(False, False)

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

bg_img = tk.PhotoImage(file='background.png')
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.26, rely=0.5, anchor='center')

lbl_input = tk.Label(frame,
                     text='Введите 5-значное HEX-число',
                     font=('Arial', 10),
                     anchor='center')
lbl_input.grid(column=0, row=0, padx=10, pady=15)
arg_input = tk.Entry(frame, width=10)
arg_input.grid(column=0, row=1, padx=10, pady=15)

lbl_result = tk.Label(frame, text='', font=('Arial', 10))
lbl_result.grid(column=0, row=2)

btn_gen = tk.Button(frame, text='Generate Key', command=key_generate)
btn_gen.grid(column=0, row=3, padx=20, pady=15)
btn_exit = tk.Button(window, text='Close', command=close)
btn_exit.pack(anchor='ne', padx=10, pady=10)

window.mainloop()