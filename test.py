''' This is a test tab'''

import tkinter as tk


calculator = tk.Tk()
object = {}
calc_input = tk.StringVar()



merge = {}   
   

# Need separate frames for a display, and the buttons
display_frame = tk.Frame(calculator, width = 300, height = 300)
display_frame.pack()

display_field = tk.Entry(display_frame, width = 50 , textvariable = calc_input)
display_field.grid(row = 0, column = 0, pady = 5, padx = 5, ipady = 10)



btns_frame = tk.Frame(calculator, width = 10, height = 10)
btns_frame.pack()


# Generate a 4 * 4 field for buttons
def board():
   
    lista = [['CL', '«', ' ', '/'], ['7', '8', '9', '*' ], ['4', '5', '6', '+'], ['1', '2', '3', '-'], ['', '0', '.', '=']]
    print(lista[0])
    for r in range(len(lista)):
        for c in range(len(lista[r])):
            btn = tk.Button(btns_frame, width = 10, height = 5, text = (lista[r][c]), borderwidth = 1)
            btn.grid(row=r, column=c)
            btn["command"] = lambda btn = btn: click(btn)
            function = lista[r][c]
            row = r
            column = c
            object[function] = row, column
           
            button = btn
            ficktion = function
            merge[button] = ficktion
    
    return merge[button]
    return btn    


def click(button):
    
    print("Button clicked on " + merge[button])
    a  = functions(merge[button])
    


def functions(a):
    display_item = a
    
    
    
    if a == '=':
        display_field.delete(tk.END)
        answer = eval(display_field.get())
        print(answer)    
        display_field.delete(0,tk.END)
        display_field.insert(tk.END, answer)
    elif a == 'CL':
        display_field.delete(0,tk.END)
    elif a == '«':
        display_field.delete(len(display_field.get())-1)
    else:
        display_field.insert(tk.END, display_item)    
       
       






board()
calculator.mainloop()
