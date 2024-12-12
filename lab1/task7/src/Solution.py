def function(n, a: list[float]):
    dic: dict[int, float] = {}

    for idx, val in enumerate(a):
        dic[idx + 1] = val

    res = sorted(dic.items(), key=lambda x: x[1])
    return f"{res[0][0]} {res[n // 2][0]} {res[-1][0]}"

if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    n = int(input.readline().strip())
    a = list(map(float, input.readline().strip().split()))

    res = function(n, a)

    output.write(res)
