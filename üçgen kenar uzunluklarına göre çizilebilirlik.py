#a,b,c kenar uzunlukları verilen bir üçgenin
#oluşturulup oluşturulamayacağını bulma

import math              #mutlak değer fonksiyonu fabs   ye ihtiyacımız var 

a=eval(input("a kenar uzunluğu?"))
b=eval(input("b kenar uzunluğu?"))
c=eval(input("c kenar uzunluğu?"))

if c>=(a+b)or c<=math.fabs(a-b):
    print(" bu kenarlardan bir üçgen çizilemez")
elif b>=(a+c) or b<=math.fabs(a-c):
    print("bu kenarlardan bir üçgen çizilemez")
elif a>=(b+c) or a<=math.fabs(b-c):
    print ("bu kenarlardan bir üçgen çizilemez")
else:
    print("bu kenarlardan bir üçgen çizilebilir")
    
