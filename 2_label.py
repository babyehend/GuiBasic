from tkinter import *

root = Tk()
root.title("Babye GUI")
root.geometry("640x480") #창 크기 가로 x 세로
# root.geometry("640x480+100+300") #창 크기 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 크기 변경 가능 여부 (비활성화)

# label
label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See again")

    global photo2 # 전역변수 설정 필요 (변수 삭제 방지)
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop() #창이 닫히지 않게 하는 루프(?)
