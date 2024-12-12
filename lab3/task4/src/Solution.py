from lab3.utils import read, write


def function(s, p, segments, points):
    events = []
    results = [0] * p

    for i in range(s):
        a, b = segments[i]
        events.append((a, 'L'))
        events.append((b, 'R'))

    for i in range(p):
        events.append((points[i], 'P', i))

    events.sort(key=lambda x: (x[0], x[1] != 'L', x[1] == 'R'))

    active_segments = 0

    for event in events:
        if event[1] == 'L':
            active_segments += 1
        elif event[1] == 'R':
            active_segments -= 1
        else:
            _, _, idx = event
            results[idx] = active_segments

    return " ".join(map(str, results))


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    s, p = map(int, file.readline().split())
    segments = [tuple(map(int, file.readline().split())) for _ in range(s)]
    points = list(map(int, file.readline().split()))
    file.close()

    result = function(s, p, segments, points)

    write('../txtf/output.txt', result + "\n")
