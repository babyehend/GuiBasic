from tkinter import *

root = Tk()
root.title("Babye GUI")
root.geometry("640x480") #창 크기 가로 x 세로
# root.geometry("640x480+100+300") #창 크기 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x, y 창 크기 변경 가능 여부 (비활성화)

# List box
listbox = Listbox(root, selectmode="extended", height=0) #height = 한번에 보이는 리스트의 개수
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # delete
    # listbox.delete(END)

    # check number of elements in list
    # print(listbox.size(), "things in the list")

    # check elements in the list
    print("From 1 to 3 in the list : ", listbox.get(0, 2))

    #check selected element(return the position value of element)
    print("Selected element : ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop() #창이 닫히지 않게 하는 루프(?)
