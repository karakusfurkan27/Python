class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def display_balance(self):
        print(f"Mevcut Bakiye: {self.balance} TL")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL yatırıldı.")
        else:
            print("Geçersiz miktar.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL çekildi.")
        elif amount > self.balance:
            print("Yetersiz bakiye.")
        else:
            print("Geçersiz miktar.")

def atm_menu():
    atm = ATM()

    while True:
        print("\nATM İşlemleri:")
        print("1. Bakiye Görüntüle")
        print("2. Para Yatir")
        print("3. Para Çek")
        print("4. Çikiş")
        
        choice = input("Seçiminiz (1/2/3/4): ")

        if choice == '1':
            atm.display_balance()
        elif choice == '2':
            amount = float(input("Yatirmak istediğiniz miktar: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Çekmek istediğiniz miktar: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Çikiş yapiliyor.")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# ATM uygulamasını çalıştırmak için menüyü çağırıyoruz
atm_menu()
