import customtkinter

def vrema():
    time = float(entry.get())
    if 4 <= time <=11:
        label_vrem.configure(text="Доброе утро!")
    elif 12 <= time <= 16:
        label_vrem.configure(text="Добрый день!")
    elif 17 <= time <= 23:
        label_vrem.configure(text="Добрый вечер!")
    elif 24 <= time <= 3:
        label_vrem.configure(text="Доброй ночи!")
    else :
        label_vrem.configure(text="Не существует времени")
def clear():
    entry.delete(0, 'end')
    label_vrem.configure(text="")


win = customtkinter.CTk()
win.title("ggwp")
win.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")




label = customtkinter.CTkLabel(master=win, width=100, text="Введите текущее время")
label.place(relx=0, rely=0)

entry = customtkinter.CTkEntry(master=win, width=50)
entry.place(relx=0.25, rely=0)

label_vrem = customtkinter.CTkLabel(master=win,width=100, text="")
label_vrem.place(relx=0.3, rely=0.1)


button = customtkinter.CTkButton(master=win, text="Показать", command=vrema)
button.place(relx=0, rely=0.3)
button_clear = customtkinter.CTkButton(master=win, text="Очистить", command=clear)
button_clear.place(relx=0.5, rely=0.3)



win.mainloop()