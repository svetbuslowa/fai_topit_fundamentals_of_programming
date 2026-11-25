# === Функции с контрактами ===

def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        raise ValueError("Список не должен быть пустым")
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    if not name or not name.strip():
        return ""
    return " ".join(p.capitalize() for p in name.strip().split())


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    if not results:
        return f"{prefix} для {student}: нет данных"
    mean = arithmetic_mean(results)
    return f"{prefix} для {student}: {mean:.{precision}f} (по {len(results)} оценкам)"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    seen = set()
    result = []
    for tag in tags:
        cleaned = tag.strip().lower() if lowercase else tag.strip()
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            result.append(cleaned)
    return tuple(result)


# === Проверки через assert ===

# arithmetic_mean
assert arithmetic_mean([2, 4, 6]) == 4.0
assert arithmetic_mean([10]) == 10.0
assert arithmetic_mean([1.0, 2.0, 3.0, 4.0]) == 2.5
try:
    arithmetic_mean([])
    assert False, "Должно было возникнуть исключение"
except ValueError:
    pass

# normalize_name
assert normalize_name("  anna   ivanova  ") == "Anna Ivanova"
assert normalize_name("bob") == "Bob"
assert normalize_name("  ") == ""

# build_report
assert build_report("Анна", [80, 90]) == "Результат для Анна: 85.00 (по 2 оценкам)"
assert build_report("Борис", [], prefix="Итог") == "Итог для Борис: нет данных"
assert build_report("Дарья", [100], precision=0) == "Результат для Дарья: 100 (по 1 оценкам)"

# collect_tags
assert collect_tags("Python", "python", " ML ", "") == ("python", "ml")
assert collect_tags("A", "B", "A", lowercase=False) == ("A", "B")
assert collect_tags() == ()

print("Все assert-проверки пройдены.")


# === Демонстрация распаковки ===

args = ["Анна", [78, 91, 84]]
kwargs = {"precision": 1, "prefix": "Отчёт"}
print("\n=== Распаковка ===")
print(build_report(*args, **kwargs))


# === Исследование LEGB ===

course = "Python"


def outer_func():
    level = "Intermediate"

    def inner_func():
        nonlocal level
        level = "Advanced"
        print(f"Inside inner: course={course}, level={level}")

    inner_func()
    print(f"Inside outer: level={level}")


print("\n=== LEGB ===")
outer_func()


# === Ошибка изменяемого значения по умолчанию ===

def add_result_bad(value, results=[]):
    results.append(value)
    return results


def add_result_good(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


print("\n=== Изменяемое значение по умолчанию ===")
print("bad:", add_result_bad(1), add_result_bad(2))
print("good:", add_result_good(1), add_result_good(2))


# === Практическое расширение: замыкания ===

def apply_to_results(operation, values):
    """Применяет функцию operation ко всем элементам values."""
    return [operation(v) for v in values]


def make_threshold_checker(threshold):
    """Фабрика функций проверки порога."""
    def checker(score):
        return score >= threshold
    return checker


def double(x):
    return x * 2


print("\n=== Замыкания ===")
print("apply (named):", apply_to_results(double, [1, 2, 3]))
print("apply (lambda):", apply_to_results(lambda x: x ** 2, [1, 2, 3]))

check_60 = make_threshold_checker(60)
check_90 = make_threshold_checker(90)
print("check_60(75):", check_60(75))
print("check_60(50):", check_60(50))
print("check_90(75):", check_90(75))
print("check_90(95):", check_90(95))
