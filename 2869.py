# cnt = 0
# A,B,V = map(int,input().split())
# while V >= 0:
#     cnt += 1
#     V -= A
#     if V <= 0:
#         print(cnt)
#         break
#     V += B

A,B,V = map(int,input().split())
day = (V - B)/(A - B)
print(int(day))