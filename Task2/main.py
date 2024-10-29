import turtle

# Функція для малювання сегмента кривої Коха
def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

# Функція для малювання сніжинки Коха з трьох кривих
def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

# Основна функція програми
def main():
    # Запитуємо рівень рекурсії у користувача
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    length = 300  # Довжина сторони сніжинки

    # Налаштування екрану та черепашки
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    # Малювання сніжинки Коха
    koch_snowflake(t, length, level)

    # Завершення програми
    turtle.done()

if __name__ == "__main__":
    main()