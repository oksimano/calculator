import tkinter as tk

calculator = tk.Tk()
# Need separate frames for a display, and the buttons
input_frame = tk.Frame(calculator, width = 300, height = 300)
input_frame.pack()

input_field = tk.Entry(input_frame, width = 50 , justify= "right" )
input_field.grid(row = 0, column = 0, pady = 5, padx = 5, ipady = 10)
input_field.insert(0, "user input ")


btns_frame = tk.Frame(calculator, width = 300, height = 300)
btns_frame.pack()


# Generate 4 * 4 field 
lista = [7, 8, 9, "/" , 4, 5, 6, "*", 1, 2, 3, "+", "=", 0, ".", "-"]
lol = 0
while lol <= len(lista):
    i = 0
    for r in range(4):
        for c in range(4):
            tk.Button(btns_frame, width = 10, height = 5, text=(lista[i]),
                borderwidth=1 ).grid(row=r,column=c)
            print(lista[i])
            i += 1
            print(i)
    lol +=1

calculator.mainloop()