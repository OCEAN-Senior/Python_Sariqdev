# # 11 - dars
# a = int(input("Sonni kiriting >> ")) 
# print("Son 0 dan katta! ") if a > 0 else print("Son 0 dan kichik!")
#======================================================================
# narx = 20000
# salat = True
# choy = False

# if choy and salat:
#     narx += 10000
# elif choy or salat:
#     narx += 5000

# print(f"Siz bizga {narx} so'm to'lashingiz lozim!")
#=======================================================================
# narx = 15000
# choy = 1
# salat = 0
# non = 1
# kampot = 1
# assarti = 0
# if choy:
#     print("Mijoz choy oldi")
#     narx += 5000

# if salat:
#     print("Mijoz salat oldi")
#     narx += 5000

# if non:
#     print("Mijoz non oldi")
#     narx += 2000

# if kampot:
#     print("Mijoz kampot oldi")
#     narx += 5000

# if assarti:
#     print("Mijoz assarti oldi")
#     narx += 5000

# print(f"Sizdan {narx} so'm bo'ldi!\nYana keling kutamiz!")
#======================================================================
menyu = ['osh', 'norin', 'manti', 'kabob']
qabul = input("Qanday taom xohlaysiz!? >> ")
if qabul.lower() in menyu:
    print("Buyurtma qabul qilindi! ")
else:
    print("Bizda bunday taom yo'q!")