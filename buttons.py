import tkinter as tk
calculator = tk.Tk()


tk.Entry(calculator, text= "yehha").grid(row = 0)

lista = [7, 8, 9, "/" , 4, 5, 6, "*", 1, 2, 3, "+", "=", 0, ".", "-"]
lol = 0
while lol <= len(lista):
    i = 0
    
    for r in range(4):
        for c in range(4):
            tk.Button(calculator, text=(lista[i]),
                borderwidth=1 ).grid(row=r,column=c)
            print(lista[i])
            i += 1
            print(i)
    lol +=1

calculator.mainloop()