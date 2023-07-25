homework_grades_str = '55, 85, 75, 45, 90, 30, 90, 60, 0'
quiz_grades_str = '100, 100, 100, 100, 100, 100, 100, 90, 100'
group_work_grades_str = '100, 100, 100, 100, 100, 100, 100, 50, 50, 50'
final_test_grade = 75

def grade_calculator(homework_grades_str, quiz_grades_str, group_work_grades_str, final_test_grade):
  # Convert the input strings to lists of grades
  homework_grades = [float(grade) for grade in homework_grades_str.split(',')]
  quiz_grades = [float(grade) for grade in quiz_grades_str.split(',')]
  group_work_grades = [float(grade) for grade in group_work_grades_str.split(',')]

# Sort the homework grades in ascending order
  homework_grades.sort()

  # Remove the two lowest homework grades
  homework_grades = homework_grades[2:]

  # Calculate the total homework grade by taking the sum of the remaining grades
  # and multiplying it by the weight (15%)
  total_homework_grade = sum(homework_grades[:7])/7 * 0.15

#sort quiz grades in ascending order
  quiz_grades.sort()

  #remove the two lowest quiz grades
  quiz_grades = quiz_grades[2:]

  # Calculate the total quiz grade by taking the sum of the best 8 out of 10
  # quiz grades and multiplying it by the weight (15%)
  total_quiz_grade = sum(quiz_grades[:7])/7 * 0.15


  # Calculate the total group work grade by taking the sum of the best 8 out of 10
  # group work grades and multiplying it by the weight (10%)
  total_group_work_grade = sum(group_work_grades[:7])/7 * 0.1

#Final grade 
  finals_grade = final_test_grade * 0.6

  # Calculate the total grade
  total_grade = total_homework_grade + total_quiz_grade + total_group_work_grade + finals_grade

  # Calculate the remaining grade needed to achieve an overall grade of 80%
  remaining_grade = 80 - total_grade

  # Print the results
  print(f"TOTAL SCORE: {total_homework_grade:.2f}% + {total_quiz_grade:.2f}% + {total_group_work_grade:.2f}% + {finals_grade:.2f}%"  ' = '  f"{total_grade:.2f}%" )
  print(f"Total homework grade: {total_homework_grade:.2f}%")
  print(f"Total quiz grade: {total_quiz_grade:.2f}%")
  print(f"Total group work grade: {total_group_work_grade:.2f}%")
  print(f"final test grade: {finals_grade:.2f}%")
  
grade_calculator(homework_grades_str, quiz_grades_str, group_work_grades_str, final_test_grade)
