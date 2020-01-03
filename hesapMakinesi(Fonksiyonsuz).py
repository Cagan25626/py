print("----Hesap Makinesi----")
print("İşlemler:")
print("1: Toplama")
print("2: Çıkarma")
print("3: Çarpma")
print("4: Bölme")
islem = int(input("Seçtiğiniz İşlemin Kodunu Giriniz:"))
num1 = int(input("İlk Sayıyı Giriniz:"))
num2 = int(input("İkinci Sayıyı Giriniz:"))

if islem == 1:
  print(num1 + num2)
elif islem == 2:
  print(num1 - num2)
elif islem == 3:
  print(num1 * num2)
elif islem == 4:
  print(num1 / num2)
else:
  print("Yanlış bir işlem kodu girdiniz! Lütfen programı yeniden başlatın!")