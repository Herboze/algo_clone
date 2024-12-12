from lab6.utils import read, write


def function(n, x, a, b, ac, bc, ad, bd):
    MOD_A = 10 ** 3
    MOD_B = 10 ** 15
    MOD_X = 10 ** 15

    hash_table = set()  # Используем `set` для хранения чисел

    for _ in range(n):
        if x in hash_table:
            # Если X уже есть в таблице
            a = (a + ac) % MOD_A
            b = (b + bc) % MOD_B
        else:
            # Если X нет в таблице
            hash_table.add(x)
            a = (a + ad) % MOD_A
            b = (b + bd) % MOD_B

        # Обновляем X
        x = (x * a + b) % MOD_X

    return x, a, b


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n, x, a, b = map(int, file.readline().strip().split())
    ac, bc, ad, bd = map(int, file.readline().strip().split())
    file.close()

    x, a, b = function(n, x, a, b, ac, bc, ad, bd)

    print(f"\nINPUT: {n, x, a, b, ac, bc, ad, bd}")
    print(f"OUTPUT:\n{x, a, b}")

    write('../txtf/output.txt', f"{x} {a} {b}")
