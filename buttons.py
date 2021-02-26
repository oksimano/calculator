import tkinter as tk


calculator = tk.Tk()
object = {}


    
   

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


lista = [['7', '8', '9', "/" ], ['4', '5', '6', "*"], ['1', '2', '3', "+"], ["=", '0', ".", "-"]]

for r in range(len(lista)):
    for c in range(len(lista[r])):
        btn = tk.Button(btns_frame, width = 10, height = 5, text = (lista[r][c]), borderwidth = 1)
        btn.grid(row=r, column=c)
        btn["command"] = lambda btn = btn: merge[button]
  
        function = lista[r][c]
        row = r
        column = c
        object[function] = row, column
        
        button = btn
        ficktion = function
        merge[button] = ficktion
        print("Button clicked on " + merge[button])
    







print(merge)
print("Button clicked on " + merge[button])

calculator.mainloop()
try:
        to_integer = int(a)
        print("integer", a)
        print(type(to_integer))
    except:
        to_string = a 
        print("not a number")
        print(to_string)
        print(type(to_string))