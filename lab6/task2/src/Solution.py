from lab6.utils import read, write


def function(operations):
    phone_book = {}
    results = []

    for operation in operations:
        parts = operation.split()
        command = parts[0]
        number = int(parts[1])

        if command == "add":
            name = parts[2]
            phone_book[number] = name
        elif command == "del":
            phone_book.pop(number, None)
        elif command == "find":
            results.append(phone_book.get(number, "not found"))

    return "\n".join(results)


if __name__ == "__main__":
    # Read input data
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    operations = file.readlines()
    file.close()

    # Process operations and write results to output
    res = function(operations)

    print(f"\nINPUT: {n, operations}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', res)
