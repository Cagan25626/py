print("----Hangi Yıl 100 Yaşında Olacaksın----")
print("Öğrenmek İster Misin?")
print("1: Evet")
print("2: Hayır")
cevap = int(input("Cevabın:"))
if cevap == 2:
  print("Sen Bilirsin")
elif cevap == 1:
  name = input("İlk önce adını öğrenelim:")
  age = int(input("Yaşını öğrenelim:"))
  year = int(input("Son olarak şuan hangi yıldayız:"))
  value = 100 - age
  sonuc = year + value
  print(name +" "+ str(sonuc) +" yılında 100 yaşında olacaksın!" )
  print("Hangisini istersin?")
  print("1: Sonucu istediğim kadar yazdır")
  print("2 : Tekrar Dene")
  print("3:Programı bitir")
  cevap2 = int(input("Cevabın:"))
  if cevap2 == 1:
    sayi = int(input("Sonucu kaç kere yazdıralım?"))
    for i in range (1,sayi + 1):
      print(name +" "+ str(sonuc) +" yılında 100 yaşında olacaksın!" )
  elif cevap2 == 2:
    name = input("İlk önce adını öğrenelim:")
    age = int(input("Yaşını öğrenelim:"))
    year = int(input("Son olarak şuan hangi yıldayız:"))
    value = 100 - age
    sonuc = year + value
    print(name +" "+ str(sonuc) +" yılında 100 yaşında olacaksın!" )
  elif cevap2 == 3:
    print("Program kapatılıyor")
  
