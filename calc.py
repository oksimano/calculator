import tkinter as tk


calculator = tk.Tk()
object = {}

def click(button):
    print("Button clicked on " + merge[button])
    
   

# Need separate frames for a display, and the buttons
display_frame = tk.Frame(calculator, width = 300, height = 300)
display_frame.pack()

display_field = tk.Entry(display_frame, width = 50 , justify= "right" )
display_field.grid(row = 0, column = 0, pady = 5, padx = 5, ipady = 10)
display_field.insert(0, "user_display ")


btns_frame = tk.Frame(calculator, width = 10, height = 10)
btns_frame.pack()

btn = []
lol = ()
merge = {}
# Generate a 4 * 4 field for buttons
def board():
    lista = [['7', '8', '9', "/" ], ['4', '5', '6', "*"], ['1', '2', '3', "+"], ["=", '0', ".", "-"]]
    
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

active="red"
default_color="white"         
        


def functions(args):
    if args == 7:
        print("Plusz 7")


def calculations():
    pass

def answer():
    pass



board()
print(merge)
functions('object')

calculator.mainloop()
