import math
import random


# Исходные данные
measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

# Первый проход: сумма, мин, макс, чётные (без min/max/sum/count)
total_sum = 0
min_val = measurements[0]
max_val = measurements[0]
even_count = 0

for val in measurements:
    total_sum += val
    if val < min_val:
        min_val = val
    if val > max_val:
        max_val = val
    if val % 2 == 0:
        even_count += 1

mean_val = total_sum / len(measurements)

# Второй проход: подсчёт значений выше среднего
above_mean_count = 0
for val in measurements:
    if val > mean_val:
        above_mean_count += 1

print("=== Анализ измерений ===")
print(f"Сумма: {total_sum}")
print(f"Мин: {min_val}, Макс: {max_val}")
print(f"Чётных: {even_count}")
print(f"Среднее: {mean_val:.2f}")
print(f"Выше среднего: {above_mean_count}")


# Линейный поиск первого вхождения
def linear_search(arr: list[int], target: int) -> int:
    """Возвращает индекс первого вхождения или -1."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


target = int(input("\nВведите число для поиска: "))
idx = linear_search(measurements, target)
print(f"Линейный поиск {target}: индекс = {idx}")


# Проверка простоты до √n
def is_prime(n: int) -> bool:
    """Проверяет, является ли n простым числом."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


print("\n=== Проверка простоты ===")
for n in [2, 7, 12, 17, 25, 97, 100]:
    print(f"{n} простое? {is_prime(n)}")


# Практическое расширение: сортировка выбором и бинарный поиск
def selection_sort(arr: list[int]) -> tuple[list[int], int]:
    """Сортировка выбором. Возвращает (отсортированный список, число сравнений)."""
    result = arr.copy()
    comparisons = 0
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result, comparisons


def binary_search(arr: list[int], target: int) -> tuple[int, int]:
    """Бинарный поиск в отсортированном списке. Возвращает (индекс или -1, число сравнений)."""
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = left + (right - left) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons


def linear_search_count(arr: list[int], target: int) -> int:
    """Линейный поиск с подсчётом сравнений."""
    comparisons = 0
    for val in arr:
        comparisons += 1
        if val == target:
            return comparisons
    return comparisons


def compare_searches():
    """Сравнительная таблица на наборах 10, 100, 1000 элементов."""
    random.seed(42)
    print("\n=== Сравнительная таблица ===")
    print(f"{'N':<6} {'Сортировка':<12} {'Лин. поиск (ср.)':<18} {'Бин. поиск (ср.)':<18} {'Ускорение'}")
    print("-" * 70)

    for n in [10, 100, 1000]:
        raw = random.sample(range(n * 10), n)
        sorted_arr, sort_comps = selection_sort(raw)

        # 50 запросов: половина — элементы массива, половина — отсутствующие
        targets = [
            random.choice(sorted_arr) if random.random() < 0.5
            else n * 10 + 1
            for _ in range(50)
        ]

        lin_total = sum(linear_search_count(sorted_arr, t) for t in targets)
        bin_total = sum(binary_search(sorted_arr, t)[1] for t in targets)

        lin_avg = lin_total / 50
        bin_avg = bin_total / 50
        speedup = lin_avg / bin_avg if bin_avg > 0 else float("inf")

        print(f"{n:<6} {sort_comps:<12} {lin_avg:<18.1f} {bin_avg:<18.1f} {speedup:.1f}x")


compare_searches()
