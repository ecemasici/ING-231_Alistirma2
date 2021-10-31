

import random

#10-98 arasında bir sayı üretir.(integer)
sayı=random.randint(10,98)

#oyunun doğru çalışması için program basamakları farklı bir sayı tutmalı
if str(sayı)[0]==str(sayı)[1]:
   sayı=random.randint(10,98)

while True:

    doğruyersayacı=0
    yanlışyersayacı=0
    
    #oyuncudan bir sayı girmesi istenir(str)
    tahmin=input("Lütfen bir sayı giriniz:")

    #oyuncu 10'dan küçük,98'den büyük ve basamakları aynı olan bir tahminde bulunursa uyarı alır ve başa dönsün
    if int(tahmin)<10 or int(tahmin)>98 or tahmin[0]==tahmin[1]:
        print("Lütfen 10 ile 98 arasında basamakları aynı olmayan bir sayı giriniz!")

    elif (tahmin[0] in str(sayı)) or (tahmin[1] in str(sayı)):

        if tahmin[0]==str(sayı)[0] and tahmin[1]==str(sayı)[1]:
            doğruyersayacı+=2
            print("Sayıyı doğru tahmin ettiniz!")
            
        elif tahmin[0]==str(sayı)[0] and tahmin[1]!=str(sayı)[1]:
            doğruyersayacı+=1
            yanlışyersayacı-=1

        else: 
            doğruyersayacı+=1
            yanlışyersayacı-=1
                        
    else:
            yanlışyersayacı-=2
                    
    print("doğruyersayacı=",doğruyersayacı,"yanlışyersayacı=",yanlışyersayacı)
            
        
            

