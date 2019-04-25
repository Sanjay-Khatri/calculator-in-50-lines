from tkinter import *
sample = Tk()
sample.geometry('500x500')

keys =[[('7',  "seven"), ('8',"eight"), ('9',  "nine"), ('+', "add")],
       [('4',  "four"), ('5', "five"), ('6',  "six"), ('-',  "minus")],
       [('1',  "one"), ('2',  "two"), ('3',  "three"), ('*',  "star")],
       [('0',  "zero"), ('=',"equals"), ('/',  "divide"), ('C', "calculate")],
]
def cal(event):
    try:
        s = eval(entry1.get())
        entry1.delete(0, END)
        entry1.insert(0, s)
    except SyntaxError:
        entry1.delete(0, END)
        entry1.insert(0, "Syntax ERROR")

def click_event(inp):
    for key in keys:
        for num in key:
            if (inp == 'calculate'):
                entry1.delete(0, END)

            elif(inp == 'equals'):
                cal('<Button-1>')

            elif(inp == num[1]):
                st = entry1.get()
                entry1.delete(0, END)
                entry1.insert(0, st + num[0])


entry1 =Entry(sample, justify = 'right', font ="Helvetica 50")
entry1.bind('<Return>',cal)
entry1.grid(row = 0, column = 0, columnspan = 4, stick = 'nsew' )

row = 1
for key in keys:
    col = 0
    for num in key:
        action = lambda x = num[1]:click_event(x)
        Button(sample,text = num[0],font ="Helvetica 30", command = action).grid(row = row, column = col, stick = 'nsew')
        col += 1
    row += 1

#configure

for i in range(0,4):
    sample.columnconfigure(i, weight=5)
    sample.rowconfigure(i, weight=5)

sample.rowconfigure(4,weight=5)

sample.mainloop()