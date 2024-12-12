from lab3.utils import read, write


def anti_quick_sort(n):
    perm = list(range(1, n + 1))
    for i in range(2, n):
        perm[i], perm[i // 2] = perm[i // 2], perm[i]
    return perm


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    file.close()

    array = anti_quick_sort(n)

    write('../txtf/output.txt', ' '.join(map(str, array)))
