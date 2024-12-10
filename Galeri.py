import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Resim Galerisi")
        
        # Resim listesi ve indeks
        self.image_list = []
        self.image_index = 0

        # GUI Elemanları
        self.image_label = Label(self.root)
        self.image_label.pack()

        self.prev_button = Button(self.root, text="Önceki", command=self.show_previous_image)
        self.prev_button.pack(side="left", padx=10)

        self.next_button = Button(self.root, text="Sonraki", command=self.show_next_image)
        self.next_button.pack(side="right", padx=10)

        self.load_button = Button(self.root, text="Klasör Seç", command=self.load_images)
        self.load_button.pack(side="bottom", pady=10)

    def load_images(self):
        # Klasör seç ve resimleri yükle
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.image_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                               if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            if self.image_list:
                self.image_index = 0
                self.show_image()
            else:
                self.image_label.config(text="Klasörde görüntü bulunamadı.")

    def show_image(self):
        if self.image_list:
            image_path = self.image_list[self.image_index]
            img = Image.open(image_path)
            img = img.resize((600, 400), Image.ANTIALIAS)  # Resmi yeniden boyutlandır
            photo = ImageTk.PhotoImage(img)

            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            self.image_label.config(text="Resim yüklenemedi.")

    def show_next_image(self):
        if self.image_list:
            self.image_index = (self.image_index + 1) % len(self.image_list)
            self.show_image()

    def show_previous_image(self):
        if self.image_list:
            self.image_index = (self.image_index - 1) % len(self.image_list)
            self.show_image()

# Uygulamayı başlat
if __name__ == "__main__":
    root = Tk()
    gallery = ImageGallery(root)
    root.mainloop()
