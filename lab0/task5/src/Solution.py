def function(n):
    if (n > 45 or n <= 0):
        raise "out of bounds"
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    n = int(input.readline().strip())
    output.write(f"{function(n)}")
