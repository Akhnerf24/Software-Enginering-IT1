# variable

# integer
a = 1
b = 2
b = b + a

# string
animal = "Gajah"

# boolean
c = True
d = False

# float
e = 3.0

# List/Array
f = []

# Dictionary
g = {}

# Tuple
h = ()

# Print
print("Singa")
print(2 + 3)
print(True)
print(b)
print("Nama Hewannya adalah : " + animal)

# ini menggunakan dictionary 
print("Nama Hewannya adalah :{}".format(animal))
# contatenate int ke string
print("Ini nilai a dari int ke str :" + str(a))
print("Ini tidak perlu di convert : {}".format(a))
print("Nama : {}, \nTempat Tinggal : {}, \nUmur :{}".format("Akhner", "Palembang", "19"))

# contoh Array
NamaOrang = ["David", "David2", "David3"]
print(NamaOrang)
print(NamaOrang[0])
List_1 = ["David"] * 4
print(List_1)
print(NamaOrang[0:2]) #ini sebut array 0 dan 1
print(NamaOrang[-1]) #ini panggil 1 dari yang belakang
print(NamaOrang[-2:])#ini 2 terakhir

#nambahkan ke array pake append
NamaOrang.append("hai")
print(NamaOrang)
