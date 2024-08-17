### README.md

**[🇬🇧 English Version](#filesystem-rree-generator) | [🇷🇺 Русская Версия](#генератор-дерева-файловой-системы)**

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
Configure the script in the `config` dictionary to suit your needs. Then, run the script:

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
Настройте скрипт в словаре `config` в соответствии с вашими потребностями. Затем запустите скрипт:

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
