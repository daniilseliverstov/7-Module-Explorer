import tkinter

import os

from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выбирите файл', filetypes=(('Текстовый файл', '.txt'),
                                                                                            ('Все файлы', '*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)

window = tkinter.Tk()  #Объект класса, окно приложения
window.title('Проводник')  # Имя окна
window.geometry('550x150')  # Задаем размер окна
window.configure(bg='black')  # Фон окна
window.resizable(False, False) # Запрещаем менять габариты окна
text = tkinter.Label(window, text='Текст', width=80, height=5, background='silver')  # Создаем объект, текст, принадлежащий окну, задаем ширину/высоту
text.grid(column=1, row=1)  #метод позволяет делить окно на колонны и ряды, размещаем в 1 колонне 1 ряду
button_select = tkinter.Button(window, width=25, height=5, text='Выбирите файл', command=file_select)  # Добавляем кнопку
button_select.grid(column=1, row=2)
window.mainloop()  # Обновление окна, создается сразу после window. Весь код между
