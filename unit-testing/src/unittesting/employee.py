import requests


class Employee:
    bonus_amount = 20000

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_bonus(self):
        self.pay = self.pay + self.bonus_amount

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response'
