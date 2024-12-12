def function(A, B):
    n = len(A)
    C = [0] * (n + 1)
    carry = 0

    for i in range(n - 1, -1, -1):
        sum_bits = int(A[i]) + int(B[i]) + carry
        C[i + 1] = sum_bits % 2
        carry = sum_bits // 2

    C[0] = carry
    result = ''.join(map(str, C))
    return result.lstrip('0') or '0'


if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    A, B = input.readline().strip().split()

    res = function(A, B)

    output.write(res)
