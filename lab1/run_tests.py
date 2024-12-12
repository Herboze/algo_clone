import os
import subprocess


def run_tests():
    tasks = sorted([f for f in os.listdir() if os.path.isdir(f) and f.startswith("task")], key=lambda x: int(x[4:]))
    print(f"Запуск тестов для лабораторной работы №{os.getcwd()[-1]}...")
    for task in tasks:
        tests_path = os.path.join(task, "tests/Tests.py")
        if os.path.exists(tests_path):
            print(
                f"----------------------------------------------------------------------\nТестирую задачу №{task[4:]}:\n----------------------------------------------------------------------")
            subprocess.run(["python3", "-m", "unittest", "Tests.py"], check=True, cwd=os.path.join(task, "tests"))
        else:
            raise "Файл Tests.py не найден."


if __name__ == "__main__":
    run_tests()
