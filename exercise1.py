a = int(input("Введите первое число = "))
b = int(input("Введите второе число = "))
c = int(input("Введите третье число = "))
d = 5
if (a==b) or (a==c) or (c==b):
        print('no')
elif (a and b<d) or (a and c<d) or (b and c<d):
        print('yes')



