import tkinter as tk
import time

class TrafficLight:
    def __init__(self, root):
        self.root = root
        self.root.title("Trafik Lambasi")
        
        # Trafik lambası çerçevesi
        self.canvas = tk.Canvas(root, width=100, height=260, bg="black")
        self.canvas.pack()

        # Kırmızı, sarı ve yeşil ışıklar
        self.red_light = self.canvas.create_oval(20, 20, 80, 80, fill="grey")
        self.yellow_light = self.canvas.create_oval(20, 100, 80, 160, fill="grey")
        self.green_light = self.canvas.create_oval(20, 180, 80, 240, fill="grey")

        # Işıkları döngüsel olarak değiştir
        self.current_light = "red"
        self.change_light()

    def change_light(self):
        # Tüm ışıkları kapat
        self.canvas.itemconfig(self.red_light, fill="grey")
        self.canvas.itemconfig(self.yellow_light, fill="grey")
        self.canvas.itemconfig(self.green_light, fill="grey")
        
        # Geçerli ışığı yak
        if self.current_light == "red":
            self.canvas.itemconfig(self.red_light, fill="red")
            self.current_light = "green"
            delay = 9000  # 9 saniye kırmızı ışık
        elif self.current_light == "green":
            self.canvas.itemconfig(self.green_light, fill="green")
            self.current_light = "yellow"
            delay = 9000  # 9 saniye yeşil ışık
        elif self.current_light == "yellow":
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
            self.current_light = "red"
            delay = 2000  # 2 saniye sarı ışık

        # Belirli bir süre sonra ışığı değiştir
        self.root.after(delay, self.change_light)

# Ana pencereyi oluştur ve trafik lambasını çalıştır
root = tk.Tk()
traffic_light = TrafficLight(root)
root.mainloop()
