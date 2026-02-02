import csv
import heapq
import sys

def read_graph_from_csv(filename):
    """Чтение матрицы смежности из CSV-файла"""
    graph = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Преобразуем строки в числа, заменяем пустые значения на 0
            graph_row = []
            for val in row:
                if val == '' or val == '0':
                    graph_row.append(0)
                else:
                    graph_row.append(float(val) if '.' in val else int(val)) # тернарный оператор
            graph.append(graph_row)
    return graph

def dijkstra(graph, start, end):
    """Алгоритм Дейкстры для поиска кратчайшего пути"""
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    previous = [-1] * n
    visited = [False] * n
    
    # Приоритетная очередь: (расстояние, вершина)
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if visited[current]:
            continue
            
        visited[current] = True
        
        # Если дошли до конечной вершины
        if current == end:
            break
        
        # Проверяем всех соседей
        for neighbor in range(n):
            weight = graph[current][neighbor]
            if weight > 0:  # Есть ребро
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
    
    # Восстанавливаем путь
    if distances[end] == float('inf'):
        return None, float('inf')
    
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return path, distances[end]

def bfs_shortest_path(graph, start, end):
    """BFS для поиска кратчайшего пути в невзвешенном графе"""
    n = len(graph)
    visited = [False] * n
    previous = [-1] * n
    queue = [start]
    visited[start] = True
    
    while queue:
        current = queue.pop(0)
        
        if current == end:
            break
        
        for neighbor in range(n):
            if graph[current][neighbor] > 0 and not visited[neighbor]:
                visited[neighbor] = True
                previous[neighbor] = current
                queue.append(neighbor)
    
    # Если путь не найден
    if not visited[end]:
        return None
    
    # Восстанавливаем путь
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return path

print("Программа для поиска кратчайшего пути в графе")

# Запрос имени файла
filename = input("Введите имя CSV-файла с матрицей смежности: ")

try:
    # Чтение графа из файла
    graph = read_graph_from_csv(filename)
    n = len(graph)
    
    print(f"\nГраф успешно загружен из файла '{filename}'")
    print(f"Количество вершин: {n}")
    
    # Вывод информации о графе
    print("\nМатрица смежности (первые 5 строк и столбцов):")
    for i in range(min(5, n)):
        row_preview = []
        for j in range(min(5, n)):
            row_preview.append(str(graph[i][j]))
        if n > 5:
            row_preview.append("...")
        print("  ".join(row_preview))
    if n > 5:
        print("...")
    
    # Определяем тип графа (взвешенный или нет)
    is_weighted = False
    for i in range(min(n, 10)):
        for j in range(min(n, 10)):
            if graph[i][j] > 0 and graph[i][j] != 1:
                is_weighted = True
                break
    
    print(f"\nТип графа: {'Взвешенный' if is_weighted else 'Невзвешенный'}")
    
    # Запрос вершин у пользователя
    print("\n" + "=" * 50)
    print("Введите номера вершин (от 0 до {})".format(n-1))
    
    while True:
        try:
            start = int(input(f"Начальная вершина (0-{n-1}): "))
            if 0 <= start < n:
                break
            else:
                print(f"Ошибка: вершина должна быть в диапазоне 0-{n-1}")
        except ValueError:
            print("Ошибка: введите целое число")
    
    while True:
        try:
            end = int(input(f"Конечная вершина (0-{n-1}): "))
            if 0 <= end < n:
                break
            else:
                print(f"Ошибка: вершина должна быть в диапазоне 0-{n-1}")
        except ValueError:
            print("Ошибка: введите целое число")
    
    # Поиск кратчайшего пути
    print("\n" + "=" * 50)
    print(f"Поиск кратчайшего пути из вершины {start} в вершину {end}...")
    
    if is_weighted:
        path, distance = dijkstra(graph, start, end)
        if path:
            print(f"Кратчайший путь найден!")
            print(f"Длина пути: {distance}")
            print(f"Маршрут: {' -> '.join(map(str, path))}")
        else:
            print(f"Путь из вершины {start} в вершину {end} не существует")
    else:
        path = bfs_shortest_path(graph, start, end)
        if path:
            print(f"Кратчайший путь найден!")
            print(f"Длина пути: {len(path)-1} ребер")
            print(f"Маршрут: {' -> '.join(map(str, path))}")
        else:
            print(f"Путь из вершины {start} в вершину {end} не существует")
            
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден")
except Exception as e:
    print(f"Ошибка: {str(e)}")
