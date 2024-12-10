f=open("python.txt")
print(f.read())

f.seek(0)
f.seek(10)

print(f.read())
print(f.tell())

with open("python.txt","r") as d:
    print(d.read())