from lab6.utils import read, write


def function(lines):
    vote_count = {}

    for line in lines:
        # Разделяем строку на имя кандидата и количество голосов
        name, count = line.rsplit(maxsplit=1)
        count = int(count)

        # Суммируем голоса для каждого кандидата
        if name in vote_count:
            vote_count[name] += count
        else:
            vote_count[name] = count

    # Сортируем кандидатов лексикографически
    sorted_results = sorted(vote_count.items())

    # Формируем результат в виде строки
    result = "\n".join(f"{name} {count}" for name, count in sorted_results)
    return result


if __name__ == "__main__":
    # Чтение входных данных
    file = read('../txtf/input.txt')
    lines = file.readlines()
    file.close()

    # Подсчет голосов
    res = function(lines)

    print(f"\nINPUT: {list(lines)}")
    print(f"OUTPUT:\n{res}")

    # Запись результата в файл
    write('../txtf/output.txt', res)
