from tkinter import *

root = Tk()
root.title("Babye GUI")
root.geometry("640x480") #창 크기 가로 x 세로
# root.geometry("640x480+100+300") #창 크기 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 크기 변경 가능 여부 (비활성화)

# Check Button
chkvar = IntVar() # input the int type value in chkvar
chkbox = Checkbutton(root, text="Not show for 24hours", variable=chkvar)
# chkbox.select() # auto select option
# chkbox.deselect() # auto deselect option
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Not show for a week", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) #select = 1 , deselect = 0
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않게 하는 루프(?)
