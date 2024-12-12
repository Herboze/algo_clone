from lab4.utils import read, write, Stack


def function(n, expression):
    stack = Stack()

    for i in range(n):
        token = expression[i]
        if token.isdigit():  # Если это число
            stack.push_back(int(token))
        else:  # Если это оператор
            b = stack.pop()
            a = stack.pop()
            result = None

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            if result:
                stack.push_back(result)

    return stack.pop()  # Результат выражения остается в стеке


if __name__ == "__main__":
    file = read('../txtf/input.txt')

    n = int(file.readline().strip())
    expression = file.readline().strip().split()

    file.close()

    result = function(n, expression)

    print(f"\nINPUT: {n, expression}")
    print(f"OUTPUT:\n{result}")

    write("../txtf/output.txt", str(result))
