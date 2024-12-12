from lab4.utils import read, write, Queue


def function(lines: list[str]) -> str:
    queue: Queue = Queue()

    res: list[str] = []

    for line in lines[1:]:
        match line.strip():
            case "-":
                queue.pop()
            case "?":
                res.append(str(queue.min()))
            case _:
                operand, value = line.strip().split()
                queue.push(int(value))
    return '\n'.join(res)


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    data = file.readlines()
    res = function(data)
    file.close()

    print(f"\nINPUT: {list(data)}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', res)
