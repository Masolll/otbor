def prost(n):           #Функция которая проверяет числа на простоту
    d=2
    while d*d<=n:       #делители перебираем до корня из числа n
        if n%d==0:      #если число делится значит оно не простое
            return False#в таком случае возвращаем ложь
        d+=1
    return True         #если по итогу работы всего цикла
                        #функция не вернула ложь значит число простое
                        #возвращаем истину
k=0
for p in range(2,46+1):
    if prost(p):
        k+=1
print(k)
    
