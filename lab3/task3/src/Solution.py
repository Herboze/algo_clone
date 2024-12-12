from lab3.utils import read, write


def function(n, k, sizes):
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(sizes[i])

    for group in groups:
        group.sort()

    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(groups[i % k][i // k])

    for i in range(1, n):
        if sorted_sizes[i] < sorted_sizes[i - 1]:
            return "НЕТ"
    return "ДА"


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n, k = map(int, file.readline().split())
    sizes = list(map(int, file.readline().split()))
    file.close()

    result = function(n, k, sizes)

    write('../txtf/output.txt', result + "\n")
