from tkinter import *
window =Tk()

for i in range(3): 
    for j in range(3):
        frame = Tk.Frame(
            master=window, 
            relief=Tk. RAISED, 
            borderwidth=1
        )
frame.grid(row=i, column=j, padx=5, pady=5)
label = Tk. Label(master=frame, text=f"Row {i}\nColumn {j}")
label. pack()

window.mainloop()