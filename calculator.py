from tkinter import *
a = Tk()
a.title('calculator')
a.configure(bg='pink')

def clear():
    db.delete(0,END)

def btn_clk(num):
    cur_num = db.get()
    clear()
    f_num = cur_num + num
    db.insert(0,f_num)

first_num = 0
def add():
    global first_num
    first_num = db.get()
    clear()

def equal():
    global first_num
    second_num = db.get()
    clear()
    result = int(first_num) + int(second_num)
    db.insert(0, result)

db = Entry(a,width=14, font=('Arial',28), justify=RIGHT)
btn_0 = Button(a,text='0', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('0'))
btn_1 = Button(a,text='1', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('1'))
btn_2 = Button(a,text='2', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('2'))
btn_3 = Button(a,text='3', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('3'))
btn_4 = Button(a,text='4', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('4'))
btn_5 = Button(a,text='5', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('5'))
btn_6 = Button(a,text='6', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('6'))
btn_7 = Button(a,text='7', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('7'))
btn_8 = Button(a,text='8', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('8'))
btn_9 = Button(a,text='9', padx=36, pady=10, font=('Arial', 14), command= lambda: btn_clk('9'))
btn_clear = Button(a, text='clear', padx=74, pady=10, font=('Arial', 14), command = clear)
btn_add = Button(a, text='+', padx=36, pady=10, font=('Arial',14),command=add)
btn_sub = Button(a, text='-', padx=36, pady=10, font=('Arial',14),command=add)
btn_mul = Button(a, text='*', padx=36, pady=10, font=('Arial',14))
btn_div = Button(a, text='/', padx=36, pady=10, font=('Arial',14))
btn_equal = Button(a, text='=', padx=36, pady=48, font=('Arial',14),command=equal)


db.grid(row=0, column=0,columnspan=3, padx=10, pady=10)
btn_0.grid(row=4, column=0,padx=2, pady=2)
btn_1.grid(row=3, column=0,padx=2, pady=2)
btn_2.grid(row=3, column=1,padx=2, pady=2)
btn_3.grid(row=3, column=2,padx=2, pady=2)
btn_4.grid(row=2, column=0,padx=2, pady=2)
btn_5.grid(row=2, column=1,padx=2, pady=2)
btn_6.grid(row=2, column=2,padx=2, pady=2)
btn_7.grid(row=1, column=0,padx=2, pady=2)
btn_8.grid(row=1, column=1,padx=2, pady=2)
btn_9.grid(row=1, column=2,padx=2, pady=2)
btn_clear.grid(row=4,column=1, columnspan=2, padx=2, pady=2)
btn_add.grid(row=5,column=0, padx=2, pady=2)
btn_sub.grid(row=5,column=1, padx=2, pady=2)
btn_mul.grid(row=6,column=0, padx=2, pady=2)
btn_div.grid(row=6,column=1, padx=2, pady=2)
btn_equal.grid(row=5,column=2, rowspan=2, padx=2, pady=2)

mainloop()