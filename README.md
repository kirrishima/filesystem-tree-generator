**[🇬🇧 English Version](#filesystem-tree-generator) | [🇷🇺 Русская Версия](#генератор-дерева-файловой-системы)**

# Filesystem Tree Generator

This Python script generates a visual representation of the filesystem tree in a specified directory and saves it to a text file. The script allows for various configurations to skip or ignore certain directories and files based on patterns.

## Features
- Generate a filesystem tree for a specified directory.
- Skip directories based on specific patterns.
- Ignore files or directories using customizable patterns.
- Exception handling for specific files or directories.

## Requirements
- Python 3.x

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/filesystem-tree-generator.git
```
Navigate to the project directory:
```bash
cd filesystem-tree-generator
```

## Usage
Configure the script in the `config` dictionary to suit your needs. 

### Configuration
- `file_path`: The name of the file where the tree will be saved.
- `skip_content_folders`: Folders whose contents will be skipped.
- `ignore_patterns`: Folders and files that will be skipped (uses `fnmatch` patterns).
- `hard_ignores`: Similar to `ignore_patterns`, but bypasses exceptions.
- `exceptions`: Files or folders that will not be ignored despite matching ignore patterns.

Then, run the script:

```bash
python generate_tree.py
```

### Example Configuration:
```python
config = {
    "file_path": "filesystem_tree.txt",
    "skip_content_folders": [
        "folder1/subfolder",
        "folder2/subfolder"
    ],
    "ignore_patterns": [
        ".git", "*.pyc", "__pycache__"
    ],
    "hard_ignores": [
        "*.log", "*.tmp"
    ],
    "exceptions": [
        "important_folder"
    ]
}
```

### Example Output

```
folder
├── fd — копия.py
├── file.txt
├── filesystem_tree.txt
├── folder1
│   └── subfolder
│       └── ◯ ◯ ◯
├── folder2
│   └── subfolder
│       └── ◯ ◯ ◯
└── folder3
    ├── file.txt
    └── subfolder
        └── file.txt
```

The generated filesystem tree will be saved in the file specified in the `file_path` configuration, typically `filesystem_tree.txt`.

---

# Генератор Дерева Файловой Системы

Этот скрипт на Python генерирует визуальное представление дерева файловой системы в указанной директории и сохраняет его в текстовый файл. Скрипт позволяет настроить различные параметры для пропуска или игнорирования определённых директорий и файлов на основе шаблонов.

## Возможности
- Генерация дерева файловой системы для указанной директории.
- Пропуск директорий на основе определённых шаблонов.
- Игнорирование файлов или директорий с использованием настраиваемых шаблонов.
- Обработка исключений для определённых файлов или директорий.

## Требования
- Python 3.x

## Установка
Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/filesystem-tree-generator.git
```
Перейдите в каталог проекта:
```bash
cd filesystem-tree-generator
```

## Использование
Настройте скрипт в словаре `config` в соответствии с вашими потребностями. 

### Конфигурация
- `file_path`: Название файла, в который будет сохранено дерево.
- `skip_content_folders`: Папки, содержимое которых будет пропущено.
- `ignore_patterns`: Папки и файлы, которые будут пропущены (используются шаблоны `fnmatch`).
- `hard_ignores`: Аналогично `ignore_patterns`, но игнорирует исключения.
- `exceptions`: Файлы или папки, которые не будут проигнорированы, даже если совпадают с шаблонами игнорирования.

Затем запустите скрипт:

```bash
python generate_tree.py
```

### Пример настройки:
```python
config = {
    "file_path": "filesystem_tree.txt",
    "skip_content_folders": [
        "folder1/subfolder",
        "folder2/subfolder"
    ],
    "ignore_patterns": [
        ".git", "*.pyc", "__pycache__"
    ],
    "hard_ignores": [
        "*.log", "*.tmp"
    ],
    "exceptions": [
        "important_folder"
    ]
}
```

### Пример Результата

```
folder
├── fd — копия.py
├── file.txt
├── filesystem_tree.txt
├── folder1
│   └── subfolder
│       └── ◯ ◯ ◯
├── folder2
│   └── subfolder
│       └── ◯ ◯ ◯
└── folder3
    ├── file.txt
    └── subfolder
        └── file.txt
```

Сгенерированное дерево файловой системы будет сохранено в файле, указанном в конфигурации `file_path`, обычно `filesystem_tree.txt`.
