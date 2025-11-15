ENERGIA = 18

MOVS = [(0, -1), (1, 0), (-1, 0), (0, 1)]

lab = [
    [1, 1, 1, 1, 99, 1, 1, 1, 'I'],
    [1, 99, 99, 1, 1, 1, 99, 1, 99],
    [1, 1, 99, 1, 1, 99, 1, 1, 1],
    [99, 1, 99, 99, 99, 99, 99, 99, 99],
    [1, 1, 1, -1, 1, 1, 1, 3, 99],
    [-2, 99, 99, 99, 99, 99, 1, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 1, 99],
    [1, 99, 99, 99, 99, 99, 99, 1, 1],
    ['F', 1, 1, 3, 1, 1, 99, 1, 1]
]

sol = [[0]*9 for _ in range(9)]
pasos = 0

def buscar(letra):
    for f in range(9):
        for c in range(9):
            if lab[f][c] == letra:
                return f, c

def valido(f, c):
    return 0 <= f < 9 and 0 <= c < 9 and lab[f][c] != 99

def energia_de(f, c):
    if lab[f][c] == 'I' or lab[f][c] == 'F':
        return 0
    return lab[f][c]   # POSITIVOS RESTAN, NEGATIVOS SUMAN

def resolver(f, c, energia):
    global pasos

    if lab[f][c] == 'F':
        sol[f][c] = 1
        pasos += 1
        return True

    sol[f][c] = 1
    pasos += 1

    for df, dc in MOVS:
        nf, nc = f + df, c + dc

        if valido(nf, nc) and sol[nf][nc] == 0:
            nueva = energia - energia_de(nf, nc)
            if nueva >= 0:
                if resolver(nf, nc, nueva):
                    return True

    sol[f][c] = 0
    pasos -= 1
    return False

inicio = buscar('I')

if resolver(inicio[0], inicio[1], ENERGIA):
    print("¡Salida encontrada!")
else:
    print("No hay camino posible.")

print("\nMatriz solución:")
for fila in sol:
    print(fila)

print("\nPasos utilizados:", pasos)