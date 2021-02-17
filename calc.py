import tkinter as tk
import buttons

calculator = tk.Tk()
class Dictionary:
    def __init__(self,r,c,i):
        self.dict = {

        }
      
        
object = {}
key = 0
def board():
    # Need separate frames for a display, and the buttons
    display_frame = tk.Frame(calculator, width = 300, height = 300)
    display_frame.pack()

    display_field = tk.Entry(display_frame, width = 50 , justify= "right" )
    display_field.grid(row = 0, column = 0, pady = 5, padx = 5, ipady = 10)
    display_field.insert(0, "user display ")


    btns_frame = tk.Frame(calculator, width = 10, height = 10)
    btns_frame.pack()

    # Generate a 4 * 4 field for buttons
    lista = [[7, 8, 9, "/" ], [4, 5, 6, "*"], [1, 2, 3, "+"], ["=", 0, ".", "-"]]
    
   
    global key
    for r in range(len(lista)):
        for c in range(len(lista[r])):
            tk.Button(btns_frame, width = 10, height = 5, text = (lista[r][c]),
                borderwidth = 1).grid(row=r, column=c)
            function = lista[r][c]
            row = r
            column = c
            object[key] = function, row, column
            print(object[key])
            key += 1
        
                
        


def functions():
    pass

def calculations():
    pass

def answer():
    pass


board()

calculator.mainloop()
