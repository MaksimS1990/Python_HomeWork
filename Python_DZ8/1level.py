n = '22 + 300'
m = n.split()
print(m)

a = int(m[0])
c = m[1]
b = int(m[2])


def calc (a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

print(a, b, c)

print(calc(a, b, c))
