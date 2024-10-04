import customtkinter

def display_text():
    text = entry.get()
    new_win = customtkinter.CTk()
    new_win.title("ggwp2")
    new_win.geometry("200x200")
    label = customtkinter.CTkLabel(master=new_win, text=text)
    label.pack(padx=20, pady=10)
    new_win.mainloop()

win = customtkinter.CTk()
win.title("ggwp")
win.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


label = customtkinter.CTkLabel(master=win, width=100, height=100, text="Введите название книги")
label.pack(padx=0, pady=0)

entry = customtkinter.CTkEntry(master=win, width=300)
entry.pack(padx=0, pady=5)

button = customtkinter.CTkButton(master=win, text="ОК", command=display_text)
button.pack(padx=0, pady=10)

win.mainloop()
