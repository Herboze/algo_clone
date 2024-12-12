from lab4.utils import read, write, Stack


def function(sequence: str) -> str:
    stack = Stack()
    opening_brackets = {'(': ')', '[': ']', '{': '}'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    for index, char in enumerate(sequence):
        if char in opening_brackets:
            stack.push_back((char, index + 1))
        elif char in closing_brackets:
            if stack.is_empty() or stack.face()[0] != closing_brackets[char]:
                return str(index + 1)
            stack.pop()

    if not stack.is_empty():
        return str(stack.face()[1])

    return "Success"


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = file.readline().strip()
    file.close()
    result = function(n)

    print(f"\nINPUT: {n}")
    print(f"OUTPUT:\n{result}")

    write('../txtf/output.txt', str(result))
