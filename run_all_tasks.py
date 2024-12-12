import os
import subprocess


def run_tasks():
    labs = sorted([f for f in os.listdir() if os.path.isdir(f) and f.startswith("lab")])
    print(f"Запуск всех задач:\n\n")

    for lab in labs:

        lab_path = os.path.join(lab, "run_tasks.py")
        if os.path.exists(lab_path):
            try:
                # Перехожу в директорию лабораторной работы и запускаю run_tasks.py
                result = subprocess.run(["python3", "run_tasks.py"], check=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, cwd=f"{os.getcwd()}/{lab}")
                print(result.stdout.decode())
            except subprocess.CalledProcessError as e:
                print(f"Ошибка при выполнении задач для {lab}: {e}")
        else:
            print(f"Файл {lab_path} не найден.")


if __name__ == "__main__":
    run_tasks()
