import random
l="abcdefghijklmnopqrstuvwxyz"
u=str.upper(l)
n="0123456789"
s="{}!@#$%^&*-+"
total=l+u+n+s
for i in range (5): 
    l=int(input("Enter length of password: "))
    pas="".join(random.sample(total,l))
    print(pas)
