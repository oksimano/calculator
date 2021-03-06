import tkinter as tk
import tkinter.font as tkFont


calculator = tk.Tk()
calc_input = tk.StringVar()
merge = {}   
   
calculator.title('Calculator')
fontStyle = tkFont.Font(family = "Helvetica ", size = 12)
# Need separate frames for a display, and the buttons
display_frame = tk.Frame(calculator)
display_frame.pack()

display_field = tk.Entry(display_frame, width = 25 , textvariable = calc_input, font = "Helvetica 16 bold")
display_field.grid(row = 0, column = 0, pady = 12, padx = 12, ipady = 10)



btns_frame = tk.Frame(calculator, width = 15, height = 15)
btns_frame.pack()


# Generate a 4 * 4 field for buttons
def board():
   
    lista = [['Clear', '«', '%', '/'], ['7', '8', '9', '*' ], ['4', '5', '6', '+'], ['1', '2', '3', '-'], ['+/-', '0', '.', '=']]
    
    for r in range(len(lista)):
        for c in range(len(lista[r])):
            btn = tk.Button(btns_frame, width = 8, height = 5, text = (lista[r][c]), borderwidth = .5,  font = fontStyle)
            btn.grid(row=r, column=c)
            btn["command"] = lambda btn = btn: click(btn)
            merge[btn] = lista[r][c]
            
      


def click(btn):
    
    print("Button clicked on " + merge[btn])
    functions(merge[btn])
    


def functions(key):
    display_item = key
    if key == '=':
        display_field.delete(tk.END)
        answer = eval(display_field.get())
        print(answer)    
        display_field.delete(0,tk.END)
        display_field.insert(tk.END, answer)
    elif key == 'Clear':
        display_field.delete(0,tk.END)
    elif key == '«':
        display_field.delete(len(display_field.get())-1)
    elif key == "+/-":
        display_field.insert('0', "-")
    else:
        display_field.insert(tk.END, key)    
       
       






board()
calculator.mainloop()
