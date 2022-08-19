import application.salary as calc
import application.db.people as empl
import datetime as dt

if __name__ == '__main__':
    print(f'{dt.date.today()}')
    calc.calculate_salary()
    empl.get_employees()
