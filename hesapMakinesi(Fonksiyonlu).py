def toplama(num1,num2):
  return num1 + num2
def cikarma(num1,num2):
  return num1 - num2
def carpma(num1,num2):
  return num1 * num2
def bolme(num1,num2):
  return num1 / num2

print("----Hesap Makinesi----")
print("İşlemler:")
print("1: Toplama")
print("2 : Çıkarma")
print("3: Çarpma")
print("4: Bölme")

islem = int(input("Sectiğiniz İşlemin Kodunu Giriniz:"))
num1 = int(input("İlk Sayıyı Giriniz:"))
num2 = int(input("İkinci Sayıyı Giriniz:"))

if islem == 1:
  sonuc = toplama(num1,num2)
  print(sonuc)
elif islem == 2:
  sonuc = cikarma(num1,num2)
  print(sonuc)
elif islem == 3:
  sonuc = carpma(num1,num2)
  print(sonuc)
elif islem == 4:
  sonuc = bolme(num1,num2)
  print(sonuc)
else:
  print("Girdiğiniz İşlem Kodu Yanlış!Programı Tekrar Başlatmalıyız")