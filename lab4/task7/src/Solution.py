from lab4.utils import read, write, Deque


def sliding_window_maximum(n, array, m):
    deq: Deque = Deque()
    max_values = []

    for i in range(n):
        if len(deq) > 0 and deq[0] == i - m:
            deq.popleft()

        while len(deq) > 0 and array[deq[-1]] < array[i]:
            deq.pop()

        deq.append(i)

        if i >= m - 1:
            max_values.append(array[deq[0]])

    return max_values


if __name__ == "__main__":
    file = read('../txtf/input.txt')

    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))
    m = int(file.readline().strip())

    file.close()

    result = sliding_window_maximum(n, array, m)

    print(f"\nINPUT: {n, array, m}")
    print(f"OUTPUT:\n{result}")

    write("../txtf/output.txt", " ".join(map(str, result)))
