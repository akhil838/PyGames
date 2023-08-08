import tkinter
from tkinter import *
from tkinter import font
flame = tkinter.Tk()
flame.title("FLAMES")
flame.geometry('300x200+600+300')
flame.resizable(False, False)

meaning = {'F': 'Friends', 'L': 'Love', 'A': 'Ancestors', 'M': 'Marriage', 'E': 'Enemy', 'S': 'Siblings'}

def Calculate():
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    common = []
    name1 = list(n1.get())
    n1.delete(0, END)
    name2 = list(n2.get())
    n2.delete(0, END)

    for i in range(0, len(name1)):
        for j in range(0, len(name2)):
            if name1[i] == name2[j]:
                common.append(name1[i])
                name2.remove(name1[i])
                break
    for i in range(0, len(common)):
        for j in range(0, len(name1)):
            if common[i] == name1[j]:
                name1.remove(common[i])
                break

    num = len(name1) + len(name2)
    t = 0

    while len(flames) != 1:
        count = (num % len(flames)) - 1
        t = ((t + count) % len(flames))
        flames.pop(t)
    print(meaning[flames[0]])
    result['text']=meaning[flames[0]]


ln1 = Label(flame, text="Enter 1st Name")
ln1.pack(padx=0, pady=0)
n1 = Entry(flame, bd=3, width=100)
n1.pack(padx=0)
ln2 = Label(flame, text="Enter 2nd Name")
ln2.pack()
n2 = Entry(flame, bd=3, width=100)
n2.pack()
c = Button(flame, text="Calculate", command=Calculate)
c.pack()
result = Label(flame,text='',font = font.Font(family='Inlanders', size=40))
result.pack()

flame.mainloop()
