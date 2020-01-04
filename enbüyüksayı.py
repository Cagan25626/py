print("----En Büyük Sayı Hangisi?----")
num1 = int(input("İlk Sayıyı Giriniz:"))
num2 = int(input("İkinci Sayıyı Giriniz:"))
num3 = int(input("Üçüncü Sayıyı Giriniz:"))

if num1 >= num2 and num1 >= num3:
  print("En Büyük Sayı:"+ str(num1) )
elif num2 >= num1 and num2 >= num3:
  print("En Büyük Sayı:"+ str(num2) )
else:
  print("En Büyük Sayı:"+ str(num3))
