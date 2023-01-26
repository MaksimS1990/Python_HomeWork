n = ' 22 * 300 - 14 + 10 * 10 '

m = n.split()

print(m)

def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b
    
stack = []
numbers = []
for i in range(0, len(m)):
    if m[i] == '/' or m[i] == '*' or m[i] == '+' or m[i] == '-':
        stack.append(m[i])
        while(stack == ["'/', '+'"] or stack == ["'/', '-'"] or stack == ["'*', '+'"] or stack == ["'*', '-'"]):
            temp = stack.pop()
            numbers.append(temp)    
    else: 
        numbers.append(m[i])
print(numbers, stack)



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
