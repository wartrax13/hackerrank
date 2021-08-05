if __name__ == '__main__':
    grade = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade.append([name, score])
    sorted_1 = sorted(list(set([x[1] for x in grade])))

    second_list = sorted_1[1]

    low_final_list = []
    for student in grade:
        if second_list == student[1]:
            low_final_list.append(student[0])

    for student in sorted(low_final_list):
        print(student)

    '''5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39'''
