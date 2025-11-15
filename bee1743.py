def compativel(plugue, tomada):
    # implementar solução aqui
    for i in range(5):
        if plugue[i] == tomada [i]:
          return False
        
    return True

# Leitura e Tratamento dos dados
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
# Exibição do resultado
print('Y' if compativel(l1, l2) else 'N')

