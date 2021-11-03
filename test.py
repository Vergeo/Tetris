import tkinter as tk

def print_var() :
    print(var.get())

root = tk.Tk()
var = tk.StringVar()
entry = tk.Entry(textvariable=var)
entry.pack()
button =tk.Button(command=print_var)
button.pack()
root.mainloop()