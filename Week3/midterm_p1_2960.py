N, K = map(int, input().split())


if N <= K or N == 1:
    print("except")
else:
    
    range1 = list(range(2, N+1))

    count = []
    for i in range(2, N+1):
        
        for j in range(1, int(N/i)+1):
            
            if i*j in range1:
                range1.remove(i*j)
                count.append(i*j)
    print(count[K-1])
