#Разработано программистом Кондряковым А.В. специально для нужд ССЦ 28.11.2023

import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
Logo = resource_path("img\Logo.png")

def click_button():
    """
    Конвертирует значение массы яблок в граммы семян и выводит результат в ярлык lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (float(fahrenheit) * 1.7)
    lbl_result["text"] = f"{round(celsius)}"
    podvoi = int(celsius * 75)/4
    lbl_result3["text"] = f"{round(podvoi)}"

# Создание окна.
window = tk.Tk()
window.title("Яблочный калькулятор ССЦ")
window.resizable


fnc_logo = PhotoImage(file="Logo.png")
label1 = ttk.Label(image=fnc_logo, text="Введите вес яблок в кг", compound="top")
label1.grid(padx=6, pady=6)


# Создание рамки для ввода значения массы яблок через виджет
# однострочного текстового поля вместе с ярлыком.
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="кг")

# Макет для рамки ввода массы яблок и ярлыка с текстом грамм
# использует менеджер геометрии .grid().
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")


# Создание кнопки-конвертера и ярлыка для вывода результата.
btn_convert = tk.Button(
    master=window,
    text="Посчитать",
    command=click_button
)
lbl_result = tk.Label(master=window, text="")
lbl_result2 = tk.Label(master=window, text="грамм")
lbl_result3 = tk.Label(master=window, text="")
lbl_result4 = tk.Label(master=window, text="подвоев")

# Настройка макета через менеджер геометрии .grid().
frm_entry.grid(row=1, column=0, padx=10)
btn_convert.grid(row=1, column=1, pady=10)
lbl_result.grid(row=1, column=2, padx=10)
lbl_result2.grid(row=1, column=3, padx=1)
lbl_result3.grid(row=1, column=4, padx=1)
lbl_result4.grid(row=1, column=5, padx=1)

# Запуск приложения.
window.mainloop()
