print("---Faktoriyel Hesaplama---")
num = int(input("Hangi Sayını Faktoriyeli Hesaplansın:"))

faktoriyel = 1

if num == 0:
  print("Sonuç: 1")
elif num < 0:
  print("Negatif Sayıların Faktoriyeli Hesaplanmaz")
else:
  for i in range (1,num + 1):
    faktoriyel = faktoriyel * i
  print("Sonuç:"+ str(faktoriyel))