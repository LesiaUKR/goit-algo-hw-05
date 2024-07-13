def binary_search(arr, x):
    left, right = 0, len(arr) - 1  # Визначаємо початкові індекси лівої та правої межі
    iterations = 0  # Лічильник ітерацій
    upper_bound = None  # Змінна для зберігання "верхньої межі"

    while left <= right:
        iterations += 1  # Збільшуємо лічильник ітерацій
        mid = (left + right) // 2  # Знаходимо середній елемент
        
        if arr[mid] == x:
            # Якщо середній елемент дорівнює x, повертаємо кількість ітерацій і сам елемент
            return (iterations, arr[mid])
        elif arr[mid] < x:
            # Якщо середній елемент менший за x, зсуваємо ліву межу вправо
            left = mid + 1
        else:
            # Якщо середній елемент більший за x, зсуваємо праву межу вліво
            right = mid - 1
    
    # Визначаємо "верхню межу" після завершення циклу
    if left < len(arr):
        # Якщо left не вийшов за межі масиву, встановлюємо upper_bound як arr[left]
        upper_bound = arr[left]
    else:
        # Якщо left вийшов за межі масиву, встановлюємо upper_bound як "No upper bound found"
        upper_bound = "No upper bound found"

    # Повертаємо кількість ітерацій і "верхню межу"
    return (iterations, upper_bound)

# Приклад використання:
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
x = 7.0
iterations, upper_bound = binary_search(arr, x)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}") # Виведе: Iterations: 3, Upper bound: No upper bound found

x = 4.0
iterations, upper_bound = binary_search(arr, x)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}") # Виведе: Iterations: 2, Upper bound: 4.4