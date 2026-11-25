students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}


def mean(values: list[float]) -> float:
    """Среднее значение. Для пустого списка возвращает 0.0."""
    if not values:
        return 0.0
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def minimum(values: list[float]) -> float:
    """Минимум без использования min()."""
    if not values:
        return None
    m = values[0]
    for v in values[1:]:
        if v < m:
            m = v
    return m


def maximum(values: list[float]) -> float:
    """Максимум без использования max()."""
    if not values:
        return None
    m = values[0]
    for v in values[1:]:
        if v > m:
            m = v
    return m


def classify(score: float) -> str:
    """Текстовая категория результата."""
    if score >= 90:
        return "отличный"
    elif score >= 75:
        return "хороший"
    elif score >= 60:
        return "удовлетворительный"
    else:
        return "недостаточный"


def student_summary(name: str, results: list[int]) -> dict:
    """Словарь с итогами одного студента."""
    if not results:
        return {
            "name": name,
            "mean": 0.0,
            "min": None,
            "max": None,
            "category": "нет данных",
        }
    return {
        "name": name,
        "mean": mean(results),
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(mean(results)),
    }


def group_summary(students_data: dict) -> dict:
    """Общая статистика группы."""
    if not students_data:
        return {"count": 0, "mean": 0.0, "categories": {}}

    all_means = []
    categories = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
    }

    for name, results in students_data.items():
        if results:
            m = mean(results)
            all_means.append(m)
            categories[classify(m)] += 1

    return {
        "count": len(students_data),
        "mean": mean(all_means) if all_means else 0.0,
        "categories": categories,
    }


def find_top_students(students_data: dict) -> list[str]:
    """Список студентов с наибольшим средним результатом."""
    if not students_data:
        return []

    means = {
        name: mean(results)
        for name, results in students_data.items()
        if results
    }
    if not means:
        return []

    max_mean = max(means.values())
    return [name for name, m in means.items() if m == max_mean]


def format_report(student_data: list[dict], group_data: dict, top_students: list[str]) -> str:
    """Итоговый текстовый отчёт."""
    lines = ["=== Отчёт по группе ===", ""]
    for s in student_data:
        lines.append(
            f"{s['name']}: средний={s['mean']:.2f}, "
            f"мин={s['min']}, макс={s['max']}, "
            f"категория={s['category']}"
        )
    lines.append("")
    lines.append(f"Средний по группе: {group_data['mean']:.2f}")
    lines.append(f"Распределение категорий: {group_data['categories']}")
    lines.append(f"Лидеры: {', '.join(top_students) if top_students else 'нет'}")
    return "\n".join(lines)


# === Основная программа ===

summaries = [student_summary(name, results) for name, results in students.items()]
group = group_summary(students)
tops = find_top_students(students)
print(format_report(summaries, group, tops))


# === Проверка: 6 сценариев ===

print("\n=== Сценарий 1: обычный набор ===")
print(group_summary(students))

print("\n=== Сценарий 2: один студент ===")
print(group_summary({"Только один": [80, 90]}))

print("\n=== Сценарий 3: несколько лидеров ===")
print(find_top_students({"А": [90, 90], "Б": [90, 90], "В": [80]}))

print("\n=== Сценарий 4: пустая группа ===")
print(group_summary({}))

print("\n=== Сценарий 5: студент без результатов ===")
print(student_summary("Пустой", []))

print("\n=== Сценарий 6: граничные значения категорий ===")
for score in [59, 60, 74, 75, 89, 90]:
    print(f"  {score} -> {classify(score)}")


