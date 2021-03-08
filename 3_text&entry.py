from tkinter import *

root = Tk()
root.title("Babye GUI")
root.geometry("640x480") #창 크기 가로 x 세로
# root.geometry("640x480+100+300") #창 크기 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 크기 변경 가능 여부 (비활성화)

# Text & Entry
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "input the text")


e = Entry(root, width=30)
e.pack()
e.insert(0, "enter the one line")

def btncmd():
    print(txt.get("1.0", END)) #txt.get("rows.columns", END)
    print(e.get())

    # delete input
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않게 하는 루프(?)
