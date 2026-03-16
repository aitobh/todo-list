import json
import os

FILE = "tasks.json"


# ==============================
# ASCII TITLE
# ==============================
def print_title():
    print(r"""
    ___    ______________      __________  ____  ____ 
   /   |  /  _/_  __/ __ \    /_  __/ __ \/ __ \/ __ \
  / /| |  / /  / / / / / /_____/ / / / / / / / / / / /
 / ___ |_/ /  / / / /_/ /_____/ / / /_/ / /_/ / /_/ / 
/_/  |_/___/ /_/  \____/     /_/  \____/_____/\____/  
          
          L'organisation à porté de vous


-------------------------------------------------------
                                                      
""")

# ==============================
# LOAD / SAVE
# ==============================
def load_tasks():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# ==============================
# PROGRESS BAR
# ==============================
def progress_bar(percent, size=10):

    filled = int(size * percent / 100)
    empty = size - filled

    return "[" + "■" * filled + " " * empty + f"] {percent}%"


# ==============================
# LIST TASKS
# ==============================
def list_tasks(tasks):

    if not tasks:
        print("\nAucune tâche.\n")
        return

    print("\nTÂCHES :\n")

    for i, t in enumerate(tasks):
        print(f"{i+1}. {t['name']}")
        print(f"   {progress_bar(t['progress'])}")
        print()


# ==============================
# CREATE TASK
# ==============================
def create_task(tasks):

    name = input("Nom de la tâche: ")

    task = {
        "name": name,
        "progress": 0
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Tâche ajoutée.")


# ==============================
# UPDATE TASK
# ==============================
def update_task(tasks):

    list_tasks(tasks)

    try:
        idx = int(input("Numéro de la tâche: ")) - 1
    except:
        return

    if idx < 0 or idx >= len(tasks):
        return

    print("1. Modifier le nom")
    print("2. Modifier la progression")

    choice = input("> ")

    if choice == "1":
        tasks[idx]["name"] = input("Nouveau nom: ")

    elif choice == "2":
        try:
            p = int(input("Progression (0-100): "))
            p = max(0, min(100, p))
            tasks[idx]["progress"] = p
        except:
            pass

    save_tasks(tasks)


# ==============================
# DELETE TASK
# ==============================
def delete_task(tasks):

    list_tasks(tasks)

    try:
        idx = int(input("Numéro à supprimer: ")) - 1
    except:
        return

    if idx < 0 or idx >= len(tasks):
        return

    tasks.pop(idx)
    save_tasks(tasks)

    print("Tâche supprimée.")


# ==============================
# MAIN LOOP
# ==============================
def main():

    tasks = load_tasks()

    while True:

        print_title()

        print("1. Lister les tâches")
        print("2. Ajouter une tâche")
        print("3. Modifier une tâche")
        print("4. Supprimer une tâche")
        print("5. Quitter")

        choice = input("\n> ")

        if choice == "1":
            list_tasks(tasks)

        elif choice == "2":
            create_task(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            break

        input("\nAppuyez sur entrée...")
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()