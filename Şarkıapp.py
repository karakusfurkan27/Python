import tkinter as tk
from tkinter import messagebox
import pygame

# Pygame'i başlatıyoruz
pygame.init()

# Şarkı dosyaları ve veriler
songs = {
    "Pop": [
        {"title": "Shape of You", "path": "pop_shape_of_you.mp3", "type": "pop", "favorite": False},
        {"title": "Blinding Lights", "path": "pop_blinding_lights.mp3", "type": "pop", "favorite": False}
    ],
    "Rock": [
        {"title": "Bohemian Rhapsody", "path": "rock_bohemian_rhapsody.mp3", "type": "rock", "favorite": False},
        {"title": "Stairway to Heaven", "path": "rock_stairway_to_heaven.mp3", "type": "rock", "favorite": False}
    ],
    "Türkçe": [
        {"title": "Fikrimin İnce Gülü", "path": "turkce_fikrimin_ince_gulu.mp3", "type": "turkce", "favorite": False},
        {"title": "Deli", "path": "turkce_deli.mp3", "type": "turkce", "favorite": False}
    ],
    "Türkçe Rap": [
        {"title": "Neyim Var Ki", "path": "turkce_rap_neyim_var_ki.mp3", "type": "turkce_rap", "favorite": False},
        {"title": "Yarim", "path": "turkce_rap_yarim.mp3", "type": "turkce_rap", "favorite": False}
    ],
    "Podcast": [
        {"title": "Teknoloji Sohbeti", "path": "podcast_teknoloji_sohbeti.mp3", "type": "podcast", "favorite": False},
        {"title": "Güncel Olaylar", "path": "podcast_guncel_olaylar.mp3", "type": "podcast", "favorite": False}
    ]
}

last_played = None  # Son çalınan şarkıyı tutacak
favorites = []  # Favori şarkıları tutacak

# Fonksiyonlar
def play_music(song_path):
    """Şarkıyı çalmaya başla"""
    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(loops=0, start=0.0)
    except Exception as e:
        messagebox.showerror("Hata", f"Şarkı çalınamadı! {e}")
        
    # En son çalınan şarkıyı güncelle
    global last_played
    last_played = song_path

def stop_music():
    """Şarkıyı durdur"""
    pygame.mixer.music.stop()

def pause_music():
    """Şarkıyı duraklat"""
    pygame.mixer.music.pause()

def unpause_music():
    """Şarkıyı devam ettir"""
    pygame.mixer.music.unpause()

def add_to_favorites(song_title):
    """Favorilere şarkı ekle"""
    for genre in songs.values():
        for song in genre:
            if song["title"] == song_title:
                song["favorite"] = True
                favorites.append(song)
                messagebox.showinfo("Favori", f"{song_title} favorilere eklendi.")

def show_last_played():
    """Son çalınan şarkıyı göster"""
    if last_played:
        messagebox.showinfo("Son Çalınan", f"Son çalınan şarkı: {last_played}")
    else:
        messagebox.showinfo("Son Çalınan", "Henüz hiçbir şarkı çalmadı.")

def show_favorites():
    """Favori şarkıları göster"""
    if favorites:
        fav_titles = [song["title"] for song in favorites]
        messagebox.showinfo("Favoriler", "\n".join(fav_titles))
    else:
        messagebox.showinfo("Favoriler", "Henüz favori şarkınız yok.")

# GUI penceresini oluştur
root = tk.Tk()
root.title("Şarkı Uygulaması")
root.geometry("400x400")  # Pencere boyutları

# Şarkı türleri
genre_listbox = tk.Listbox(root, height=6)
for genre in songs.keys():
    genre_listbox.insert(tk.END, genre)
genre_listbox.pack(pady=10)

def update_song_list(event):
    """Seçilen türe göre şarkıları listele"""
    selected_genre = genre_listbox.get(tk.ACTIVE)
    song_listbox.delete(0, tk.END)  # Eski şarkıları sil
    
    for song in songs[selected_genre]:
        song_listbox.insert(tk.END, song["title"])

# Şarkı listesi
song_listbox = tk.Listbox(root, height=6)
song_listbox.pack(pady=10)
genre_listbox.bind("<<ListboxSelect>>", update_song_list)

# Oynat Butonu
def play_selected_song():
    """Seçilen şarkıyı çal"""
    selected_song = song_listbox.get(tk.ACTIVE)
    for genre in songs.values():
        for song in genre:
            if song["title"] == selected_song:
                play_music(song["path"])

play_button = tk.Button(root, text="Oynat", width=15, command=play_selected_song)
play_button.pack(pady=5)

# Favorilere Ekle Butonu
def add_favorite():
    """Favoriye ekle"""
    selected_song = song_listbox.get(tk.ACTIVE)
    add_to_favorites(selected_song)

favorite_button = tk.Button(root, text="Favorilere Ekle", width=15, command=add_favorite)
favorite_button.pack(pady=5)

# Son Çalınanlar Butonu
last_played_button = tk.Button(root, text="Son Çalınan", width=15, command=show_last_played)
last_played_button.pack(pady=5)

# Favori Şarkılar Butonu
favorite_songs_button = tk.Button(root, text="Favoriler", width=15, command=show_favorites)
favorite_songs_button.pack(pady=5)

# Duraklat Butonu
pause_button = tk.Button(root, text="Duraklat", width=15, command=pause_music)
pause_button.pack(pady=5)

# Devam Et Butonu
unpause_button = tk.Button(root, text="Devam Et", width=15, command=unpause_music)
unpause_button.pack(pady=5)

# Durdur Butonu
stop_button = tk.Button(root, text="Durdur", width=15, command=stop_music)
stop_button.pack(pady=5)

# Uygulama başlatılıyor
root.mainloop()
