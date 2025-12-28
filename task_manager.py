from datetime import date
import json


def start():
    action = [
        "1 - Создать задачу",
        "2 - Завершить задачу",
        "3 - Вывести список задачь",
        "4 - Выключить менеджер",
    ]

    print("Приветсвую вас в менеджере задач!")
    while True:
        print()
        print(*action, sep="\n")
        print()
        answer = int(input("Напишите цифру вашего действия !\n"))
        if answer == 1:
            print(add_task())
        elif answer == 2:
            edit_task()
        elif answer == 3:
            show_list_tasks()
        elif answer == 4:
            print("Пока")
            break
        else:
            print("Невенрная операция введите число от 1 до 4")


def add_task(ready=False, today=date.today(), option=None):
    tasks = load_task()
    if tasks:
        last_id = max(task["id"] for task in tasks)
    else:
        last_id = 0
    name_task = input("Как будет называться задача ?")
    new_id = last_id + 1
    if name_task:
        task = {
            "id": new_id,
            "name_task": name_task.strip(),
            "option": option,
            "Ready": ready,
            "date": f"{today.day}-{today.month}-{today.year}",
        }
        tasks.append(task)
        save_tasks(tasks)
        print(f"Задача '{name_task}' добавлена с id = {new_id}")
    else:
        print("Имя задачи должно быть обязательно заполненно")


def edit_task():
    answer = input("Вы точно уверены что готовы завершить задачу!")
    if answer.lower() not in ["yes", "y", "да", "конечно", "д"]:
        print("Вы отказались завершать задачу.")
        return

    name_task = input("Напишите id или Имя задачи чтобы завершить её \n")
    tasks = load_task()
    found = False

    for task in tasks:
        if task["name_task"] == name_task or str(task["id"]) == name_task:
            task["Ready"] = True
            found = True
            print(
                f"Поздравляем вы завершили задачу {task['name_task']}. Дальнейших успехов !"
            )
            break

    if not found:
        print("Вы ввели некорректные данные!")
    save_tasks(tasks)


def show_list_tasks(ready=False):
    for i in load_task():
        if i["Ready"]:
            print(
                f"Задача: '{i['name_task']}', под номером id = '{i['id']}', создана '{i['date']}', ЗАВЕРШЕНА!"
            )
        else:
            print(
                f"Задача: '{i['name_task']}', под номером id = '{i['id']}', создана '{i['date']}', Еще НЕ ЗАВЕРШЕНА"
            )


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(
            tasks,
            f,
            indent=4,
            ensure_ascii=False,
        )


def load_task():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data


start()
