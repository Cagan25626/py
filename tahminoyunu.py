import random
print("----Tahmin Oyunu----")
secretNum = random.randint(1,9)
guessCount = 0
guess = 0
while guess != secretNum and guess != "exit":
  guess = input("Tahminini gir(1 ve 9 arasında):")

  if guess == "exit":
    break
  
  guess = int(guess)
  guessCount = guessCount + 1

  if guess < secretNum:
    print("Tahminin biraz az!")
  elif guess > secretNum:
    print("Tahminin biraz fazla!")
  else:
    print("Tahminin Doğru!")
    print("Deneme Sayın:"+ str(guessCount))