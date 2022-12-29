first = float(input("First: "))
operator = str(input("Operator: "))
second = float(input("Second: "))
result = 0
if operator == "+":
    result = first + second
if operator == "-":
    result = first - second
if operator == "*":
    result = first * second
if operator == "/":
    result = first / second

print("Ergebnis: " + str(round(result, 4)))
