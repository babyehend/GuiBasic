from tkinter import *

root = Tk()
root.title("Babye GUI")
root.geometry("640x480") #창 크기 가로 x 세로
# root.geometry("640x480+100+300") #창 크기 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 크기 변경 가능 여부 (비활성화)

# Button
# btn1 = Button(root, text="Button 1")
# btn1.pack()
#
# btn2 = Button(root, padx=5, pady=10, text="Button 2")
# btn2.pack()
#
# btn3 = Button(root, padx=10, pady=5, text="Button 3")
# btn3.pack()
#
# btn4 = Button(root, width=5, height=3, text="Button 4")
# btn4.pack()
# # pad = 여백 , width, height = 고정 크기
#
# btn5 = Button(root, fg="gray", bg="white", text="Button 5")
# btn5.pack()
#
# photo = PhotoImage(file="img.png")
# btn6 = Button(root, image=photo)
# btn6.pack()
#
# def btncmd():
#     print('button7 has been activated')
#
# btn7 = Button(root, text="active button", command=btncmd)
# btn7.pack()


# label
# label1 = Label(root, text="Hello")
# label1.pack()
#
# photo = PhotoImage(file="img.png")
# label2 = Label(root, image=photo)
# label2.pack()
#
# def change():
#     label1.config(text="See again")
#
#     global photo2 # 전역변수 설정 필요 (변수 삭제 방지)
#     photo2 = PhotoImage(file="img2.png")
#     label2.config(image=photo2)
#
# btn = Button(root, text="click", command=change)
# btn.pack()


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
