# Enquanto Verdadeiro
while(True):
    # ler valores para L e R
    L, R = map(int, input().split())
    # Verificar se L e R são iguais a zero
    # (Condição de Parada)
    if(L == 0 and R == 0): break
    # Imprimir L + R
    print(L + R)


