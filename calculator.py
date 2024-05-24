import tkinter as tk
from tkinter import messagebox

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression)) 
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        expression = ""

window = tk.Tk()
window.title("Calculator")
window.geometry("650x800")

expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(window)
input_frame.pack(expand=True, fill='both')

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), justify='right', bd=10, bg="#eee")
input_field.pack(expand=True, fill='both')

btns_frame = tk.Frame(window)
btns_frame.pack(expand=True, fill='both')

clear = tk.Button(btns_frame, text='C', font=('arial', 18, 'bold'), fg='black', width=32, height=3, bd=1, bg='#eee', command=lambda: btn_clear())
clear.grid(row=0, column=0, columnspan=3)
divide = tk.Button(btns_frame, text='/', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#eee', command=lambda: btn_click('/'))
divide.grid(row=0, column=3)

btn7 = tk.Button(btns_frame, text='7', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(7))
btn7.grid(row=1, column=0)
btn8 = tk.Button(btns_frame, text='8', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(8))
btn8.grid(row=1, column=1)
btn9 = tk.Button(btns_frame, text='9', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(9))
btn9.grid(row=1, column=2)
multiply = tk.Button(btns_frame, text='*', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#eee', command=lambda: btn_click('*'))
multiply.grid(row=1, column=3)

btn4 = tk.Button(btns_frame, text='4', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(4))
btn4.grid(row=2, column=0)
btn5 = tk.Button(btns_frame, text='5', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(5))
btn5.grid(row=2, column=1)
btn6 = tk.Button(btns_frame, text='6', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(6))
btn6.grid(row=2, column=2)
subtract = tk.Button(btns_frame, text='-', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#eee', command=lambda: btn_click('-'))
subtract.grid(row=2, column=3)

btn1 = tk.Button(btns_frame, text='1', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(1))
btn1.grid(row=3, column=0)
btn2 = tk.Button(btns_frame, text='2', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(2))
btn2.grid(row=3, column=1)
btn3 = tk.Button(btns_frame, text='3', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#fff', command=lambda: btn_click(3))
btn3.grid(row=3, column=2)
add = tk.Button(btns_frame, text='+', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#eee', command=lambda: btn_click('+'))
add.grid(row=3, column=3)

btn0 = tk.Button(btns_frame, text='0', font=('arial', 18, 'bold'), fg='black', width=21, height=3, bd=1, bg='#fff', command=lambda: btn_click(0))
btn0.grid(row=4, column=0, columnspan=2)
decimal = tk.Button(btns_frame, text='.', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#eee', command=lambda: btn_click('.'))
decimal.grid(row=4, column=2)
equals = tk.Button(btns_frame, text='=', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, bg='#eee', command=lambda: btn_equal())
equals.grid(row=4, column=3)

window.mainloop()
