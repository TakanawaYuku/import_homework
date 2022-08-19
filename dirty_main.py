from application.salary import *
from application.db.people import *
import datetime as dt

if __name__ == '__main__':
    print(f'{dt.date.today()}')
    calculate_salary()
    get_employees()