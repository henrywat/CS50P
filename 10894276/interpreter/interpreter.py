expression = input("Expression: ")
x, y, z = expression.split()
x = int(x)
z = int(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z

formatted_result = "{:.1f}".format(result)
print(formatted_result)
