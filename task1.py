
# a= open("baza.txt", "x")

number = int(input("(1) TXT Faylini sil (2) Melumat Elave et : "))

if number == 1:
    import os
    os.remove("baza.txt")
elif number == 2:
    b= open("baza.txt", "a")
    b.write(input("Melumat daxil edin: "))


