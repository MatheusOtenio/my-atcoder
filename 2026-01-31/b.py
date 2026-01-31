N, K = map(int, input().split())

total_feijoes = 0
anos_passados = 0

while True:
    total_feijoes += (N + anos_passados)
    
    if total_feijoes >= K:
        print(anos_passados)
        break
        
    anos_passados += 1