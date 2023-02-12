def print_students(students, a):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        if sum(student["marks"])/3 > a:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
                  str(student["marks"]).ljust(20))


groupmates = [
    {
        "name": "Александр",
        "surname": "Плешаков",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Сахарова",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Арсений",
        "surname": "Смирнов",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Красько",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Александр",
        "surname": "Чернов",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [5, 4, 5]
    }
]
a = float(input())
print_students(groupmates, a)
