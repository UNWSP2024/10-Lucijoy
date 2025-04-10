# Author: Lucia Floan
# Date: Apr 4, 2025
# Title: Employee Class

# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.
class Employee:
  def __init__(self, name, id_number, department, job_title):
    self.name = name
    self.id_number = id_number
    self.department = department
    self.job_title = job_title

  def display_info(self):
    print('name:', self.name)
    print('ID number:', self.id_number)
    print('Department:', self.department)
    print('Job title:', self.job_title)
    print()
employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
employee2 = Employee('Mark Jones', 39119, 'IT', 'Programer')
employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

employee1.display_info()
employee2.display_info()

employee3.display_info()



