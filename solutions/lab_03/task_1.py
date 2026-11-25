def classify_student(score: int, work_type: str, absences: int) -> str:
    """Классифицирует результат студента с учётом пропусков."""
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


# Часть 4. Тестовые сценарии (граничные значения)
test_cases = [
    (0, "exam", 0),
    (59, "project", 2),
    (60, "practice", 3),
    (74, "exam", 4),
    (75, "project", 0),
    (89, "practice", 5),
    (90, "exam", 3),
    (100, "project", 4),
]

print("=== Тестовые сценарии ===")
for score, work_type, absences in test_cases:
    print(f"({score}, {work_type}, {absences}) -> {classify_student(score, work_type, absences)}")


# Практическое расширение: обработка списка из 10+ записей
records = [
    (0, "exam", 0),
    (59, "project", 2),
    (60, "practice", 3),
    (74, "exam", 4),
    (75, "project", 0),
    (89, "practice", 5),
    (90, "exam", 3),
    (100, "project", 4),
    (85, "exam", 1),
    (42, "practice", 2),
]

# Исходные данные не изменяем — используем for по списку
results = []
for score, work_type, absences in records:
    results.append(classify_student(score, work_type, absences))

# Подсчёт студентов каждого уровня
level_counts = {
    "отличный": 0,
    "хороший": 0,
    "удовлетворительный": 0,
    "недостаточный": 0,
}
for result in results:
    for level_name in level_counts:
        if level_name in result:
            level_counts[level_name] += 1
            break

print("\n=== Индивидуальные результаты ===")
for result in results:
    print(result)

print("\n=== Итоговая сводка ===")
for level_name, count in level_counts.items():
    print(f"  {level_name}: {count}")
