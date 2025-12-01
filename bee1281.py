N  = int(input())

for _ in range(N):
    M = int(input())
    feira = {}
    
    preços = {}
    for _ in range(M):
        feira[nome] = float(preços)
        
        nome, valor = input().split()
        preços[nome] = float(valor)
        
        P = int(input())
        total = 0.0
        for _ in range(P):
            nome, qtd = input().split
            qtd = int(qtd)
            total += preços[nome] * qtd
            
            print(f"R$ {total:.2f}")
    