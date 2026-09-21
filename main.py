import csv


def calculate_average(data, subject):
    average = 0
    sum = 0
    for mark in data:
        sum += int(mark[subject])
    return sum / len(data)


def best_student(data, common_keys):
    print("\nBest student:")
    marks = []
    sum = 0
    max = 0
    nom = 0
    for i in range(len(data)):
        for subject in common_keys:
            sum += int(data[i][subject])
        # print(sum)
        if max < sum:
            max = sum
            nom = i
        sum = 0
    print(data[nom]["name"], max)

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


def average_mark_on_each_subject(data, common_keys):
    print("\nAverage mark on each subject:")
    common_keys = common_keys.copy()
    common_keys.pop()
    # maxi = 0
    nom = 0
    i = 0
    dict = {}
    for subject in common_keys:
        ans = calculate_average(data, subject=subject)
        dict[subject] = ans
        print(subject, ans)
    max_key = max(dict, key=dict.get)
    min_key = min(dict, key=dict.get)
    print("\nBest subject:", max_key)
    print("Worst subject:", min_key)

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
