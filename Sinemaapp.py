import tkinter as tk
from tkinter import messagebox

# Filmler ve türleri
films = [
    {"name": "The Idea of You", "genre": "Romantik Komedi", "rating": "100%"},
    {"name": "Immaculate", "genre": "Korku", "rating": "91%"},
    {"name": "The Imaginary", "genre": "Animasyon Macera", "rating": "91%"},
    {"name": "Abigail", "genre": "Korku Gerilim", "rating": "71%"},
    {"name": "All We Imagine as Light", "genre": "Drama", "rating": "100%"}
]

# Sinema salonları ve koltuklar
cinema_halls = ['Salon 1', 'Salon 2', 'Salon 3']
seats = {'Salon 1': [f'{i+1}' for i in range(10)], 'Salon 2': [f'{i+1}' for i in range(12)], 'Salon 3': [f'{i+1}' for i in range(15)]}

# İçecek seçenekleri
drinks = ['Su', 'Kola', 'Ayran', 'Meyve Suyu']

# Uygulama penceresi
window = tk.Tk()
window.title("Sinema Bilet Rezervasyon Sistemi")

# Film seçimi fonksiyonu
def select_movie():
    movie = movie_var.get()
    movie_info = next((movie for movie in films if movie['name'] == movie), None)
    if movie_info:
        messagebox.showinfo("Film Bilgisi", f"Film Adı: {movie_info['name']}\nTür: {movie_info['genre']}\nDeğerlendirme: {movie_info['rating']}")
    else:
        messagebox.showerror("Hata", "Film bulunamadı.")

# Koltuk seçimi ve rezervasyon fonksiyonu
def select_seat():
    hall = hall_var.get()
    seat = seat_var.get()
    if seat in seats[hall]:
        messagebox.showinfo("Rezervasyon Onayı", f"{hall} - Koltuk {seat} için rezervasyon başarılı.")
    else:
        messagebox.showerror("Hata", "Geçersiz Koltuk Seçimi.")

# İçecek seçimi fonksiyonu
def select_drink():
    drink = drink_var.get()
    messagebox.showinfo("İçecek Seçimi", f"Seçtiğiniz içecek: {drink}")

# Bilet alımı fonksiyonu
def buy_ticket():
    movie = movie_var.get()
    hall = hall_var.get()
    seat = seat_var.get()
    drink = drink_var.get()
    
    if not movie or not hall or not seat or not drink:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
    else:
        messagebox.showinfo("Bilet Alımı", f"Film: {movie}\nSalon: {hall}\nKoltuk: {seat}\nİçecek: {drink}\nBilet alımınız başarılı!")
        reset_fields()

# Alanları sıfırlama fonksiyonu
def reset_fields():
    movie_var.set('')
    hall_var.set('')
    seat_var.set('')
    drink_var.set('')
    
# Film seçimi
movie_var = tk.StringVar()
movie_menu = tk.OptionMenu(window, movie_var, *[film['name'] for film in films])
movie_menu.pack(pady=10)

# Film bilgilerini gösterme butonu
movie_button = tk.Button(window, text="Film Bilgilerini Göster", command=select_movie)
movie_button.pack(pady=10)

# Film türü seçimi
genre_var = tk.StringVar()
genre_menu = tk.OptionMenu(window, genre_var, *["Romantik Komedi", "Korku", "Animasyon Macera", "Drama", "Korku Gerilim"])
genre_menu.pack(pady=10)

# Sinema salonu seçimi
hall_var = tk.StringVar()
hall_menu = tk.OptionMenu(window, hall_var, *cinema_halls)
hall_menu.pack(pady=10)

# Koltuk seçimi
seat_var = tk.StringVar()
seat_menu = tk.OptionMenu(window, seat_var, *seats['Salon 1'])
seat_menu.pack(pady=10)

# İçecek seçimi
drink_var = tk.StringVar()
drink_menu = tk.OptionMenu(window, drink_var, *drinks)
drink_menu.pack(pady=10)

# Rezervasyon butonu
book_button = tk.Button(window, text="Koltuk Rezervasyonu Yap", command=select_seat)
book_button.pack(pady=10)

# İçecek alma butonu
drink_button = tk.Button(window, text="İçecek Al", command=select_drink)
drink_button.pack(pady=10)

# Bilet alımı butonu
ticket_button = tk.Button(window, text="Bilet Al", command=buy_ticket)
ticket_button.pack(pady=20)

window.mainloop()
