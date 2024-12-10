import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

class StadiumGUI:
    def __init__(self, root, name):
        self.root = root
        self.root.title(name)
        self.name = name

        # Takımlar ve şampiyonluk sayıları
        self.teams = {
            "Türkiye": {
                "Galatasaray": {"cups": 24},  # Güncellenmiş Galatasaray şampiyonluk sayısı
                "Fenerbahçe": {"cups": 19},
                "Beşiktaş": {"cups": 16},
                "Trabzonspor": {"cups": 7},
                "Başakşehir": {"cups": 0},
                "Sivasspor": {"cups": 0},
                "Göztepe": {"cups": 1},
            },
            "Avrupa Milli Takımlar": {
                "Almanya": {"cups": 4},
                "Fransa": {"cups": 2},
                "İspanya": {"cups": 1},
                "İtalya": {"cups": 4},
                "Portekiz": {"cups": 1},
                "İngiltere": {"cups": 1},
                "Hollanda": {"cups": 0},
                "Belçika": {"cups": 0},
                "Arnavutluk": {"cups": 0},
                "Türkiye": {"cups": 0},  # Türkiye A Milli Takımının kupa sayısı
            },
            "Avrupa Kulüpleri": {
                "Real Madrid": {"cups": 14},
                "Barcelona": {"cups": 5},
                "Bayern Münih": {"cups": 6},
                "Manchester United": {"cups": 3},
                "Liverpool": {"cups": 6},
                "Chelsea": {"cups": 2},
                "Paris Saint-Germain": {"cups": 0},
                "Juventus": {"cups": 2},
                "AC Milan": {"cups": 7},
                "Borussia Dortmund": {"cups": 0},
            }
        }

        # Veritabanı bağlantısı
        self.conn = sqlite3.connect("stadium.db")
        self.cursor = self.conn.cursor()
        self.setup_database()

        # Bilet yönetimi
        self.rows = None
        self.seats_per_row = None
        self.seating = []
        self.buttons = []

        self.login_screen()

    def setup_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                row INTEGER,
                seat INTEGER,
                customer_name TEXT,
                price REAL,
                team TEXT
            )
        """)
        self.conn.commit()

    def login_screen(self):
        login_frame = tk.Frame(self.root, bg="#004B87")
        login_frame.pack(pady=50)

        tk.Label(login_frame, text="Admin Şifresini Girin", font=("Arial", 14), bg="#004B87", fg="white").grid(row=0, column=0, pady=10)
        password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
        password_entry.grid(row=1, column=0, pady=10)

        tk.Button(login_frame, text="Giriş Yap", font=("Arial", 14), command=lambda: self.verify_login(password_entry.get(), login_frame), bg="#FF6347", fg="white").grid(row=2, column=0, pady=10)

    def verify_login(self, password, frame):
        if password == "admin":
            frame.destroy()
            self.show_team_selection()
        else:
            messagebox.showerror("Hata", "Yanlış Şifre")

    def show_team_selection(self):
        team_frame = tk.Frame(self.root, bg="#ADD8E6")
        team_frame.pack(pady=20)

        tk.Label(team_frame, text="Takım Seçin", font=("Arial", 14), bg="#ADD8E6").grid(row=0, column=0, padx=10)

        self.team_var = tk.StringVar()
        self.team_var.set("Türkiye")  # Default kategori

        category_menu = tk.OptionMenu(team_frame, self.team_var, "Türkiye", "Avrupa Milli Takımlar", "Avrupa Kulüpleri")
        category_menu.grid(row=1, column=0, padx=10)

        self.team_listbox = tk.Listbox(team_frame, width=40, height=10, bg="#F0F8FF", fg="black", font=("Arial", 12))
        self.team_listbox.grid(row=2, column=0, padx=10, pady=10)

        self.update_teams_list()

        tk.Button(team_frame, text="Seçilen Takımı Göster", font=("Arial", 12), command=self.show_selected_team, bg="#FF6347", fg="white").grid(row=3, column=0, pady=10)

        self.team_var.trace("w", lambda *args: self.update_teams_list())

    def update_teams_list(self):
        category = self.team_var.get()
        teams = self.teams.get(category, {})
        
        self.team_listbox.delete(0, tk.END)
        for team in teams:
            self.team_listbox.insert(tk.END, f"{team} - Şampiyonluk Sayısı: {teams[team]['cups']}")

    def show_selected_team(self):
        selected_team_index = self.team_listbox.curselection()
        if selected_team_index:
            team_name = self.team_listbox.get(selected_team_index)
            team_name_only = team_name.split(" -")[0]
            cups = self.teams[self.team_var.get()][team_name_only]["cups"]
            messagebox.showinfo("Seçilen Takım", f"Seçilen Takım: {team_name_only}\nŞampiyonluk Sayısı: {cups}")
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir takım seçin.")

    def setup_dynamic_seating(self):
        config_frame = tk.Frame(self.root, bg="#FFFAF0")
        config_frame.pack(pady=20)

        tk.Label(config_frame, text="Koltuk Sayısını ve Satır Sayısını Girin", font=("Arial", 12), bg="#FFFAF0").grid(row=0, column=0, padx=5)
        rows_entry = tk.Entry(config_frame, font=("Arial", 12))
        rows_entry.grid(row=0, column=1, padx=5)

        tk.Label(config_frame, text="Her Satırda Koltuk Sayısı", font=("Arial", 12), bg="#FFFAF0").grid(row=1, column=0, padx=5)
        seats_entry = tk.Entry(config_frame, font=("Arial", 12))
        seats_entry.grid(row=1, column=1, padx=5)

        tk.Button(config_frame, text="Uygula", font=("Arial", 12), command=lambda: self.initialize_seating(rows_entry.get(), seats_entry.get(), config_frame), bg="#FF6347", fg="white").grid(row=2, columnspan=2, pady=10)

    def initialize_seating(self, rows, seats_per_row, frame):
        try:
            self.rows = int(rows)
            self.seats_per_row = int(seats_per_row)
            self.seating = [['Empty' for _ in range(self.seats_per_row)] for _ in range(self.rows)]
            frame.destroy()
            self.create_ui()
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz giriş. Lütfen sayısal değerler girin.")

    def create_ui(self):
        tk.Label(self.root, text=f"{self.name} Koltuk Düzeni", font=("Arial", 16), bg="#FF6347", fg="white").grid(row=0, columnspan=self.seats_per_row + 2, pady=10)

        # Koltuk butonları
        self.buttons = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.seats_per_row):
                btn = tk.Button(self.root, text=f"{i+1}-{j+1}", width=8, height=2, bg="lightgreen", command=lambda r=i, s=j: self.book_seat(r, s))
                btn.grid(row=i+1, column=j, padx=5, pady=5)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

        # Reset ve Rapor Butonları
        tk.Button(self.root, text="Tümünü Sıfırla", bg="#FF6347", fg="white", command=self.reset_all).grid(row=self.rows+1, column=0, columnspan=self.seats_per_row//2, pady=10)
        tk.Button(self.root, text="Raporu Göster", bg="#FF6347", fg="white", command=self.show_report).grid(row=self.rows+1, column=self.seats_per_row//2, columnspan=self.seats_per_row//2, pady=10)

    def book_seat(self, row, seat):
        if self.seating[row][seat] == 'Empty':
            customer_name = simpledialog.askstring("Rezervasyon", "Müşteri Adı:")
            if customer_name:
                price = simpledialog.askfloat("Rezervasyon", "Bilet Fiyatı Girin:")
                team = simpledialog.askstring("Rezervasyon", "Takım Seçin:")
                self.seating[row][seat] = 'Booked'
                self.buttons[row][seat].config(bg="red", text="Booked")
                self.cursor.execute("INSERT INTO bookings (row, seat, customer_name, price, team) VALUES (?, ?, ?, ?, ?)", (row, seat, customer_name, price, team))
                self.conn.commit()
                messagebox.showinfo("Başarılı", f"{customer_name} Koltuk {row+1}-{seat+1} için rezervasyon yapıldı.")
            else:
                messagebox.showerror("Hata", "Müşteri adı girilmelidir.")
        else:
            messagebox.showwarning("Uyarı", "Bu koltuk zaten rezerve edilmiştir.")

    def reset_all(self):
        for row in range(self.rows):
            for seat in range(self.seats_per_row):
                self.seating[row][seat] = 'Empty'
                self.buttons[row][seat].config(bg="lightgreen", text=f"{row+1}-{seat+1}")

    def show_report(self):
        self.cursor.execute("SELECT * FROM bookings")
        bookings = self.cursor.fetchall()
        report = "Rapor\n\n"
        for booking in bookings:
            report += f"ID: {booking[0]}, Row: {booking[1]}, Seat: {booking[2]}, Customer: {booking[3]}, Price: {booking[4]}, Team: {booking[5]}\n"
        messagebox.showinfo("Rezervasyon Raporu", report)


# Ana uygulama başlatma
if __name__ == "__main__":
    root = tk.Tk()
    stadium_name = "Sample Stadium"
    app = StadiumGUI(root, stadium_name)
    root.mainloop()
