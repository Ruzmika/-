print("Количество операций:")
score = int(input())
print("Введите число:")
a = float(input())
num = a
for i in range(score):
    print("Введите число:")
    b = float(input())
    print("Знак (+,-,*,/,^): ")
    var = (input())
    if var == "-":
        num -= b
        print("Ответ: ""%.2f" % (num))
        i -= 1
    elif var == "+":
        num += b
        print("Ответ: ""%.2f" % (num))
        i -= 1
    elif var == "/":
        if b == 0:
            i += 1
            continue
        num = float(num / b)
        print("Ответ: ""%.2f" % (num))
        i -= 1
    elif var == "*":
        num *= b
        print("Ответ: " "%.2f" % (num))
        i -= 1
    elif var == "^":
        num **= b
        print("Ответ: " "%.2f" % (num))
    else:
        print("Ошибка")