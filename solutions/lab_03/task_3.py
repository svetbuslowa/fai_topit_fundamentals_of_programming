submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

# Построение структур данных
students = set()
labs = set()
attempts_by_student: dict[str, list[int]] = {}
best_results: dict[tuple[str, str], int] = {}
attempts_count: dict[tuple[str, str], int] = {}

for student, lab, score in submissions:
    students.add(student)
    labs.add(lab)

    # Список попыток студента
    attempts_by_student.setdefault(student, []).append(score)

    # Лучшие результаты по паре (student, lab)
    key = (student, lab)
    if key not in best_results or score > best_results[key]:
        best_results[key] = score

    # Количество попыток по паре
    attempts_count[key] = attempts_count.get(key, 0) + 1

print("=== Построенные структуры ===")
print(f"Студенты: {students}")
print(f"Лабораторные: {labs}")
print(f"Попытки по студентам: {attempts_by_student}")
print(f"Лучшие результаты: {best_results}")
print(f"Количество попыток: {attempts_count}")

# Студенты, сдававшие обе работы (через операции над множествами)
students_by_lab: dict[str, set[str]] = {}
for student, lab, _ in submissions:
    students_by_lab.setdefault(lab, set()).add(student)

# Пересечение множеств студентов по всем лабам
all_students_sets = list(students_by_lab.values())
students_with_all_labs = all_students_sets[0]
for s in all_students_sets[1:]:
    students_with_all_labs = students_with_all_labs & s

print(f"\nСтуденты, сдававшие все работы: {students_with_all_labs}")

# Добавление новой записи без полного перестроения
new_record = ("daria", "lab_02", 4)
students.add(new_record[0])
labs.add(new_record[1])

student, lab, score = new_record
attempts_by_student.setdefault(student, []).append(score)

key = (student, lab)
if key not in best_results or score > best_results[key]:
    best_results[key] = score
attempts_count[key] = attempts_count.get(key, 0) + 1

print(f"\nПосле добавления {new_record}:")
print(f"  Попытки {student}: {attempts_by_student[student]}")
print(f"  Лучший {key}: {best_results[key]}")
print(f"  Попыток {key}: {attempts_count[key]}")

# Практическое расширение: текстовые запросы
def process_query(query: str) -> str:
    """Обрабатывает текстовый запрос к данным."""
    parts = query.strip().split()
    if not parts:
        return "Пустой запрос"

    cmd = parts[0].lower()

    if cmd == "student" and len(parts) >= 2:
        name = parts[1]
        return str(attempts_by_student.get(name, f"Студент {name} не найден"))

    elif cmd == "best" and len(parts) >= 3:
        key = (parts[1], parts[2])
        return str(best_results.get(key, f"Нет данных по {key}"))

    elif cmd == "attempts" and len(parts) >= 3:
        key = (parts[1], parts[2])
        return str(attempts_count.get(key, 0))

    elif cmd == "completed" and len(parts) >= 2:
        lab = parts[1]
        return str(students_by_lab.get(lab, set()))

    else:
        return f"Неизвестная команда: {cmd}"


print("\n=== Текстовые запросы ===")
queries = [
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01",
    "unknown cmd",
    "student nobody",
]
for q in queries:
    print(f"  {q} -> {process_query(q)}")
