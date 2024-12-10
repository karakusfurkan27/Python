def start_game():
    print("Hoş geldiniz! Büyük maceraya hazır mısınız?")
    print("Bir ormanda kayboldunuz ve çıkış yolunu bulmalısınız.")
    first_choice()

def first_choice():
    print("\nİleride iki yol var: Sol ve Sağ. Hangi yoldan gitmek istersiniz?")
    choice = input("Sol (S) / Sağ (Sağ): ").lower()

    if choice == 's':
        left_path()
    elif choice == 'sağ':
        right_path()
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
        first_choice()

def left_path():
    print("\nSol yoldan ilerliyorsunuz ve bir nehirle karşılaşıyorsunuz.")
    print("Nehri geçmek için bir köprü var. Ne yapacaksınız?")
    choice = input("Köprüyü Geç (K) / Geri Dön (G): ").lower()

    if choice == 'k':
        cross_bridge()
    elif choice == 'g':
        first_choice()
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
        left_path()

def right_path():
    print("\nSağ yoldan ilerliyorsunuz ve bir mağara buluyorsunuz.")
    print("Mağaraya girmeli misiniz?")
    choice = input("Giriş (G) / Geri Dön (G): ").lower()

    if choice == 'g':
        enter_cave()
    elif choice == 'g':
        first_choice()
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
        right_path()

def cross_bridge():
    print("\nKöprüyü geçiyorsunuz ve güvenli bir yere ulaşıyorsunuz. Tebrikler! Oyunu kazandınız.")

def enter_cave():
    print("\nMağaraya giriyorsunuz ve bir hazine buluyorsunuz. Tebrikler! Oyunu kazandınız.")

start_game()
