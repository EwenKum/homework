
rating = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(sorted(students))
student_total_1 = sum(grades[0]) / 5
student_total_2 = sum(grades[1]) / 4
student_total_3 = sum(grades[2]) / 4
student_total_4 = sum(grades[3]) / 3
student_total_5 = sum(grades[4]) / 5
students_set = [student_total_1, student_total_2, student_total_3, student_total_4, student_total_5]
rating.update({students_list[0]: students_set[0],
               students_list[1]: students_set[1],
               students_list[2]: students_set[2],
               students_list[3]: students_set[3],
               students_list[4]: students_set[4]
               })
print(rating)


