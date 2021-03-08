import tkinter.ttk as ttk # import ttk to use combobox
from tkinter import *

root = Tk()
root.title("Babye GUI")
root.geometry("640x480") #창 크기 가로 x 세로
# root.geometry("640x480+100+300") #창 크기 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 크기 변경 가능 여부 (비활성화)

# combobox
values = [i for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("")

def btncmd():
    pass

btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않게 하는 루프(?)
