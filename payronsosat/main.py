import customtkinter
import tkinter


win = customtkinter.CTk()
win.title("ggwp")
win.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


def buttonFunkshen():
    print("соси")

button = customtkinter.CTkButton(master=win, text="хуй", command=buttonFunkshen)
button.place(relx=0.4, rely=0.5)







win.mainloop()