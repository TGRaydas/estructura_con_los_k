import numpy as np
x = 0
y = 0
num_value = 0 #Valor actual
global_counter = 0 #Mayor cantidad encontrada
number_global_counter = None #Numero del mayor encontrado
counter = 1 #Encontrados actualmente
actual_counter = 1 #Cantidad de casillas encontradas
n = int(input())
matrix = []
marked_for_visit = []
for i in range(n):
    row = []
    for z in range(n):
        row.append(np.random.randint(0, 2))
    matrix.append(row)
    print(row)
def search(x, y, n, counter, matrix, num_value, actual_counter):
    some = False
    if x + 1 < n: # Derecha
        if matrix[y][x + 1] == num_value:
            matrix[y][x + 1] = "x"
            counter += 1
            marked_for_visit.append([y, x + 1])
            some = True
            actual_counter += 1
    if x - 1 >= 0: # Izquierda
        if matrix[y][x - 1] == num_value:
            matrix[y][x - 1] = "x"
            counter += 1
            marked_for_visit.append([y, x - 1])
            some = True
            actual_counter += 1
    if y + 1 < n: # Abajo
        if matrix[y + 1][x] == num_value:
            matrix[y + 1][x] = "x"
            counter += 1
            marked_for_visit.append([y + 1, x])
            some = True
            actual_counter += 1
    if y - 1 >= 0:
        if matrix[y - 1][x] == num_value:
            matrix[y - 1][x] = "x"
            counter += 1
            marked_for_visit.append([y - 1, x])
            some = True
            actual_counter += 1
    return some, counter, actual_counter
num_value = matrix[y][x]
matrix[y][x] = "x"
while actual_counter < n*n:
    return_v, counter, actual_counter = search(x, y, n, counter, matrix, num_value, actual_counter)
    while return_v:
        return_v, counter, actual_counter = search(x, y, n, counter, matrix, num_value, actual_counter)
    if len(marked_for_visit) > 0:
        x = marked_for_visit[0][1]
        y = marked_for_visit[0][0]
        marked_for_visit.pop(0)
    else:
        if counter > global_counter:
            global_counter = counter
            number_global_counter = num_value
        for l in range(n):
            help = False
            for z in range(n):
                if (matrix[l][z] == 0 or matrix[l][z] == 1):
                    x = z
                    y = l
                    num_value = matrix[y][x]
                    matrix[y][x] = "x"
                    actual_counter += 1
                    counter = 1
                    help = True
                    break
            if help == True:
                break
print("Se repite " + str(global_counter) + " veces el numero " + str(number_global_counter))


