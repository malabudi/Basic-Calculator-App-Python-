from tkinter import *

#setup window
window = Tk()
window.title('Calculator')
window.configure(bg = '#1b1e21')
window.resizable(0, 0)

can_insert = True #stores boolean to remember whether we can continue inserting into calculator
can_solve = False #makes user type at least one thing before clicking '='

#function handles all calculations and inputs
def calc(data):
    current_value = output.get('end -2 chars') #gets last character in output
    global can_insert
    global can_solve

    #conditions how data should be inserted
    if data.isnumeric() or data == '.':
        if can_insert: 
            output.insert('end', data)
            can_solve = True
            if current_value == '.' and data == '.': #prevents duplicating decimals
                output.replace('end -3 chars', 'end -1 chars', data)
    elif data in "+-*/" and can_insert:
        output.insert('end', data)
        if current_value in "+-/*": #prevents duplicating operators also replaces existing operators
             output.replace('end-3c', 'end-1c', data)

    #solves equation
    elif data == '=' and can_insert and can_solve:
        equation = output.get('end -1 lines linestart', 'end -1 lines lineend')
        try:
            answer = eval(equation)
            output.insert('end', '\n' + str(answer))
        except SyntaxError:
            output.insert('end', '\n' + 'ERROR: SYNTAX')
        except ZeroDivisionError:
            output.insert('end', '\n' + 'ERROR: 0 DIVISION')
        can_insert = False
        can_solve = False

#handles clearing calculator
def clear():
    output.delete('1.0', 'end')
    global can_insert 
    can_insert = True
        
#------------------------------------------------Begin building calculator
#output for calculator
output = Text(window, font = 'Consolas 16', height = 2, width = 20, wrap = 'none', bg = '#F5F5F5')
output.grid(row = 0, column = 0, columnspan = 4, padx = 15, pady = 15)

#------------------------------------------- Buttons
#clear and operators
b_clear = Button(window, text = 'C', width = 7, height = 3, font = 'arial 9 bold', command = lambda: clear(), bg = '#C72C41', fg = 'white', activebackground = '#EE4540')
b_clear.grid(row = 1, column = 2, padx = (5, 0))

b_div = Button(window, text = '/', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('/'), bg = '#C72C41', fg = 'white', activebackground = '#EE4540')
b_div.grid(row = 1, column = 3, padx = 5)

b_mult = Button(window, text = '*', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('*'), bg = '#C72C41', fg = 'white', activebackground = '#EE4540')
b_mult.grid(row = 2, column = 3)

b_subt = Button(window, text = '-', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('-'), bg = '#C72C41', fg = 'white', activebackground = '#EE4540')
b_subt.grid(row = 3, column = 3)

b_add = Button(window, text = '+', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('+'), bg = '#C72C41', fg = 'white', activebackground = '#EE4540')
b_add.grid(row = 4, column = 3)

b_equal = Button(window, text = '=', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('='), bg = '#C72C41', fg = 'white', activebackground = '#EE4540')
b_equal.grid(row = 5, column = 3, pady = (0, 10))

#numbers
b_9 = Button(window, text = '9', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('9'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_9.grid(row = 2, column = 2, padx = (5, 0), pady = 10)

b_8 = Button(window, text = '8', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('8'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_8.grid(row = 2, column = 1)

b_7 = Button(window, text = '7', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('7'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_7.grid(row = 2, column = 0, padx = 5)

b_6 = Button(window, text = '6', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('6'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_6.grid(row = 3, column = 2, padx = (5, 0))

b_5 = Button(window, text = '5', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('5'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_5.grid(row = 3, column = 1)

b_4 = Button(window, text = '4', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('4'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_4.grid(row = 3, column = 0)

b_3 = Button(window, text = '3', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('3'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_3.grid(row = 4, column = 2, padx = (5, 0), pady = 10)

b_2 = Button(window, text = '2', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('2'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_2.grid(row = 4, column = 1)

b_1 = Button(window, text = '1', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('1'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_1.grid(row = 4, column = 0)

b_0 = Button(window, text = '0', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('0'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_0.grid(row = 5, column = 0, pady = (0, 10))

b_decimal = Button(window, text = '.', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('.'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_decimal.grid(row = 5, column = 1, pady = (0, 10))

b_negative = Button(window, text = '(-)', width = 7, height = 3, font = 'arial 9 bold', command = lambda: calc('-'), bg = '#801336', fg = 'white', activebackground = '#EE4540')
b_negative.grid(row = 5, column = 2, padx = (5, 0), pady = (0, 10))

#run calculator
window.mainloop()

