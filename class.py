
class BenimSinifim:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def kendiFunc(self):
        print("Merhaba ,benim, adim" + self.name)

    def __str__(self):
        return f"{self.name}({self.age})"
    

p1 = BenimSinifim("Berk",20)
p1.age = 15

print(p1)
print(p1.name)
print(p1.age)

del p1
del p1.age

print(p1.age)
p1.kendiFunc()

