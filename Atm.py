class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.balance} TL")
        else:
            print("Geçersiz miktar. Lütfen pozitif bir değer girin.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL çekildi. Yeni bakiye: {self.balance} TL")
        else:
            print("Geçersiz işlem. Yetersiz bakiye veya geçersiz miktar.")

    def check_balance(self):
        print(f"Mevcut bakiye: {self.balance} TL")


def atm_menu():
    print("\n*** Bankamatik ***")
    print("1. Bakiye Kontrolü")
    print("2. Para Yatirma")
    print("3. Para Çekme")
    print("4. Çikiş")
    print("******************")


def atm():
    account = BankAccount("Kullanici")

    while True:
        atm_menu()
        choice = input("Seçiminizi yapin: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Yatirilacak miktar: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Çekilecek miktar: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Çikiş yapiliyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    atm()
