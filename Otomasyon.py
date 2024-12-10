import pyautogui
import time

# Ekran boyutlarını al
screen_width, screen_height = pyautogui.size()

# Fareyi ekranın ortasına taşı
pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=2)

# 2 saniye bekle
time.sleep(2)

# Fareyi sağa doğru hareket ettir
pyautogui.move(200, 0, duration=1)

# Sol tıklama yap
pyautogui.click()

# Klavye ile yazı yaz
pyautogui.typewrite('Merhaba, bu bir otomasyon örneğidir!', interval=0.1)

# 2 saniye bekle
time.sleep(2)

# ESC tuşuna bas
pyautogui.press('esc')

