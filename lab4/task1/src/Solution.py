from lab4.utils import read, write, Stack


def function(lines: list[str]) -> str:
    stack: Stack = Stack()

    res: list[str] = []

    for line in lines[1:]:
        if line.strip() == "-":
            res.append(str(stack.pop()))
        else:
            operand, value = line.strip().split()
            stack.push_back(int(value))

    return '\n'.join(res)


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    data = list(file.readlines())
    res = function(data)
    file.close()

    print(f"\nINPUT: {data}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', res)
