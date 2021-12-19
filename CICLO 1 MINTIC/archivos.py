archivo = open(r'C:\Users\nicol\PycharmProjects\MisionTic\Clases MinTic\archivo.txt', "a+", encoding="utf-8")
print(archivo.mode)
#archivo.write("Café\n")
#print(archivo.mode)

archivo.seek(0)
for i in archivo.readlines():
    print(i, end="")
