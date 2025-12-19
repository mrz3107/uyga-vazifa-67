#1.Dictionary yaratish va unga 5 ta element qo‘shish.
#2.Foydalanuvchidan kalit kiritishini so‘rab, shu kalitga tegishli qiymatni ekranga chiqarish (get()).
#3.Dictionary dan kalit bo‘yicha elementni o‘chirish (pop()).
#4.Dictionary ning barcha kalit va qiymatlarini alohida chiqarish (keys(), values()).
#5.Dictionary ustida for sikli yordamida barcha elementlarni ekranga chiqarish.

Dic = {'Ali': "13 Yosh", "Alex": "15 yosh", 'Asil': "20 Yosh", "Alinur": "16 yosh", "Axmadjon": "19 yosh",}
print (Dic)

data = {
    "ism": "Ali",
    "yosh": 18,
    "shahar": "Toshkent"
}

kalit = input("O‘chiriladigan kalitni kiriting: ")

qiymat = data.pop(kalit, "Bunday kalit mavjud emas")

print("O‘chirilgan qiymat:", qiymat)
print("Yangilangan dictionary:", data)

data = {

    "ism": "Ali",
    "yosh": 18,
    "shahar": "Toshkent"
}

print("Kalitlar:")
for k in data.keys():
    print(k)

print("\nQiymatlar:")
for v in data.values():
    print(v)


data = {
    "ism": "Ali",
    "yosh": 18,
    "shahar": "Toshkent"
}

for kalit, qiymat in data.items():
    print(kalit, ":", qiymat)
