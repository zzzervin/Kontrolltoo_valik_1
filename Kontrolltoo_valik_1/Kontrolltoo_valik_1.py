#n=""
#while type(n)!=int:
#    try:
#       n=int(input("Сколко елок будете брать  "))
#        if n>0 and n<10:
#            
#            for A in range (0,n):
#                              A1=("   /V\    ")
#                              print(end=A1)
#            print()
#            for A in range (0,n):
#                              A2=("  / V \   ")                  
#                              print(end=A2)
#            print()
#            for A in range (0,n):
#                              A3=(" / V V \  ")
#                              print(end=A3)
#            print()
#            for A in range (0,n):
#                              A4=("/VV V VV\ ")
#                              print(end=A4)
#            print()
#            print()
#        else:
#            print("Столько елок не продоем")
#    except:
#           TypeError

####3 Дано N чисел. Найти количество положительных чисел среди них; N рандомное число

#from random import *
#p=0
#a=randint(1,11)
#for i in range (0,a):
#    N=randint(-100,100)
#    print(N)
#    if N>0:
#        p+=1
#print("положительных: ",p)


####4 Посчитать четные и нечетные цифры введенного натурального числа.
#### Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

#n = int(input("введи чесло"))
#pos=nig=0
#while n>0:
#    if n%2 == 0:
#        pos += 1
#    else:
#        nig += 1
#    n = n//10
#print("четных: ",int(pos)) 
#print("нечетных : ",int(nig)) 

#####5 Найти сумму ряда чисел от A до B. Полученный результат вывести на экран;
C=
A=int(input("введи чесло A:"))
B=int(input("введи чесло B:"))
for i in range (A,B):
    C=A+B

    print(i)
print(C)