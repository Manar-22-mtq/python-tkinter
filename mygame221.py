from tkinter import *
from random import sample

window = Tk()
img = PhotoImage(file="mylogo.png")

imgLb1 = Label(window, image=img)
Label1 = Label(window, relief='groove', width=2)
label2 = Label(window, relief='groove', width=2)
label3 = Label(window, relief='groove', width=2)
label4 = Label(window, relief='groove', width=2)
label5 = Label(window, relief='groove', width=2)
label6 = Label(window, relief='groove', width=2)

getBtn = Button(window)
resBtn = Button(window)

imgLb1.grid()
Label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()

getBtn.grid()
resBtn.grid()

imgLb1.grid(row=1, column=1, padx=10)
Label1.grid(row=1, column=2, padx=10)
label2.grid(row=1, column=3, padx=10)
label3.grid(row=1, column=4, padx=10)
label4.grid(row=1, column=5, padx=10)
label5.grid(row=1, column=6, padx=10)
label6.grid(row=1, column=7, padx=(10,20))

getBtn.grid(row=2, column=2, padx=4)
resBtn.grid(row=2, column=6, padx=4)

window.title("Peace numbers game")

window.resizable(0, 0)

Label1.configure(text="...")
label2.configure(text="...")
label3.configure(text="...")
label4.configure(text="...")
label5.configure(text="...")
label6.configure(text="...")

getBtn.configure(text="Get My Lucky Number"),
resBtn.configure(text="Reset")


def reset():
    Label1.configure(text="...")
    label2.configure(text="...")
    label3.configure(text="...")
    label4.configure(text="...")
    label5.configure(text="...")
    label6.configure(text="...")
    getBtn.configure(state=NORMAL)
    resBtn.configure(state=DISABLED)


def get_number():
    nums = sample(range(0, 50), 6)

    Label1.configure(text=nums[0])
    label2.configure(text=nums[1])
    label3.configure(text=nums[2])
    label4.configure(text=nums[3])
    label5.configure(text=nums[4])
    label6.configure(text=nums[5])

    getBtn.configure(state=DISABLED)
    resBtn.configure(state=NORMAL)
    resBtn.configure(command=reset)


getBtn.configure(command=get_number)
resBtn.configure(state=DISABLED)

window.mainloop()

