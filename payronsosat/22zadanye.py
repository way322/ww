import customtkinter
import math


win = customtkinter.CTk()
win.title("ggwp")
win.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


def Descriment():
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            new_win = customtkinter.CTk()
            new_win.title("ggwp2")
            new_win.geometry("200x200")
            label = customtkinter.CTkLabel(master=new_win, text="a не должно ровняется 0")
            label.pack(padx=20, pady=10)
            new_win.mainloop()
            return

        D = b ** 2 - 4 * a * c

        if D < 0:
            new_win = customtkinter.CTk()
            new_win.title("ggwp2")
            new_win.geometry("200x200")
            label = customtkinter.CTkLabel(master=new_win, text="не имеет корней")
            label.pack(padx=20, pady=10)
            new_win.mainloop()
        elif D == 0:
            x = -b / (2 * a)
            labelKoren1.configure(text=x)
        elif D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            labelKoren1.configure(text=x1)
            labelKoren2.configure(text=x2)

def clear():
    labelKoren1.configure(text="")
    labelKoren2.configure(text="")
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    entry_c.delete(0, 'end')

label_a = customtkinter.CTkLabel(master=win, width=50, text="a")
label_a.place(relx=0, rely=0)
label_b = customtkinter.CTkLabel(master=win, width=50, text="b")
label_b.place(relx=0.2, rely=0)
label_c = customtkinter.CTkLabel(master=win, width=50, text="c")
label_c.place(relx=0.4, rely=0)

entry_a = customtkinter.CTkEntry(master=win, width=50)
entry_a.place(relx=0, rely=0.1)
entry_b = customtkinter.CTkEntry(master=win, width=50)
entry_b.place(relx=0.2, rely=0.1)
entry_c = customtkinter.CTkEntry(master=win, width=50)
entry_c.place(relx=0.4, rely=0.1)

labelKoren = customtkinter.CTkLabel(master=win, width=50, text="Корни уравнения")
labelKoren.place(relx=0.2, rely=0.2)
labelKoren1 = customtkinter.CTkLabel(master=win, width=50,text="")
labelKoren1.place(relx=0.15, rely=0.3)
labelKoren2 = customtkinter.CTkLabel(master=win, width=50,text="")
labelKoren2.place(relx=0.3, rely=0.3)


button = customtkinter.CTkButton(master=win, text="Вычеслить",command=Descriment)
button.place(relx=0, rely=0.4)
buttonclear = customtkinter.CTkButton(master=win, text="новое",command=clear)
buttonclear.place(relx=0.3, rely=0.4)


win.mainloop()