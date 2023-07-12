import random




soru = input('Şifren Kaç karakterli olsun?')


sifresembol =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

soru =  int(soru)

sifre = '' 

for i in range(soru):
    sifre += random.choice(sifresembol)
    

print(sifre)
