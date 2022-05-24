N = int(input())
a5 = 0
while N >= 0:
    if N % 5 == 0:
        a5 += N/5
        print(int(a5))
        break
    N -= 3
    a5 += 1
else :
    print(-1)