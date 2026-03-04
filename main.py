# 20
def qabul(ism):
    if ism.lower():
        return "Ism notogri qilingan"

    return "To‘g‘ri yozilgan"

text = "regwerUYGEYDG"
res = qabul('Ali')
print(res)

# 21
def baho(bal):
    if 90 <= bal <= 100:
        return "a"
    elif 70 <= bal < 89:
        return "b"
    elif 50 <= bal < 69:
        return "c"
    else:
        return "Yiqildi"


bal = int(input("Balni kiriting: "))
print("sizning bahoingz:", baho(bal))

# 22
def fasl(oy):
    if oy in [12, 1, 2]:
        return "Qish"
    else:
        return "Qish emas"


oy = int(input("Oy raqamini kiriting :"))


print("Natija:", fasl(oy))

# 23
def solishtir(son1, son2):
    if son1 > son2:
        return "1-son katta"
    else:
        return "2-son katta yoki teng"

son1 = float(input("1-sonni kiriting: "))
son2 = float(input("2-sonni kiriting: "))


print(solishtir(son1, son2))


# 24
def palindrom_tekshir(matn):

    matn_tozalangan = matn.replace(" ", "").lower()

    if matn_tozalangan == matn_tozalangan[::-1]:
        return "Palindrom"
    else:
        return "Palindrom emas"


matn = input("Matn kiriting: ")


print(palindrom_tekshir(matn))
