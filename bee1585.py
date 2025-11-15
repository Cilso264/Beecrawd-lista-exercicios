def areaLosango(D, d):
    return(D*d)/ 2


a1 = areaLosango(7, 3)
a2 = areaLosango(6, 4)
a3 = areaLosango(3, 7)

print(a1, a2, a3)
def areaLosango(D,d):
    return D*d/2
    
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    area = int(areaLosango(x, y))
    
    print(f"{area} cm2")
    