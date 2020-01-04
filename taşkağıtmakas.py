import sys

user1 = input("1. Oyuncu İsmin Ne:")
user2 = input("2. Oyuncu İsmin Ne:")
print("1:Taş")
print("2:Kağıt")
print("3:Makas")

cevap1 = int(input("1. Oyuncu Seçimini yap!:"))
cevap2 = int(input("2. Oyuncu Seçimini Yap!:"))

def compare(cevap1,cevap2):
  if cevap1 == cevap2:
    return("Berabere")
  elif cevap1 == 1:
    if cevap2 == 2:
      return("İkinci Oyuncu Kazandı!")
    else:
      return("Birinci Oyuncu Kazandı!")
  elif cevap1 == 2:
    if cevap2 == 1:
      return("Birinci Oyuncu Kazandı!")
    else:
      return("İkinci Oyuncu Kazandı!")
  elif cevap1 == 3:
    if cevap2 == 1:
      return("İkinci Oyuncu Kazandı!")
    else:
      return("Birinci Oyuncu Kazandı!")
  else:
    return("Yanlış bir değer girdiniz! Programı yeniden başlatmalısınız!")


print(compare(cevap1,cevap2))
  