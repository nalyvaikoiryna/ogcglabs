import matplotlib.pyplot as plt

# Функція для зчитування координат з файлу
def read_coordinates_from_file(filename):
    coordinates = []  # Список для зберігання координат
    with open(filename, 'r') as file:
        for line in file:
            # Розбиваємо кожний рядок на два числа
            x, y = map(int, line.strip().split())
            coordinates.append((x, y))  # Додаємо пару координат до списку
    return coordinates

# Читання координат з файлу
filename = 'c:/Users/user/Documents/DS5.txt'  # Вкажіть шлях до вашого файлу
coordinates = read_coordinates_from_file(filename)

# Розпаковка координат у окремі списки для осей X і Y
x_coords, y_coords = zip(*coordinates)

# Створення графіка
plt.figure(figsize=(9.6, 5.4))  # Розмір графіка (960x540 пікселів)
plt.scatter(x_coords, y_coords, color='blue', s=10)  # Малюємо точки (сині, розмір 10)


# Збереження зображення у файл
plt.savefig('output.png', dpi=300)  # Збереження у форматі PNG 

# Виведення графіку 
plt.show()
