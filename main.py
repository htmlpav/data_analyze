import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
import csv


def calculate_average(data, subject):
    average = 0
    sum = 0
    for mark in data:
        sum += int(mark[subject])
    return sum / len(data)


def best_student(data, common_keys):
    print("\nBest student:")

    student_marks = {}

    attendance = []
    marks = []

    max_score = 0
    best_index = 0

    for i in range(len(data)):
        total = 0

        for subject in common_keys:
            total += int(data[i][subject])

        student_marks[data[i]["name"]] = total

        attendance.append(int(data[i]["attendance"]))
        marks.append(total)

        if max_score < total:
            max_score = total
            best_index = i

    # Посещаемость ↔ баллы
    plt.scatter(attendance, marks)

    plt.title("Посещаемость ↔ Сумма баллов")
    plt.xlabel("Посещаемость (%)")
    plt.ylabel("Сумма баллов")
    plt.ylim(0, 500)

    plt.show()

    # Успеваемость студентов
    plt.bar(
        student_marks.keys(),
        student_marks.values()
    )

    plt.xlabel("Имя")
    plt.ylabel("Сумма баллов")
    plt.title("График успеваемости студентов")

    plt.ylim(0, 500)

    plt.show()

    print(data[best_index]["name"], max_score)
def worst_student(data, common_keys):
    print("\nWorst student:")
    sum = 0
    min = 1000
    nom = 0
    for i in range(len(data)):
        for subject in common_keys:
            sum += int(data[i][subject])
        # print(sum)
        if sum < min:
            min = sum
            nom = i
        sum = 0
    print(data[nom]["name"], min)

def graphic_attendance(data):
    dict = {}
    for i in range(len(data)):
        attendance = data[i]["attendance"]
        dict[data[i]["name"]] = int(attendance)
    # print(dict)
    plt.bar(
        dict.keys(),
        dict.values()
    )
    plt.title("График посещаемости")
    plt.xlabel("Имя")
    plt.ylabel("Посещаемость %")
    plt.ylim(0,100)
    plt.show()
def average_mark_on_each_subject(data, common_keys):
    print("\nAverage mark on each subject:")
    common_keys = common_keys.copy()
    common_keys.pop()

    dict = {}
    for subject in common_keys:
        ans = calculate_average(data, subject=subject)
        dict[subject] = ans
        print(subject, ans)

    max_key = max(dict, key=dict.get)
    min_key = min(dict, key=dict.get)
    print("\nBest subject:", max_key)
    print("Worst subject:", min_key)

    plt.bar(
        dict.keys(),
        dict.values()
    )

    plt.xlabel("Предмет")
    plt.ylabel("Средний балл")
    plt.title("Средний балл по предметам")

    plt.ylim(0, 100)

    plt.show()


def students_count(data):
    print("Кол-во студентов:")
    print(len(data))

def students_with_low_attendance(data):
    print("\nStudents with low attendance:")
    for i in range(len(data)):
        if int(data[i]["attendance"]) < 70:
            print(data[i]["name"], data[i]["attendance"])


with open("students.csv", "r", encoding="utf-8") as file:
    students = csv.DictReader(file)
    data = list(students)

    # for line in data:
    #     print(line)
common_keys = list(data[0].keys())
del common_keys[0]
students_count(data)
average_mark_on_each_subject(data, common_keys)
best_student(data, common_keys)
worst_student(data, common_keys)
students_with_low_attendance(data)
graphic_attendance(data)