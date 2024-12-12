def function(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for i in range(2, n + 1):
        previous, current = current, (previous + current) % 10
    return current


if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    n = int(input.readline().strip())
    output.write(f"{function(n)}")
