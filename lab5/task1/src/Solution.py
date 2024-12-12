from lab5.utils import read, write


def function(arr, n):
    for i in range(1, n + 1):
        if 2 * i <= n and arr[i - 1] > arr[2 * i - 1]:
            return "NO"
        if 2 * i + 1 <= n and arr[i - 1] > arr[2 * i]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = list(map(int, file.readline().split()))[0]
    arr = list(map(int, file.readline().split()))
    file.close()

    res = function(arr, n)

    print(f"\nINPUT: {n, arr}")
    print(f"OUTPUT:\n{res}")
    write('../txtf/output.txt', res)
