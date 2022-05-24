# stack 방식 이용 계속 추가시키면서 0이 되게 만들어 카운트
# '(','{','[' -> +1 --- cnt += 1
# ')','}',']' -> -1 --- cnt += 1

def solution(string):

    answer = 0
    stack = []
    for char in string:
        if char in '({[':
            stack.append(char)
        else:
            if char == ')' and stack[-1]=='(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stacl[-1] == '(':
                stack.pop()
            else:
                stack.append(char)