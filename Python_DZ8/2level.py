n = '22 + 300 - 14 + 10 + 10'
m = n.split()
print(m)
def calc (a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b


a = int(m[0])
c = m[1]
b = int(m[2])

result = calc(a, b, c)

for i in range(3, len(m) - 1, 2):
    result = calc(result, int(m[i + 1]), m[i])
    print(m[i], m[i + 1])
    print(result)
