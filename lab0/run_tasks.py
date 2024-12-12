import os
import subprocess


def run_tasks():
    tasks = sorted([f for f in os.listdir() if os.path.isdir(f) and f.startswith("task")], key=lambda x: int(x[4:]))
    print(f"Запуск решений для лабораторной работы №{os.getcwd()[-1]}...\nКол-во заданий: {len(tasks)}\n")

    for task in tasks:
        src_path = os.path.join(task, "src/Solution.py")
        if os.path.exists(src_path):
            print(
                f"----------------------------------------------------------------------\nЗадача №{task[4:]}:",
                end=" ")
            subprocess.run(["python3", "Solution.py"], check=True, cwd=os.path.join(task, "src"))
            print("DONE\n----------------------------------------------------------------------")

        else:
            raise f"Файл {src_path} не найден."


if __name__ == "__main__":
    run_tasks()
