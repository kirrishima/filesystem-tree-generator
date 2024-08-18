import os
import fnmatch

# Конфигурационный словарь
config = {
    "file_path": "filesystem_tree.txt",
    "skip_content_folders": [], 
    "ignore_patterns": [__file__],
    "hard_ignores": [],
    "exceptions": []
}

def preprocess(directory: str):
    with open(config["file_path"], "w") as file:
        pass

    # Преобразуем пути в абсолютные для исключений
    config["exceptions"] = [
        os.path.join(directory, path) for path in config["exceptions"]
    ]
    for key in list(config.keys()):
        if type(config[key]) is list:
            for _ in config[key]:
                for i in range(0, len(config[key])):
                    config[key][i] = config[key][i].replace("/", "\\")

def should_ignore(path, patterns):
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)

def is_exception(path):
    # hard_ignores обходят исключения
    if any(fnmatch.fnmatch(path, pattern) for pattern in config["hard_ignores"]):
        return False
    return any(os.path.commonpath([path, exc]) == exc for exc in config["exceptions"])

def process_tree_in_file(directory):
    IGNORE_CHARS = "└├│"
    file_path = os.path.join(directory, config["file_path"]) 

    with open(file_path, "r", encoding="utf-8") as ifstream:
        lines = ifstream.readlines()

    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i + 1]

        index = line.rfind("└")
        if index != -1 and len(next_line) > index and next_line[index] == "│":
            next_line = next_line[:index] + " " + next_line[index + 1:]
            lines[i + 1] = next_line

        index = line.rfind("├")
        if index != -1 and len(next_line) > index and next_line[index] not in IGNORE_CHARS:
            line = line[:index] + "└" + line[index + 1:]
            lines[i] = line

    with open(file_path, "w", encoding="utf-8") as ofstream:
        ofstream.writelines(lines)

    with open(file_path, "r+", encoding="utf-8") as ifstream:
        lines = ifstream.readlines()

        if lines[-1].find("├") != 1:
            lines[-1] = lines[-1].replace("├", "└", 1)
        else:
            lines[-1] = lines[-1].replace("├", "└")
            for i in range(len(lines) - 1, -1, -1):
                if lines[i][0] == "├":
                    lines[i] = "└" + lines[i][1:]
                    break
                lines[i] = " " + lines[i][1:]

        ifstream.seek(0)
        ifstream.writelines(lines)
        ifstream.truncate()

    print(f"Файловое дерево сохранено как {file_path}")

def generate_tree_recursive(directory, base_directory=None, prefix=""):
    if base_directory is None:
        base_directory = directory
        with open(config["file_path"], "a", encoding="utf-8") as file:
            file.write(directory.replace("/", "\\").split("\\")[-1] + "\n")

    contents = os.listdir(directory)
    pointers = ["├── "] * (len(contents) - 1) + ["└── "]

    for pointer, path in zip(pointers, contents):
        full_path = os.path.join(directory, path)
        relative_path = os.path.relpath(full_path, base_directory)
        name = os.path.basename(full_path)

        # Пропускаем исключения
        if is_exception(full_path):
            pass
        # Игнорируем папки и файлы на основе шаблонов
        elif should_ignore(relative_path, config["ignore_patterns"]) or should_ignore(relative_path, config["hard_ignores"]):
            continue

        with open(config["file_path"], "a", encoding="utf-8") as file:
            file.write(prefix + pointer + name + "\n")

        if os.path.isdir(full_path):
            if should_ignore(relative_path, config["skip_content_folders"]):
                with open(config["file_path"], "a", encoding="utf-8") as file:
                    file.write(prefix + "│   └── ◯ ◯ ◯\n")
            else:
                extension = "│   " if pointer == "├── " else "    "
                generate_tree_recursive(full_path, base_directory, prefix + extension)

def generate_tree(directory):
    preprocess(directory)
    generate_tree_recursive(directory)
    process_tree_in_file(directory)

# Путь к папке для генерации древа файловой системы. По умолчанию применяется путь файла python 
base_directory = os.path.abspath(__file__).replace(
    "\\" + os.path.basename(__file__), ""
)
base_directory = base_directory[:2].capitalize() + base_directory[2:]
generate_tree(base_directory)
input("Ожидание выхода...")
