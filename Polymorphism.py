class Poligon:
    def render(self):
        print("Poligon İşleniyor")

class Kare(Poligon):
    def render(self):
        print("Kare işleniyor")

class Yuvarlak(Poligon):
    def render(self):
        print("Yuvarlak işleniyor")

x = Yuvarlak()
x.render()

y = Kare()
y.render()

