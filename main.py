import tkinter as tk

def generate_greeting():
    name = name_entry.get()
    greeting = f"Привет, {name}!"
    greeting_label.config(text=greeting)

window = tk.Tk()
window.title("Приветствующая программа")

name_label = tk.Label(window, text="Введите своё имя:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

greeting_button = tk.Button(window, text="Создать приветствие", command=generate_greeting)
greeting_button.pack()

greeting_label = tk.Label(window, text="")
greeting_label.pack()

window.mainloop()