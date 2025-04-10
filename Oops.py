class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display(self):
        print(f"{self.name} Balance: ₹{self.balance}")

acc = BankAccount("Alice")
acc.deposit(1000)
acc.withdraw(500)
acc.display()




class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}")

student1 = Student("John", 101, "A")
student1.display()




class LibraryItem:
    def __init__(self, title):
        self.title = title

    def display(self):
        print("Title:", self.title)

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display(self):
        super().display()
        print("Author:", self.author)

book = Book("Python Basics", "John Doe")
book.display()




class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

for animal in (Dog(), Cat()):
    animal.speak()




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name}'s Salary: ₹{self.salary}")

emp = Employee("Ram", 50000)
emp.display()
