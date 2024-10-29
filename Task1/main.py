import os
import shutil
import sys
from pathlib import Path


def parse_arguments():
    # Отримуємо аргументи командного рядка
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    destination_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else source_dir / 'dist'

    # Перевіряємо існування вихідної директорії
    if not source_dir.is_dir():
        print(f"Помилка: Вихідна директорія '{source_dir}' не існує.")
        sys.exit(1)

    return source_dir, destination_dir


def copy_files(source_dir, destination_dir):
    # Рекурсивно перебираємо всі файли та директорії
    for item in source_dir.iterdir():
        # Якщо це директорія, викликаємо функцію рекурсивно
        if item.is_dir():
            copy_files(item, destination_dir)
        # Якщо це файл, копіюємо його
        elif item.is_file():
            try:
                # Отримуємо розширення файлу
                file_extension = item.suffix[1:].lower()  # Забираємо крапку та приводимо до нижнього регістру
                # Створюємо директорію для цього розширення
                extension_dir = destination_dir / file_extension
                extension_dir.mkdir(parents=True, exist_ok=True)
                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(item, extension_dir)
                print(f"Скопійовано {item} до {extension_dir}")
            except Exception as e:
                print(f"Помилка при копіюванні файлу {item}: {e}")


def main():
    # Парсинг аргументів командного рядка
    source_dir, destination_dir = parse_arguments()

    # Створюємо директорію призначення, якщо вона не існує
    destination_dir.mkdir(parents=True, exist_ok=True)

    # Рекурсивно копіюємо файли, сортуємо за розширенням
    copy_files(source_dir, destination_dir)


if __name__ == "__main__":
    main()