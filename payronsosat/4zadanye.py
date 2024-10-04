import customtkinter



win = customtkinter.CTk()
win.title("ggwp")
win.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")




def functionColor ():
    color_red = button_red.cget("fg_color")
    label.configure(fg_color=color_red)
    label2.configure(text=color_red)
def functionColor1 ():
    color_orange = button_orange.cget("fg_color")
    label.configure(fg_color=color_orange)
    label2.configure(text=color_orange)
def functionColor2 ():
    color_yellow = button_yellow.cget("fg_color")
    label.configure(fg_color=color_yellow)
    label2.configure(text=color_yellow)
def functionColor3 ():
    color_green = button_green.cget("fg_color")
    label.configure(fg_color=color_green)
    label2.configure(text=color_green)
def functionColor4 ():
    color_golub = button_golub.cget("fg_color")
    label.configure(fg_color=color_golub)
    label2.configure(text=color_golub)
def functionColor5 ():
    color_blue = button_blue.cget("fg_color")
    label.configure(fg_color=color_blue)
    label2.configure(text=color_blue)
def functionColor6 ():
    color_violet = button_violet.cget("fg_color")
    label.configure(fg_color=color_violet)
    label2.configure(text=color_violet)


label = customtkinter.CTkLabel(master=win,
                               width=100,
                               height=20,
                               text="")
label.place(relx=0, rely=0.0)
label2 = customtkinter.CTkLabel(master=win,
                               width=100,
                               height=20,
                                text="")
label2.place(relx=0, rely=0.04)

button_red = customtkinter.CTkButton(master=win, text="",fg_color="#FF0000",command=functionColor)
button_red.place(relx=0, rely=0.2)
button_orange = customtkinter.CTkButton(master=win, text="",fg_color="#FF7D00",command=functionColor1)
button_orange.place(relx=0, rely=0.25)
button_yellow = customtkinter.CTkButton(master=win, text="",fg_color="#FFFF00",command=functionColor2)
button_yellow.place(relx=0, rely=0.3)
button_green = customtkinter.CTkButton(master=win, text="",fg_color="#00FF00",command=functionColor3)
button_green.place(relx=0, rely=0.35)
button_golub = customtkinter.CTkButton(master=win, text="",fg_color="#007DFF",command=functionColor4)
button_golub.place(relx=0, rely=0.4)
button_blue = customtkinter.CTkButton(master=win, text="",fg_color="#0000FF",command=functionColor5)
button_blue.place(relx=0, rely=0.45)
button_violet = customtkinter.CTkButton(master=win, text="",fg_color="#7D00FF",command=functionColor6)
button_violet.place(relx=0, rely=0.50)


win.mainloop()