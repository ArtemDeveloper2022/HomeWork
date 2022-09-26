num1 = int(input())
action = input()
num2 = int(input())

if action == '-':
    print(num1 - num2)
elif action == '+':
    print(num1 + num2)
elif action == '/':
    print(num1 / num2)
elif action == '*':
    print(num1 * num2)
else:
    print("Введен не верный арифметический оператор")