import customtkinter



win = customtkinter.CTk()
win.title("ggwp")
win.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")



def mal():
    label.configure(width=50,
                    height=50)
def norm():
    label.configure(width=150,
                    height=150)
def big():
    label.configure(width=300,
                    height=300)


label = customtkinter.CTkLabel(master=win,
                               width=100,
                               height=100,
                               bg_color="red",
                               text="")
label.pack(padx=100, pady=100)





button = customtkinter.CTkButton(master=win, text="мал",command=mal)
button.place(relx=0, rely=0)

button = customtkinter.CTkButton(master=win, text="сред",command=norm,)
button.place(relx=0.3, rely=0)

button = customtkinter.CTkButton(master=win, text="бол",command=big)
button.place(relx=0.6, rely=0)



win.mainloop()