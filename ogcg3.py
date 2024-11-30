import numpy as np
import matplotlib.pyplot as plt

# Функція для зчитування координат з файлу
def read_coordinates_from_file(filename):
    coordinates = []  # Список для зберігання координат
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())  # Перетворюємо кожен рядок у пару чисел
            coordinates.append((x, y))
    return np.array(coordinates)

# Функція для обчислення векторного добутку, що визначає орієнтацію трьох точок
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Алгоритм Ендрю для обчислення опуклої оболонки
def andrew_algorithm(points):
    # Сортуємо точки по x та y (перетворюємо на список кортежів)
    points = sorted(points.tolist())  # Перетворюємо на список кортежів перед сортуванням

    # Створюємо нижню оболонку
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Створюємо верхню оболонку
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Відкидаємо останні точки з кожної оболонки, оскільки вони дублюються
    return lower[:-1] + upper[:-1]

# Функція для малювання точок та опуклої оболонки
def plot_points_and_hull(points, convex_hull_points):
    """
    Малює точки та опуклу оболонку за допомогою matplotlib.
    """
    # Створюємо графік
    plt.figure(figsize=(9.6, 5.4))
    
    # Малюємо точки
    points = np.array(points)
    plt.scatter(points[:, 0], points[:, 1], color='red', label='Points', zorder=5)

    # Малюємо опуклу оболонку
    convex_hull_points = np.array(convex_hull_points)
    plt.plot(np.append(convex_hull_points[:, 0], convex_hull_points[0, 0]), 
             np.append(convex_hull_points[:, 1], convex_hull_points[0, 1]), 
             color='blue', label='Convex Hull', linewidth=2)


    # Зберігаємо графік у файл
    plt.savefig("convex_hull_output.png", dpi = 300)

    # Показуємо графік
    plt.show()

# Основна функція
def main():
    # Читання координат з файлу
    filename = 'c:/Users/user/Documents/ogcglabs/DS5.txt'  
    coordinates = read_coordinates_from_file(filename)

     

    # Обчислюємо опуклу оболонку за допомогою алгоритму Ендрю
    convex_hull_points = andrew_algorithm(coordinates)

    # Малюємо точки та опуклу оболонку
    plot_points_and_hull(coordinates, convex_hull_points)


if __name__ == "__main__":
    main()


