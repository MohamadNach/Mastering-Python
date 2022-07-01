"""
https://www.hackerrank.com/challenges/nested-list/problem
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""
# The first line contains an integer, "student_number" the number of students.
student_number = int(input())
temp_list = []  # temp_list to save all the second lowest scores.
student_list = []  # student_list to save all student names and grades.


def get_student_info():
    """
    This function will get the student name and grade from the user and save it in sub list
    """
    # The  subsequent lines describe each student over  lines.
    # - The first line contains a student's name.
    # - The second line contains their grade.
    student_name = str(input())
    student_grade = float(input())
    student_sub_list = [student_name, student_grade]
    return student_sub_list


def adding_student_info(student_sub_list):
    """
    This function will add sub list of student informatio to the main list 
    """
    student_list.append(student_sub_list)
    return student_list


def sorting_students_list(student_list):
    """
    This function will sort the students acording to their grades in the main list.
    """
    length = len(student_list)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if student_list[j][1] >= 0:
                if student_list[j][1] > student_list[j+1][1]:
                    temp = student_list[j]
                    student_list[j] = student_list[j+1]
                    student_list[j+1] = temp
            else:
                temp = student_list[j]
                student_list[j] = student_list[j+1]
                student_list[j+1] = temp
    return student_list


def check_second_lowest_number(student_list):
    """
    This function will search for all second lowest scores, and
    sort them alphapetical and then print them.
    """
    length = len(student_list)
    for i in range(0, length-1):
        for j in range(0, length-1):
            if student_list[j + 1][1] == student_list[i][1]:
                pass
            elif student_list[j+1][1] > student_list[j][1]:
                for x in range(0, length - 1):
                    if student_list[x+1][1] == student_list[j + 1][1]:
                        temp_list.append(student_list[x+1])
                temp = sorting_lowest_score_list(temp_list)
                printing_lowest_score_list(temp)
                break
            elif student_list[j + 1][1] == student_list[j][1]:
                temp_list.append(student_list[j])
                for x in range(0, length - 1):
                    if student_list[x+1][1] == student_list[j + 1][1]:
                        temp_list.append(student_list[x+1])
                temp = sorting_lowest_score_list(temp_list)
                printing_lowest_score_list(temp)
                break
            elif student_list[j][1] < 0:
                for x in range(0, length - 1):
                    if student_list[x+1][1] == student_list[j + 1][1]:
                        temp_list.append(student_list[x+1])
                temp = sorting_lowest_score_list(temp_list)
                printing_lowest_score_list(temp)
                break
            else:
                temp_list.append(student_list[j])
                temp = sorting_lowest_score_list(temp_list)
                printing_lowest_score_list(temp)
                break

        break
    return temp_list


def sorting_lowest_score_list(temp_list):
    length = len(temp_list)
    for i in range(0, length):
        for j in range(0, length - 1):
            if temp_list[j][0] > temp_list[j+1][0]:
                temp = temp_list[j]
                temp_list[j] = temp_list[j+1]
                temp_list[j+1] = temp
    return temp_list


def printing_lowest_score_list(temp_list):
    length = len(temp_list)
    for i in range(0, length):
        for j in range(0, length):
            print(temp_list[j][0])
        break


################ Main While Loop ######################
while student_number > 0:

    student_sub_list = get_student_info()
    student_list = adding_student_info(student_sub_list)

    for student in student_list:
        student_number -= 1
        if student_number == 0:
            break
        student_sub_list = get_student_info()
        student_list = adding_student_info(student_sub_list)

student_list = sorting_students_list(student_list)
temp_list = check_second_lowest_number(student_list)
