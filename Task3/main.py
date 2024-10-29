def hanoi(n, source, target, auxiliary, state):
    if n > 0:
        # Переміщуємо n-1 дисків з source на auxiliary
        hanoi(n - 1, source, auxiliary, target, state)

        # Переміщуємо найбільший диск з source на target
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")

        # Переміщуємо n-1 дисків з auxiliary на target
        hanoi(n - 1, auxiliary, target, source, state)


def main():
    # Запитуємо кількість дисків
    n = int(input("Введіть кількість дисків: "))

    # Початковий стан стрижнів
    state = {
        'A': list(range(n, 0, -1)),  # Список дисків на стрижні A від найбільшого до найменшого
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {state}")

    # Виконуємо алгоритм Ханойських веж
    hanoi(n, 'A', 'C', 'B', state)

    print(f"Кінцевий стан: {state}")


if __name__ == "__main__":
    main()