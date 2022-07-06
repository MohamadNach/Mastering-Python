"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
String letters are case-sensitive.
"""


def count_substring(string, sub_string):
    my_string = ""
    count = 0
    sub = ""

    for i in range(0, len(string)):  # ABCDCDC
        j = 0
        if sub_string[j] == string[i]:
            for j in range(0, len(sub_string)):     # CDC
                my_string = string[i:]
                if len(my_string) >= len(sub_string):
                    if sub_string[j] == my_string[j]:
                        sub += my_string[j]
                        if sub == sub_string:
                            count += 1
                    else:
                        break

                else:
                    break
            sub = ""
    return count


original_string = input().strip()
substring = input().strip()
count = count_substring(original_string, substring)
print(count)
