def function(n, a):
    for i in range(1, n):
        current = a[i]
        pointer = 1

        while i - pointer >= 0 and current < a[i - pointer]:
            a[i - pointer + 1], a[i - pointer] = a[i - pointer], current
            pointer += 1

    return a


if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    n = int(input.readline().strip())
    a = list(map(int, input.readline().strip().split()))

    res = function(n, a)

    output.write(" ".join(map(str, a)))
