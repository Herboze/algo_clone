def function(a, n):
    for i in range(a):
        min_idx = i
        for j in range(i + 1, a):
            if n[j] < n[min_idx]:
                min_idx = j
        n[i], n[min_idx] = n[min_idx], n[i]

    return n

if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    n = int(input.readline().strip())
    a = list(map(int, input.readline().strip().split()))

    res = function(n, a)

    output.write(" ".join(map(str, a)))
