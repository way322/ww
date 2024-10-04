import customtkinter
import math


# Функция для решения квадратного уравнения
def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            label_result.config(text="Коэффициент 'a' не может быть равен 0.")
            label_root1.place_forget()
            label_root2.place_forget()
            return

        D = b ** 2 - 4 * a * c

        if D < 0:
            label_result.config(text="Уравнение не имеет корней.")
            label_root1.place_forget()
            label_root2.place_forget()
        elif D == 0:
            x = -b / (2 * a)
            label_result.config(text=f"Корень уравнения: {x:.2f}")
            label_root1.place(relx=0.3, rely=0.5)
            label_root2.place_forget()
        else:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            label_result.config(text="Корни уравнения:")
            label_root1.config(text=f"x1 = {x1:.2f}")
            label_root2.config(text=f"x2 = {x2:.2f}")
            label_root1.place(relx=0.3, rely=0.5)
            label_root2.place(relx=0.3, rely=0.6)

    except ValueError:
        label_result.config(text="Введите корректные значения.")


# Функция для очистки полей и сброса состояния
def clear_fields():
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    entry_c.delete(0, 'end')
    label_result.config(text="")
    label_root1.place_forget()
    label_root2.place_forget()
    entry_a.focus()


# Создание основного окна
win = customtkinter.CTk()
win.title("Решение квадратного уравнения")
win.geometry("400x300")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Метки и поля ввода
label_a = customtkinter.CTkLabel(master=win, text="Введите a:")
label_a.place(relx=0.1, rely=0.1)
entry_a = customtkinter.CTkEntry(master=win)
entry_a.place(relx=0.3, rely=0.1)

label_b = customtkinter.CTkLabel(master=win, text="Введите b:")
label_b.place(relx=0.1, rely=0.2)
entry_b = customtkinter.CTkEntry(master=win)
entry_b.place(relx=0.3, rely=0.2)

label_c = customtkinter.CTkLabel(master=win, text="Введите c:")
label_c.place(relx=0.1, rely=0.3)
entry_c = customtkinter.CTkEntry(master=win)
entry_c.place(relx=0.3, rely=0.3)

# Кнопки
button_solve = customtkinter.CTkButton(master=win, text="Вычислить", command=solve_quadratic)
button_solve.place(relx=0.1, rely=0.4)

button_clear = customtkinter.CTkButton(master=win, text="Новое", command=clear_fields)
button_clear.place(relx=0.5, rely=0.4)

# Метки для вывода результата
label_result = customtkinter.CTkLabel(master=win, text="")
label_result.place(relx=0.1, rely=0.5)

label_root1 = customtkinter.CTkLabel(master=win, text="")
label_root2 = customtkinter.CTkLabel(master=win, text="")

# Установка фокуса на поле ввода 'a'
entry_a.focus()

# Запуск основного цикла
win.mainloop()