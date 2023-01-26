n = '22 * 300 - 14 + 10 * 10'

m = n.split()


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b
    
    
stack = [' ']
numbers = []
for i in range(0, len(m)):
    
    if m[i] == '/' or m[i] == '*':
        if stack[-1] == '*' or stack[-1] == '/':
            numbers.append(stack[-1])
            stack.pop()
        stack.append(m[i]) 

    elif m[i] == '+' or m[i] == '-':
        while stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "+" or stack[-1] == "-":
            numbers.append(stack[-1])
            stack.pop()
        stack.append(m[i])    
    else: 
        numbers.append(m[i])
print(numbers, stack)

stack.reverse()
stack.pop()

numbers += stack
print(numbers)


# while(stack == ["'/', '+'"] or stack == ["'/', '-'"] or stack == ["'*', '+'"] or stack == ["'*', '-'"]):

#     while numbers[i] == '*' or numbers[i] == '/' and numbers[i] == '+' or numbers[i] == '-':
    #         numbers.append(n[i])
    #         numbers.pop()
    #     stack.append(stack[i])



# a = int(m[0])
# c = m[1]
# b = int(m[2])

# result = int(m[0])

# for i in range(1, len(m) - 1, 2):
#     if m[i] == '*' or m[i] == '/':
#         result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
#         m2.append(result)
#     else:
#         m2.append(m[i])
#         m2.append(int(m[i + 1]))


# print(m[i], m[i + 1])
# print(m2)
# print(result)
