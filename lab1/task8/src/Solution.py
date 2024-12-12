def function(n: int, a: list[int]) -> str:
    res = []
    result = []

    for _ in range(n):
        minimum = 10 ** 10
        index = -1

        for i, v in enumerate(a):
            if minimum > v:
                minimum = v
                index = i

        a[index], a[len(res)] = a[len(res)], 10 ** 10
        res.append(index)

    for i, x in enumerate(res):
        if i != x:
            result.append(f"Swap elements at indices {1 + min(x, i)} and {1 + max(x, i)}.\n")
    result.append("No more swaps needed.")

    return ''.join(result)


if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    n = int(input.readline().strip())
    a = list(map(float, input.readline().strip().split()))

    res = function(n, a)

    output.write(res)
