# class Book:

#     def __init__(self, title, author, pages, current_page=1):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = current_page
    
#     def turn_page(self):
#         self.current_page += 1

#     def turn_back_page(self):
#         self.current_page -= 1

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}"

#     def __len__(self):
#         return self.pages

# my_book = Book("A great book", "me", 198, 1)
# print(my_book)
# print(my_book.current_page)

# my_book.turn_back_page()
# print(my_book.current_page)

class Employee:

    def __init__(self, name, salary, phone_number, start_date) # -> (Int, ): There is a way here to set the Type of a variable at this level. Joy can't remember 
        self.name = name
        self.salary = salary
        self.phone_number = phone_number
        self.start_date = start_date

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

    def give_payrise(self, amount):
        self.salary = self.salary + amount

# employee_one = Employee("joy", "100k", 234234432, "01 Jan")
# print(employee_one.name)

employee_two = Employee("fran", 78000, "0407877363", "1st June 2020") # creates an employee. No output yet
print(employee_two.get_employment_details()) # gives output 

employee_two.give_payrise(50000)
print(employee_two.salary)