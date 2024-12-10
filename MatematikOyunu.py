import tkinter as tk
import random

# Oyunun ana penceresini oluştur
root = tk.Tk()
root.title("4 İşlem Matematik Oyunu")
root.geometry("400x300")

# Sonuç kutusu
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Soru ve cevap kutuları
question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 14))
answer_entry.pack(pady=10)

# Rastgele işlem ve sayı üreten fonksiyon
def new_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(["+", "-", "*", "/"])

    # Bölme işlemi için tam bölünebilir hale getirin
    if operation == "/":
        num1 = num1 * num2

    question_label.config(text=f"{num1} {operation} {num2}")
    global answer
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 // num2

# Cevabı kontrol eden fonksiyon
def check_answer():
    user_answer = answer_entry.get()
    try:
        if int(user_answer) == answer:
            result_label.config(text="Doğru!", fg="green")
        else:
            result_label.config(text="Yanlış, tekrar dene!", fg="red")
    except ValueError:
        result_label.config(text="Lütfen bir sayı girin.", fg="red")

    answer_entry.delete(0, tk.END)
    new_question()

# Butonlar
check_button = tk.Button(root, text="Cevabı Kontrol Et", font=("Arial", 14), command=check_answer)
check_button.pack(pady=10)

new_question()
root.mainloop()
