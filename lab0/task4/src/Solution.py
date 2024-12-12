def function(a, b):
    if (a > 1e9 or a < -1e9 or b > 1e9 or b < -1e9):
        raise "out of bounds"
    return a + b * b


if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    a, b = list(map(int, input.readline().split()))
    output.write(f"{function(a, b)}")
