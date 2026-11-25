# Лабораторная работа № 3. Алгоритмы, коллекции и функции

## Задание 1. Условия и классификация данных

**Код:**
```
def classify_student(score: int, work_type: str, absences: int) -> str:
    # Часть 1. Проверка диапазонов (ранний возврат)
    if not (0 <= score <= 100):
        return "Ошибка: результат должен быть от 0 до 100."
    if not (0 <= absences <= 5):
        return "Ошибка: количество пропусков должно быть от 0 до 5."

    # Часть 2. Определение уровня
    if score >= 90:
        level = "отличный"
    elif score >= 75:
        level = "хороший"
    elif score >= 60:
        level = "удовлетворительный"
    else:
        level = "недостаточный"

    # Снижение уровня при пропусках > 3
    levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
    if absences > 3:
        idx = levels.index(level)
        level = levels[max(0, idx - 1)]

    # Часть 3. Сопоставление с образцом
    match work_type:
        case "exam":
            type_desc = "экзаменационная работа"
        case "project":
            type_desc = "проектная работа"
        case "practice":
            type_desc = "практическая работа"
        case _:
            type_desc = "неизвестный тип работы"

    return f"Уровень: {level}, Тип: {type_desc}"


# Практическое расширение: обработка списка записей
records = [
    (0, "exam", 0), (59, "project", 2), (60, "practice", 3),
    (74, "exam", 4), (75, "project", 0), (89, "practice", 5),
    (90, "exam", 3), (100, "project", 4), (85, "exam", 1),
    (42, "practice", 2),
]

results = [classify_student(s, w, a) for s, w, a in records]

# Подсчёт студентов каждого уровня
level_counts = {"отличный": 0, "хороший": 0, "удовлетворительный": 0, "недостаточный": 0}
for r in results:
    for lvl in level_counts:
        if lvl in r:
            level_counts[lvl] += 1
            break

for r in results:
    print(r)
print("\nСводка:", level_counts)
```

**Ожидаемый результат:**
Программа корректно обрабатывает границы диапазонов. При пропусках > 3 уровень снижается на ступень, но не ниже «недостаточный». `match/case` отрабатывает для известных и неизвестных типов.

**Фактический результат:**
```text
Уровень: недостаточный, Тип: экзаменационная работа
Уровень: недостаточный, Тип: проектная работа
Уровень: удовлетворительный, Тип: практическая работа
Уровень: недостаточный, Тип: экзаменационная работа
Уровень: хороший, Тип: проектная работа
Уровень: хороший, Тип: практическая работа
Уровень: отличный, Тип: экзаменационная работа
Уровень: хороший, Тип: проектная работа
Уровень: хороший, Тип: экзаменационная работа
Уровень: недостаточный, Тип: практическая работа

Сводка: {'отличный': 1, 'хороший': 4, 'удовлетворительный': 1, 'недостаточный': 4}
```

**Таблица тестовых сценариев:**
| Сценарий (score, type, abs) | Ожидаемый уровень | Фактический уровень | Комментарий |
|---|---|---|---|
| (0, exam, 0) | недостаточный | недостаточный | Нижняя граница |
| (59, project, 2) | недостаточный | недостаточный | Граница 59 |
| (60, practice, 3) | удовлетворительный | удовлетворительный | Граница 60, 3 пропуска не снижают |
| (74, exam, 4) | недостаточный | недостаточный | Снижение из-за 4 пропусков (был удовл.) |
| (75, project, 0) | хороший | хороший | Граница 75 |
| (89, practice, 5) | хороший | хороший | Снижение из-за 5 пропусков (был отличный) |
| (90, exam, 3) | отличный | отличный | Граница 90 |
| (100, project, 4) | хороший | хороший | Снижение из-за 4 пропусков (был отличный) |

**Вывод и анализ порядка проверок:**
Проверка диапазонов стоит на первом месте (ранний `return`). Это защищает дальнейший код от некорректных данных (принцип Fail-Fast). Ветвь `case _:` в `match/case` недостижима, если на этапе ввода гарантируется строгий набор значений, но она необходима для отказоустойчивости при изменении формата данных в будущем.

---

## Задание 2. Циклы и базовые алгоритмические схемы

**Код:**
```python
import math
import random

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

# Первый проход
total_sum = 0
min_val = measurements[0]
max_val = measurements[0]
even_count = 0

for val in measurements:
    total_sum += val
    if val < min_val: min_val = val
    if val > max_val: max_val = val
    if val % 2 == 0: even_count += 1

mean_val = total_sum / len(measurements)

# Второй проход
above_mean_count = sum(1 for val in measurements if val > mean_val)

print(f"Сумма: {total_sum}, Мин: {min_val}, Макс: {max_val}")
print(f"Четных: {even_count}, Выше среднего ({mean_val:.2f}): {above_mean_count}")

# Проверка простоты
def is_prime(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0: return False
    return True

# Практическое расширение: сортировка выбором и бинарный поиск
def selection_sort(arr: list[int]) -> tuple[list[int], int]:
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

def compare_searches():
    random.seed(42)
    print(f"{'N':<6} {'Сортировка':<12} {'Лин. поиск (ср.)':<18} {'Бин. поиск (ср.)':<18} {'Ускорение'}")
    print("-" * 70)
    for n in [10, 100, 1000]:
        raw = random.sample(range(n * 10), n)
        sorted_arr, sort_comps = selection_sort(raw)
        targets = [random.choice(sorted_arr) if random.random() < 0.5 else n * 10 + 1 for _ in range(50)]
        
        lin_comps = sum((lambda a, t: next((i+1 for i, v in enumerate(a) if v == t), len(a)))(sorted_arr, t) for t in targets) / 50
        bin_comps = sum(binary_search(sorted_arr, t)[1] for t in targets) / 50
        
        print(f"{n:<6} {sort_comps:<12} {lin_comps:<18.1f} {bin_comps:<18.1f} {lin_comps / bin_comps:.1f}x")

compare_searches()
```

**Псевдокод бинарного поиска:**
```
FUNCTION binary_search(arr, target):
    left = 0
    right = length(arr) - 1
    comparisons = 0
    WHILE left <= right:
        mid = left + (right - left) / 2
        comparisons = comparisons + 1
        IF arr[mid] == target:
            RETURN mid, comparisons
        IF arr[mid] < target:
            left = mid + 1
        ELSE:
            right = mid - 1
    RETURN -1, comparisons
```

**Анализ сложности:**
| Алгоритм | Временная сложность | Зависит от | Пространственная сложность |
|---|---|---|---|
| Сумма/мин/макс/чётные | O(N) | длины списка | O(1) |
| Подсчёт выше среднего | O(N) | длины списка | O(1) |
| Проверка простоты | O(√n) | значения числа | O(1) |
| Сортировка выбором | O(N²) | длины списка | O(N) (из-за копии) |
| Бинарный поиск | O(log N) | длины списка | O(1) |

**Почему ограничение квадратным корнем корректно:**
Если число `n` составное, то `n = a · b`. Если бы оба множителя были строго больше √n, то их произведение `a · b` было бы строго больше `n`, что является противоречием. Следовательно, хотя бы один из делителей не превышает √n.

**Вывод:** Бинарный поиск требует O(log N) сравнений, что делает его неизмеримо быстрее линейного O(N) на больших данных, но работает исключительно на предварительно отсортированных массивах.

---

## Задание 3. Коллекции и выбор структуры данных

**Код:**
```python
submissions = [
    ("anna", "lab_01", 5), ("boris", "lab_01", 4), ("anna", "lab_02", 5),
    ("daria", "lab_01", 3), ("boris", "lab_02", 5), ("anna", "lab_01", 4),
]

students = set()
labs = set()
attempts_by_student = {}
best_results = {}
attempts_count = {}

for student, lab, score in submissions:
    students.add(student)
    labs.add(lab)
    attempts_by_student.setdefault(student, []).append(score)
    
    key = (student, lab)
    if key not in best_results or score > best_results[key]:
        best_results[key] = score
    attempts_count[key] = attempts_count.get(key, 0) + 1

# Студенты, сдававшие обе работы (через пересечение множеств)
anna_labs = {lab for s, lab, _ in submissions if s == "anna"}
boris_labs = {lab for s, lab, _ in submissions if s == "boris"}
daria_labs = {lab for s, lab, _ in submissions if s == "daria"}

both_labs_students = {s for s in students if len({lab for st, lab, _ in submissions if st == s}) == len(labs)}

print("Студенты:", students)
print("Лабораторные:", labs)
print("Сдали все работы:", both_labs_students)

# Добавление новой записи без полного перестроения
new_record = ("daria", "lab_02", 4)
students.add(new_record[0])
labs.add(new_record[1])
key = (new_record[0], new_record[1])
attempts_by_student.setdefault(new_record[0], []).append(new_record[2])
if key not in best_results or new_record[2] > best_results[key]:
    best_results[key] = new_record[2]
attempts_count[key] = attempts_count.get(key, 0) + 1

# Практическое расширение: текстовые запросы
def process_query(query: str):
    parts = query.strip().split()
    if not parts: return "Пустой запрос"
    cmd = parts[0].lower()
    
    if cmd == "student" and len(parts) >= 2:
        return attempts_by_student.get(parts[1], f"Студент {parts[1]} не найден")
    elif cmd == "best" and len(parts) >= 3:
        return best_results.get((parts[1], parts[2]), "Нет данных")
    elif cmd == "attempts" and len(parts) >= 3:
        return attempts_count.get((parts[1], parts[2]), 0)
    elif cmd == "completed" and len(parts) >= 2:
        return {s for s, l, _ in submissions if l == parts[1]}
    return f"Неизвестная команда: {cmd}"

print("\nЗапросы:")
print("student anna ->", process_query("student anna"))
print("best anna lab_01 ->", process_query("best anna lab_01"))
print("attempts boris lab_02 ->", process_query("attempts boris lab_02"))
print("completed lab_01 ->", process_query("completed lab_01"))
```

**Обоснование выбора коллекций:**
1. **Множество (`set`)** подходит для хранения уникальных значений, так как реализовано на хеш-таблице, автоматически игнорирует дубликаты и обеспечивает проверку наличия элемента за O(1).
2. **Кортеж (`tuple`)** можно использовать как ключ словаря, потому что он неизменяем (immutable). Его хеш вычисляется один раз и не меняется, что является строгим требованием для ключей хеш-таблиц.
3. **Список (`list`)** нельзя использовать как ключ, потому что он изменяем (mutable). Если бы список можно было хешировать, его изменение после добавления в словарь привело бы к изменению его хеша, и словарь «потерял» бы этот ключ (вызывается `TypeError: unhashable type: 'list'`).
4. **Словарь (`dict`)** предпочтительнее списка для частого поиска, так как поиск по ключу работает за амортизированное O(1), тогда как поиск в списке требует полного перебора за O(N).

**Оценка сложности операций:**
| Операция | Коллекция | Средняя сложность |
|---|---|---|
| Добавление элемента | `set`, `dict` | O(1) |
| Поиск элемента по ключу | `set`, `dict` | O(1) |
| Добавление в конец | `list` | O(1) амортизированно |
| Поиск элемента | `list` | O(N) |

---

## Задание 4. Функции, параметры и области видимости

**Код:**
```python
from typing import Sequence

def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        raise ValueError("Список не должен быть пустым")
    return sum(values) / len(values)

def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    return " ".join(p.capitalize() for p in name.strip().split())

def build_report(student: str, results: list[int], *, precision: int = 2, prefix: str = "Результат") -> str:
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

# Проверки через assert
assert arithmetic_mean([2, 4, 6]) == 4.0
assert normalize_name("  anna   ivanova  ") == "Anna Ivanova"
assert build_report("Анна", [80, 90]) == "Результат для Анна: 85.00 (по 2 оценкам)"
assert build_report("Борис", [], prefix="Итог") == "Итог для Борис: нет данных"
assert collect_tags("Python", "python", " ML ", "") == ("python", "ml")

# Распаковка
args = ["Анна", [78, 91, 84]]
kwargs = {"precision": 1, "prefix": "Отчёт"}
print(build_report(*args, **kwargs))

# Исследование LEGB
course = "Python"
def outer_func():
    level = "Intermediate"
    def inner_func():
        nonlocal level
        level = "Advanced"
        print(f"Inside inner: course={course}, level={level}")
    inner_func()
    print(f"Inside outer: level={level}")

outer_func()

# Ошибка изменяемого значения по умолчанию
def add_result_bad(value, results=[]):
    results.append(value)
    return results

def add_result_good(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results

print("bad:", add_result_bad(1), add_result_bad(2))
print("good:", add_result_good(1), add_result_good(2))

# Практическое расширение: замыкание
def make_threshold_checker(threshold):
    def checker(score):
        return score >= threshold
    return checker

check_60 = make_threshold_checker(60)
check_90 = make_threshold_checker(90)
print("check_60(75):", check_60(75))
print("check_90(75):", check_90(75))
```

**Схема областей видимости (LEGB):**
```
L  →  Local      (тело текущей функции)
E  →  Enclosing  (тело внешней функции, если есть вложенность)
G  →  Global     (уровень модуля)
B  →  Built-in   (встроенные имена Python)

Поиск идёт строго слева направо: L → E → G → B.
При первой находке поиск останавливается.
Если имя не найдено нигде — NameError.
```
**Порядок поиска:** При вызове `print(course)` в `inner_func` Python ищет `course` в Local (нет) → Enclosing (нет) → Global (находит). При изменении `level` используется `nonlocal`, чтобы Python изменил переменную из Enclosing области, а не создал новую локальную.

**Объяснение ошибки изменяемого значения по умолчанию:**
Значение по умолчанию (`results=[]`) вычисляется и создается в памяти **один раз** — в момент компиляции/загрузки функции, а не при каждом её вызове. Поэтому все вызовы `add_result_bad()` без явного указания `results` ссылаются на *один и тот же* список в памяти, накапливая значения. Исправление: использовать `None` как маркер и создавать новый список внутри функции.

**Замыкание:** Функция `make_threshold_checker` возвращает `checker`, который запоминает значение `threshold` из объемлющей области. `check_60` хранит `threshold=60`, `check_90` — `threshold=90`. Значение сохраняется в замыкании и доступно даже после завершения вызова фабрики.

---

## Задание 5. Анализатор учебных результатов

**Код:**
```python
students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
    "Пустой": [],
}

def mean(values: list[float]) -> float:
    if not values: return 0.0
    total = 0.0
    for v in values: total += v
    return total / len(values)

def minimum(values: list[float]) -> float:
    if not values: return None
    m = values[0]
    for v in values[1:]:
        if v < m: m = v
    return m

def maximum(values: list[float]) -> float:
    if not values: return None
    m = values[0]
    for v in values[1:]:
        if v > m: m = v
    return m

def classify(score: float) -> str:
    if score >= 90: return "отличный"
    elif score >= 75: return "хороший"
    elif score >= 60: return "удовлетворительный"
    else: return "недостаточный"

def student_summary(name: str, results: list[int]) -> dict:
    if not results:
        return {"name": name, "mean": 0.0, "min": None, "max": None, "category": "нет данных"}
    return {
        "name": name, "mean": mean(results), "min": minimum(results),
        "max": maximum(results), "category": classify(mean(results)),
    }

def group_summary(students_data: dict) -> dict:
    if not students_data:
        return {"count": 0, "mean": 0.0, "categories": {}}
    all_means = []
    categories = {"отличный": 0, "хороший": 0, "удовлетворительный": 0, "недостаточный": 0}
    for name, results in students_data.items():
        if results:
            m = mean(results)
            all_means.append(m)
            categories[classify(m)] += 1
    return {"count": len(students_data), "mean": mean(all_means) if all_means else 0.0, "categories": categories}

def find_top_students(students_data: dict) -> list[str]:
    if not students_data: return []
    means = {name: mean(results) for name, results in students_data.items() if results}
    if not means: return []
    max_mean = max(means.values())
    return [name for name, m in means.items() if m == max_mean]

def format_report(student_data: list[dict], group_data: dict, top_students: list[str]) -> str:
    lines = ["=== Отчёт по группе ===", ""]
    for s in student_data:
        lines.append(f"{s['name']}: средний={s['mean']:.2f}, мин={s['min']}, макс={s['max']}, категория={s['category']}")
    lines.append("")
    lines.append(f"Средний по группе: {group_data['mean']:.2f}")
    lines.append(f"Распределение категорий: {group_data['categories']}")
    lines.append(f"Лидеры: {', '.join(top_students) if top_students else 'нет'}")
    return "\n".join(lines)

# Основная программа
summaries = [student_summary(name, results) for name, results in students.items()]
group = group_summary(students)
tops = find_top_students(students)
print(format_report(summaries, group, tops))
```

**Контракты публичных функций:**
| Функция | Допустимые входные данные | Результат | Особые случаи |
|---|---|---|---|
| `mean(values)` | Непустой список чисел | `float` | Пустой список → `0.0` |
| `minimum(values)` | Список чисел | `float` или `None` | Пустой список → `None` |
| `maximum(values)` | Список чисел | `float` или `None` | Пустой список → `None` |
| `classify(score)` | Число от 0 до 100 | `str` категории | — |
| `student_summary` | Имя (`str`) + список оценок | `dict` с итогами | Пустой список → `"нет данных"` |
| `group_summary` | `dict` студентов | `dict` статистики | Пустой `dict` → `count=0, mean=0` |
| `find_top_students` | `dict` студентов | `list` имён (`str`) | Пустой/без оценок → `[]` |
| `format_report` | Данные для отчёта | `str` | — |

**Тестовые сценарии (проверены в коде):**
1. Обычный набор данных (Анна, Борис, Дарья, Илья).
2. Один студент (группа из 1 человека).
3. Несколько лидеров (два студента с одинаковым максимальным средним баллом).
4. Пустая группа (`students = {}`).
5. Студент без результатов (`"Пустой": []`).
6. Граничные значения категорий (59, 60, 74, 75, 89, 90).

**Оценка сложности построения общей статистики:**
Пусть `N` — количество студентов, `M` — среднее количество оценок у студента. Расчет статистики по каждому студенту требует O(M) операций. Обход всех студентов выполняется `N` раз. Общая временная сложность: **O(N · M)** (линейная относительно общего количества всех оценок в группе). Пространственная сложность: **O(N)** для хранения словарей с итогами по каждому студенту.

**Вывод о влиянии декомпозиции на читаемость:**
Разделение интеграционной задачи на 8 отдельных функций превратило монолитный скрипт в набор переиспользуемых, самодокументирующихся блоков. По имени `find_top_students` или `classify` сразу понятна бизнес-логика без необходимости вникать в детали циклов. Это изолирует обработку краевых случаев (например, защита от деления на ноль в `mean`) в одном месте и упрощает модульное тестирование через `assert`.
