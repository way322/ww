import customtkinter
import math


win = customtkinter.CTk()
win.title("ggwp")
win.geometry("200x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def calculatorPlus():
    a = float(entry_clk1.get())
    b = float(entry_clk2.get())
    x = a + b
    labelotvet.configure(text=x)
def calculatorMinus():
    a = float(entry_clk1.get())
    b = float(entry_clk2.get())
    x = a - b
    labelotvet.configure(text=x)
def calculatorUmnoj():
    a = float(entry_clk1.get())
    b = float(entry_clk2.get())
    x = a * b
    labelotvet.configure(text=x)
def calculatorDel():
    a = float(entry_clk1.get())
    b = float(entry_clk2.get())
    x = a / b
    labelotvet.configure(text=x)


entry_clk1 = customtkinter.CTkEntry(master=win, width=70)
entry_clk1.place(relx=0, rely=0)
entry_clk2 = customtkinter.CTkEntry(master=win, width=70)
entry_clk2.place(relx=0, rely=0.06)

button_plus = customtkinter.CTkButton(master=win, text="+", width=70, command=calculatorPlus)
button_plus.place(relx=0, rely=0.11)
button_minus = customtkinter.CTkButton(master=win, text="-", width=70, command=calculatorMinus)
button_minus.place(relx=0, rely=0.16)
button_umnoj = customtkinter.CTkButton(master=win, text="*", width=70, command=calculatorUmnoj)
button_umnoj.place(relx=0, rely=0.21)
button_del = customtkinter.CTkButton(master=win, text="/", width=70, command=calculatorDel)
button_del.place(relx=0, rely=0.26)

labelotvet = customtkinter.CTkLabel(master=win, width=50,text="")
labelotvet.place(relx=0, rely=0.34)





win.mainloop()