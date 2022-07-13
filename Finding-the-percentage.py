"""
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""
student_marks = {}


def number_of_student():
    """
    This function will ask the user to enter the number of student
    The function will also check if the number between 2 -10 
    """
    while True:
        try:
            # take input from user
            num = int(input())
            # if input between 2 - 10 accept it and go to check it.
            if 2 <= num <= 10:
                break
            # or rais an error and ask for input again
            else:
                raise ValueError
        # error containt
        except ValueError:
            print("Number must be an integer between 2 and 10.")
    # finaly return the input to use it as student number.
    return num


def read_student_info(student_numbers):
    """
    This function will as user to enter student name and marks
    inside the function, check_marks_numbers function will be called to check numbers validation.
    """
    right_input = 0
    # take the student name and marks
    while right_input < student_numbers:

        # (name) take the first word as name of the student
        # (*line) unpacked the rest of line as student marks
        name, *line = input().split()

        # save all marks as a list
        scores = list(map(float, line))

        # if student marks == 3 save it to student
        right_input = check_marks_numbers(right_input, name, scores)


def check_marks_numbers(right_input, name, scores):
    """
    This function will check if marks numbers == 3
    Every mark should be between 0 - 100.
    """
    right_mark = 0
    # if student marks == 3 save it to student
    if len(scores) == 3:
        right_mark = 0
        for mark in scores:
            if 0 <= mark <= 100:
                right_mark += 1

            else:
                print(
                    f"{mark} was not correct. please enter number between 0 - 100.")
        if right_mark == 3:
            right_input += 1
            student_marks[name] = scores
        student_marks[name] = scores
    # or ask the user to input the right number of marks again
    else:
        print(f"{name} marks was not correct. please enter 3 marks.")
        while True:
            name, *line = input().split()
            scores = list(map(float, line))

            if len(scores) == 3:
                right_mark = 0
                for mark in scores:
                    if 0 <= mark <= 100:
                        right_mark += 1

                    else:
                        print(
                            f"{mark} was not correct. please enter number between 0 - 100.")
                if right_mark == 3:
                    right_input += 1
                    student_marks[name] = scores
                    break
            else:
                print(f"{name} marks was not correct. please enter 3 marks.")
    return right_input


###  Main Programme ###
student_numbers = number_of_student()
read_student_info(student_numbers)
query_name = input()
avrage = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{avrage:.2f}")
