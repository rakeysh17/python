#!/opt/bin/python
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd,alice,tyler]
# Add your function below!

#Function to calculate average of any numeric list

def average(numbers):
  total = 0
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)

#Function to calculate weighted averages

def get_average(student):
  homeworks = average(student["homework"])
  quizzess = average(student["quizzes"])
  testss = average(student["tests"])
  return 0.1 * homeworks + 0.3 * quizzess + \
0.6 * testss

#Function to calculate letter grade

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif 90 > score >= 80:
    return "B"
  elif 80 > score >= 70:
    return "C"
  elif 70 > score >= 60:
    return "D"
  else:
    return "F"

#Function to calculate class average

def get_class_average(class_list):
  results = []
  for i in class_list:
    results.append(get_average(i))
  return average(results)

#Calling and printing the class average as well as letter grade

print get_class_average(students)
print get_letter_grade(get_class_average(students))
