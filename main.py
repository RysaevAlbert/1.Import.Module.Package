
from application import salary
from application.db import people
from datetime import date

if __name__ == '__main__':
    print(f'Сегодняшняя дата:', date.today())
    salary.calculate_salary()
    people.get_employees()