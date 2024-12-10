import tkinter as tk
from tkinter import messagebox  # messagebox import edilmediği için hata alıyorduk

# İçerik ve fiyatlar
beverages = {
    "Kahve": 5.0,
    "Çay": 3.0,
    "Ayran": 4.0,
    "Kola": 6.0,
    "Su": 2.0
}

# Otomat sınıfı
class BeverageVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("İçecek Otomatı")
        self.total = 0.0

        # Etiket
        self.label = tk.Label(root, text="İçecek Seçin", font=("Arial", 20))
        self.label.pack(pady=10)

        # İçecekler için butonlar
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.buttons = {}
        for beverage, price in beverages.items():
            self.buttons[beverage] = tk.Button(self.buttons_frame, text=f"{beverage} - {price} TL", font=("Arial", 14),
                                              command=lambda b=beverage: self.select_beverage(b))
            self.buttons[beverage].pack(side=tk.LEFT, padx=10)

        # Toplam fiyat etiketi
        self.total_label = tk.Label(root, text="Toplam: 0.0 TL", font=("Arial", 16))
        self.total_label.pack(pady=20)

        # Satın Al butonu
        self.purchase_button = tk.Button(root, text="Satın Al", font=("Arial", 14), command=self.purchase)
        self.purchase_button.pack(pady=10)

    def select_beverage(self, beverage):
        """İçecek seçildiğinde toplam fiyatı günceller"""
        self.total += beverages[beverage]
        self.total_label.config(text=f"Toplam: {self.total} TL")

    def purchase(self):
        """Satın alma işlemi ve uyarı"""
        if self.total > 0:
            messagebox.showinfo("Satın Alma", f"İçeriklerinizi satın aldınız. Toplam: {self.total} TL")
            self.total = 0  # Satın alma işleminden sonra sıfırlama
            self.total_label.config(text="Toplam: 0.0 TL")
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir içecek seçin!")

# Ana pencereyi oluştur
root = tk.Tk()

# Otomattan bir nesne oluştur
vending_machine = BeverageVendingMachine(root)

# Uygulamayı başlat
root.mainloop()
