import customtkinter

def heigh_and_width():
    width1 = float(width_entry.get())
    height1 = float(height_entry.get())
    entry.configure(width=width1, height=height1)
    entry2.configure(width=width1, height=height1)

win = customtkinter.CTk()
win.title("ggwp")
win.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


entry = customtkinter.CTkEntry(master=win, width=20)
entry.pack(padx=0, pady=0)
entry2 = customtkinter.CTkEntry(master=win, width=20)
entry2.pack(padx=0, pady=10)


width_entry = customtkinter.CTkEntry(master=win, placeholder_text="Ширина")
width_entry.pack(pady=5)
height_entry = customtkinter.CTkEntry(master=win, placeholder_text="Высота")
height_entry.pack(pady=5)


button = customtkinter.CTkButton(master=win, text="измнить", command=heigh_and_width)
button.pack(padx=0, pady=0)




win.mainloop()