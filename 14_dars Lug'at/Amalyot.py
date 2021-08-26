# MyFamily_name = {
#     'Otam' : 'Otaming ismi Ikramov Botir',
#     'Onam' : 'Onamning ismi Daminova Moxidil', 
#     'Ukam' : 'Ukamning ismi Abduvaitov Bunyodxon', 
#     'Singlim' : 'Singlimning ismi Abduvaitova Yulduzxon'
#     }
# MyFamily_year = {
#     'Otam' : '1973 - yilda, Samarqand viloyatida',
#     'Onam' : '1975 - yilda, Samarqand viloyatida ', 
#     'U
#     kam' : '2006 - yilda, Samarqand viloyatida ', 
#     'Singlim' : '2001 - yilda, Samarqand viloyatida '
# }
# print(f"{MyFamily_name['Otam']} {MyFamily_year['Otam']} tug'ilgan!")
# print(f"{MyFamily_name['Onam']} {MyFamily_year['Onam']} tug'ilgan!")
# print(f"{MyFamily_name['Ukam']} {MyFamily_year['Ukam']} tug'ilgan!")
# print(f"{MyFamily_name['Singlim']} {MyFamily_year['Singlim']} tug'ilgan!")
#==============================================================================

royxat = {
    'integer':'Butun son',
    'float':"O'nlik son",
    'string':'Matn',
    'list':"Ro'yxat",
    'tuple':"O'zgarmas son"}

#print(royxat)

# kalit_soz = str(input("Kalit so'zni kiriting: >> ").lower())
# print(royxat.get(kalit_soz, "Bunday kalit so'z mavjud emas!"))

# # kalit_soz = str(input("Kalit so'zni kiritig! >> ").lower())
# # tarjima = royxat.get(kalit_soz)

# # if tarjima == None:
# #     print("Bunday so'z mavjud emas!")
# # else:
# #     print(f"{kalit_soz.title()} so'zi {tarjima} deb tarjima qilinadi!")

# kalit_soz = input("Kalit so'zni kiriting! >> ").lower()
# print(kalit_soz.get(kalit_soz, "Bunday lug'at mavjud emas!"))

# kalit_soz = input("Kalit so'zni kiriting!")
# tarjima = royxat.get(kalit_soz)

# if tarjima == None:
#     print("Bunday kalit so'z mavjud emas!")
# else:
#     print(f"{kalit_soz.title()} so'z {tarjima} deb tarjima qilinadi!")

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    