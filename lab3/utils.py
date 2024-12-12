def measuring_time_and_memory(task_func, *args):
    import time
    import memory_profiler

    start_time = time.monotonic_ns()
    result = task_func(*args)
    end_time = time.monotonic_ns() - start_time

    memory = memory_profiler.memory_usage((task_func, args))
    human_read_input = f"Input: {args}"[:100] + "..." if len(f"Input: {args}") > 100 else f"Input: {args}"
    human_read_result = f"Result: {result}"[:100] + "..." if len(f"Result: {result}") > 100 else f"Result: {result}"

    print(f"\n{human_read_input}")
    print(human_read_result)
    print(f"Execution time: {end_time / 1e3:} microseconds")
    print(f"Peak memory usage: {memory[0]:.2f} bytes\n\n")

    return result, end_time / 1e9, memory[0] / (1024 * 1024)


def generate_random_array(size):
    import random
    return random.sample(range(-10 ** 9, 10 ** 9), size)


def read(path: str):
    return open(path, 'r')


def write(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()
