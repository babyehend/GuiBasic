from tkinter import *

root = Tk()
root.title("Babye GUI")
root.geometry("640x480") #창 크기 가로 x 세로
# root.geometry("640x480+100+300") #창 크기 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 크기 변경 가능 여부 (비활성화)

# radio button
label1 = Label(root, text="select menu").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="cheeseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="select drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="cider", value="cider", variable=drink_var)
btn_drink3 = Radiobutton(root, text="smoothie", value="smoothie", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # return the selected radio value
    print(drink_var.get())

btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않게 하는 루프(?)
