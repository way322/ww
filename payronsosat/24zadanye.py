import customtkinter
from PIL import Image
original_img = Image.open('Время года/зима.png')
original2_img = Image.open('Время года/весна.jpg')
original3_img = Image.open('Время года/лето.jpg')
original4_img = Image.open('Время года/осень.jpg')




win = customtkinter.CTk()
win.title("ggwp")
win.geometry("800x800")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")



def zima():
    img = customtkinter.CTkImage(dark_image=Image.open('Время года/зима.png'),
                                 size=(200, 200))
    labelimg.configure(image=img)
def vesna():
    img = customtkinter.CTkImage(dark_image=Image.open('Время года/весна.jpg'),
                                 size=(200, 200))
    labelimg.configure(image=img)
def leto():
    img = customtkinter.CTkImage(dark_image=Image.open('Время года/лето.jpg'),
                                 size=(200, 200))
    labelimg.configure(image=img)
def osen():
    img = customtkinter.CTkImage(dark_image=Image.open('Время года/осень.jpg'),
                                 size=(200, 200))
    labelimg.configure(image=img)



button_zima = customtkinter.CTkButton(master=win, text="Зима", width=70,command=zima)
button_zima.place(relx=0, rely=0)
button_vesna = customtkinter.CTkButton(master=win, text="Весна", width=70,command=vesna)
button_vesna.place(relx=0.2, rely=0)
button_leto = customtkinter.CTkButton(master=win, text="Лето", width=70,command=leto)
button_leto.place(relx=0.4, rely=0)
button_osen = customtkinter.CTkButton(master=win, text="Осень", width=70,command=osen)
button_osen.place(relx=0.6, rely=0)
labelimg = customtkinter.CTkLabel(master=win, width=400, text="", height=400)
labelimg.place(relx=0, rely=0.2)

win.mainloop()