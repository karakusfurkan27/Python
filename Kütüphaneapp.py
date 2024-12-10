import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


# Veritabanını oluşturma ve başlangıç türlerini ekleme
def initialize_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres (id)
        )
    """)

    # Başlangıç türlerini ekle
    default_genres = [
        "Roman", "Çocuk Kitapları", "Dünya Klasikleri", "Yardımcı Kaynaklar", "Bilişim"
    ]
    for genre in default_genres:
        try:
            cursor.execute("INSERT INTO genres (name) VALUES (?)", (genre,))
        except sqlite3.IntegrityError:
            pass  # Tür zaten varsa atla

    conn.commit()
    conn.close()


# Veritabanını sıfırla
def reset_database():
    if messagebox.askyesno("Veritabanı Sıfırla", "Tüm veriler silinecek. Devam etmek istiyor musunuz?"):
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS books")
        cursor.execute("DROP TABLE IF EXISTS genres")
        conn.commit()
        conn.close()
        initialize_database()
        messagebox.showinfo("Başarılı", "Veritabanı başarıyla sıfırlandı.")


# Kullanıcı Girişi
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Başarılı", "Giriş başarılı!")
        main_window()
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")


# Kitap Ekleme
def add_book():
    def save_book():
        title = title_entry.get()
        author = author_entry.get()
        genre_name = genre_combobox.get()

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM genres WHERE name = ?", (genre_name,))
        genre = cursor.fetchone()

        if genre:
            genre_id = genre[0]
            cursor.execute("INSERT INTO books (title, author, genre_id) VALUES (?, ?, ?)",
                           (title, author, genre_id))
            conn.commit()
            messagebox.showinfo("Başarılı", "Kitap başarıyla eklendi.")
        else:
            messagebox.showerror("Hata", "Seçilen tür bulunamadı.")
        conn.close()

    book_window = Toplevel(root)
    book_window.title("Kitap Ekle")

    Label(book_window, text="Kitap Adı:", font=("Arial", 12)).pack(pady=5)
    title_entry = Entry(book_window, font=("Arial", 12))
    title_entry.pack(pady=5)

    Label(book_window, text="Yazar:", font=("Arial", 12)).pack(pady=5)
    author_entry = Entry(book_window, font=("Arial", 12))
    author_entry.pack(pady=5)

    Label(book_window, text="Tür:", font=("Arial", 12)).pack(pady=5)
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM genres")
    genres = [row[0] for row in cursor.fetchall()]
    conn.close()
    genre_combobox = Combobox(book_window, values=genres, font=("Arial", 12))
    genre_combobox.pack(pady=5)

    Button(book_window, text="Kaydet", command=save_book, bg="blue", fg="white").pack(pady=10)


# Kitap Silme
def delete_book():
    def remove_book():
        book_title = book_entry.get()
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE title = ?", (book_title,))
        if cursor.rowcount > 0:
            conn.commit()
            messagebox.showinfo("Başarılı", "Kitap başarıyla silindi.")
        else:
            messagebox.showerror("Hata", "Bu isimde bir kitap bulunamadı.")
        conn.close()

    delete_window = Toplevel(root)
    delete_window.title("Kitap Sil")

    Label(delete_window, text="Silinecek Kitap Adı:", font=("Arial", 12)).pack(pady=5)
    book_entry = Entry(delete_window, font=("Arial", 12))
    book_entry.pack(pady=5)
    Button(delete_window, text="Sil", command=remove_book, bg="red", fg="white").pack(pady=10)


# Kitap Güncelleme
def update_book():
    def update():
        old_title = old_title_entry.get()
        new_title = new_title_entry.get()
        new_author = new_author_entry.get()
        new_genre = genre_combobox.get()

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM genres WHERE name = ?", (new_genre,))
        genre = cursor.fetchone()

        if genre:
            genre_id = genre[0]
            cursor.execute("""
                UPDATE books 
                SET title = ?, author = ?, genre_id = ? 
                WHERE title = ?
            """, (new_title, new_author, genre_id, old_title))
            if cursor.rowcount > 0:
                conn.commit()
                messagebox.showinfo("Başarılı", "Kitap başarıyla güncellendi.")
            else:
                messagebox.showerror("Hata", "Güncellenecek kitap bulunamadı.")
        conn.close()

    update_window = Toplevel(root)
    update_window.title("Kitap Güncelle")

    Label(update_window, text="Eski Kitap Adı:", font=("Arial", 12)).pack(pady=5)
    old_title_entry = Entry(update_window, font=("Arial", 12))
    old_title_entry.pack(pady=5)

    Label(update_window, text="Yeni Kitap Adı:", font=("Arial", 12)).pack(pady=5)
    new_title_entry = Entry(update_window, font=("Arial", 12))
    new_title_entry.pack(pady=5)

    Label(update_window, text="Yeni Yazar:", font=("Arial", 12)).pack(pady=5)
    new_author_entry = Entry(update_window, font=("Arial", 12))
    new_author_entry.pack(pady=5)

    Label(update_window, text="Yeni Tür:", font=("Arial", 12)).pack(pady=5)
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM genres")
    genres = [row[0] for row in cursor.fetchall()]
    conn.close()
    genre_combobox = Combobox(update_window, values=genres, font=("Arial", 12))
    genre_combobox.pack(pady=5)

    Button(update_window, text="Güncelle", command=update, bg="orange", fg="white").pack(pady=10)


# Ana Pencere
def main_window():
    main = Toplevel(root)
    main.title("Kütüphane Yönetim Sistemi")
    main.geometry("400x500")
    main.configure(bg="#e8f4f8")

    Label(main, text="Kütüphane Yönetim Sistemi", font=("Arial", 16, "bold"), bg="#e8f4f8").pack(pady=10)

    Button(main, text="Kitap Ekle", command=add_book, bg="#0275d8", fg="white", width=20).pack(pady=10)
    Button(main, text="Kitap Sil", command=delete_book, bg="red", fg="white", width=20).pack(pady=10)
    Button(main, text="Kitap Güncelle", command=update_book, bg="orange", fg="white", width=20).pack(pady=10)
    Button(main, text="Veritabanı Sıfırla", command=reset_database, bg="#5cb85c", fg="white", width=20).pack(pady=10)


# Ana Uygulama Penceresi (Login)
root = Tk()
root.title("Giriş Yap")
root.geometry("400x250")
root.configure(bg="#f7f7f7")

Label(root, text="Kütüphane Giriş", font=("Arial", 18, "bold"), bg="#f7f7f7").pack(pady=10)

Label(root, text="Kullanıcı Adı:", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
username_entry = Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

Label(root, text="Şifre:", font=("Arial", 12), bg="#f7f7f7").pack(pady=5)
password_entry = Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

Button(root, text="Giriş Yap", command=login, bg="#5cb85c", fg="white", width=15).pack(pady=20)

# Veritabanını başlat
initialize_database()

root.mainloop()
