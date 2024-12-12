def function(a, b):
    if (a > 1e9 or a < -1e9 or b > 1e9 or b < -1e9):
        raise "out of bounds"
    return a + b * b


if __name__ == "__main__": pass
    # a, b = list(map(int, input().split()))
    # print(function(a, b))