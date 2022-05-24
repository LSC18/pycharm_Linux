a = 0
s = input()
for i in range(len(s)):
    if s[i] == '(':
        a += 1
    elif s[i] == ')' and a>0:
        a -= 1
    elif s[i] == ')' and s[i] == 0:
        a = 1
        break
if a == 0:
    print('YES')
else:
    print('NO')