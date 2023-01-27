n = input('Введите выражение, которое нужно посчитать: ')

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
# print(numbers, stack)

stack.reverse()
stack.pop()

numbers += stack
# print(numbers)

result = []

for i in range(len(numbers)):
    if numbers[i] in '*':
        q = float(result.pop())
        z = float(result.pop())
        result.append(q * z)
    elif numbers[i] in '/':
        q = float(result.pop())
        z = float(result.pop())
        result.append(z / q)
    elif numbers[i] in '+':
        q = float(result.pop())
        z = float(result.pop())
        result.append(q + z)
    elif numbers[i] in '-':
        q = float(result.pop())
        z = float(result.pop())
        result.append((z - q))
    else:
        result.append(numbers[i])

print(result)