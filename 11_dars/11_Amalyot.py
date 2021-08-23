# """
# 25/11/2020
# Dasturlash asoslari
# #11-dars: if-elif-else
# Muallif: Anvar Narzullaev
# Web sahifa: https://python.sariq.dev
# """

#Juft sonni aniqlash
# Foydalanuvchidan juft son kiritishni so'rang.
# Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas"
#  degan xabarni chiqaring.

# sonn = int(input("Istalgan sonni kiriting! >> "))
# print("Rahmat!\nSiz juft son kiritdingiz") if sonn%2 == 0 else print("Marhamat yana bir bor urunib ko'ring!")

#==================================================================================================================

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingizni kiriting! >> "))

# if yosh <= 4 or yosh > 60:
#     print("Xush kelibsiz marhamat sizga bepul!")
#     narx_chipta = 'Tekin'
# elif yosh <= 18:
#     narx_chipta = 10000
# else:
#     narx_chipta = 20000
# print(f"Sizga kirish uchun {narx_chipta} ")

#==================================================================================================================

# Foydalanuvchidan ikita son kiritishni so'rang,
# sonlarni solishtiring va ularning teng yoki 
# katta/kichikligi haqida xabarni chiqaring

# son1, son2 = int(input("Birinchi sonni kiriting! >> ")), int(input("Ikkinchi sonni kiriting! >> "))
# if son1 == son2:
#     print(f"Siz kiritgan {son1} qatiiyan {son2} ga teng!")
# elif son1 > son2:
#     print(f"Siz kiritgan {son1} katta {son2} dan!")
# elif son1 < son2:
#     print(f"Siz kiritgan {son1} kichik {son2} dan!")
#==================================================================================================================

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
# "Mahsulot do'konimizda bor" aks holda,
#  "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# mahsulotlar = ['banan', 'anor', 'olma', 'shovurma', 'non', 'salat', 'un', 'kalbasa', 'yorma', 'dulana']
# savat = []
# print("Savatga kamida 5 ta mahsulot kiriting!")
# mahsulot_kiritish = int(input("Necha xil mahsulot harid qilmoqchisiz!? >> "))
# i = 1
# if mahsulot_kiritish > 4:
#     for mahsulot in range(1, mahsulot_kiritish + 1):
#         savat.append(str(input(f"{mahsulot} - mahsulot kiriting! >> ").lower()))

#     for xarid in savat:
#         if xarid in mahsulotlar:
#             print(f"Bizda {xarid.title()} bor!")
#         else:
#             print(f"Bizda {xarid.title()} yo'q! ")
# else:
#     print(f"Siz kiritgan {mahsulot_kiritish} kichik 5 dan! \nQaytaddan kiriting!")

#==================================================================================================================

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, 
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas 
# ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa 
# "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['banan', 'anor', 'olma', 'shovurma', 'non', 'salat', 'un', 'kalbasa', 'yorma', 'dulana']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# print("Savatga kamida 5 ta mahsulot kiriting!")
# mahsulot_kiritish = int(input("Necha xil mahsulot harid qilmoqchisiz!? >> "))
# i = 1
# if mahsulot_kiritish > 4:
#     for mahsulot in range(1, mahsulot_kiritish + 1):
#         savat.append(str(input(f"{mahsulot} - mahsulot kiriting! >> ").lower()))

#     for xarid in savat:
#         if xarid in mahsulotlar:
#             #print(f"Bizda {xarid.title()} bor!")
#             bor_mahsulotlar.append(xarid)
#         else:
#             # print(f"Bizda {xarid.title()} yo'q! ")
#             mavjud_emas.append(xarid)
# else:
#     print(f"Siz kiritgan {mahsulot_kiritish} kichik 5 dan! \nQaytaddan kiriting!")

# if mavjud_emas == 0:
#     print("Xayr!!!")
# else:
#     print("Do'konimizda quyidagi mahsulot mavjud emas!")
#     for emas in mavjud_emas:
#         print(emas.title())
#==================================================================================================================

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
# aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ['salom', 'xayr', 'nima', 'qani', 'moni']
# yangi_login = str(input("Yangi login tanlang! >> ").lower())

# if yangi_login in foydalanuvchilar:
#     print("\n Login band, yangi login tanlang! \n")
# else:
#     print("\n Xush kelibsiz! \n Xurmatli Admin! \n")

#==================================================================================================================

# Foydalanuvchidan biror butun son kiritishni so'rang. 
# Foydalanuvchi kiritgan sonni 2 da 10 gacha 
# bo'lgan sonlardan qay biriga qoldiqsiz 
# bo'linishini konsolga chiqaring. 

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")