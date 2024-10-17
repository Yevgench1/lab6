import math

def f(x):
    if x != 0:
        return (x**3 + 1) / (3 * x) + abs(x) / (3 * x)
    else:
        return float('inf')  

def tabulate_with_for(a, b, h):
    result = []
    for x in range(int(a / h), int(b / h) + 1):
        x_value = x * h
        result.append((x_value, f(x_value)))
    return result

def tabulate_with_while(a, b, h):
    result = []
    x = a
    while x <= b:
        result.append((x, f(x)))
        x += h
    return result

def save_to_list(values):
    value_list = []
    for x, y in values:
        value_list.append((x, y))
    return value_list

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть крок h: "))

result_for = tabulate_with_for(a, b, h)
print("\n Табулювання з циклом for:")
for x, y in result_for:
    print(f"x = {x}, f(x) = {y}")

result_while = tabulate_with_while(a, b, h)
print("\n Табулювання з циклом while:")
for x, y in result_while:
    print(f"x = {x}, f(x) = {y}")

saved_values = save_to_list(result_for) 
print("\n Значення, записані у список:")
for x, y in saved_values:
    print(f"x = {x}, f(x) = {y}")
