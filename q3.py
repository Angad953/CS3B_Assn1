# Foothill College
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 3
# Prepared by Viet Trinh
# Email: trinhviet@fhda.edu


# Implement your Employee class here
class Employee:
    def __init__(self, name='', number=''):
        self._name = name
        self._number = number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number


class ProductionWorker(Employee):
    def __init__(self, name='', number='', shift=1, hourly_pay_rate=0.0):
        super().__init__(name, number)
        self._shift = shift
        self._hourly_pay_rate = hourly_pay_rate

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, shift):
        if shift == 1 or shift == 2:
            self._shift = shift
        else:
            raise ValueError("Must be either a Day or Night Shift.")

    @property
    def hourly_pay_rate(self):
        return self._hourly_pay_rate

    @hourly_pay_rate.setter
    def hourly_pay_rate(self, rate):
        self._hourly_pay_rate = rate


def run():
    print("===== Question 3 =====")
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    shift = int(input("Enter the shift (1 for Day, 2 for Night): "))
    hourly_pay_rate = float(input("Enter the hourly pay rate: "))
    worker = ProductionWorker(name, number, shift, hourly_pay_rate)
    print("\nEmployee Information:")
    print(f"Name: {worker.name}")
    print(f"Number: {worker.number}")
    print(f"Shift: {'Day' if worker.shift == 1 else 'Night'}")
    print(f"Hourly Pay Rate: ${worker.hourly_pay_rate:.2f}")
