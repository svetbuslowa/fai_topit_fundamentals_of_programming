student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print("Первый символ:", student[0])
print("Последний символ:", student[-1])

print("Имя:", student[:4])
print("Фамилия:", student[5:])

print("Верхний:", student.upper())
print("Нижний:", student.lower())

initials = student[0] + "." + student[5] + "."
print("Инициалы:", initials)

print("Обратный курс:", course[::-1])

percent = completed / total * 100
result_1 = "%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
print("Способ 1 (%):", result_1)
result_2 = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent)
print("Способ 2 (.format()):", result_2)
result_3 = f"{student} — {course}: {completed}/{total} ({percent:.1f}%)"
print("Способ 3 (f-строка):", result_3)

symbol = "Я"
print("Символ:", symbol)
print("ord('Я') =", ord(symbol))
print("chr(1071) =", chr(1071))
encoded = symbol.encode("utf-8")
print("encode('utf-8') =", encoded)
print("len('Я') =", len(symbol))
print("len(encoded) =", len(encoded))

# student[0] = "0"