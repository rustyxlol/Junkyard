import unittest
from unittest.mock import patch
from unittesting.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.e_1 = Employee('First', 'Last', 50000)
        self.e_2 = Employee('Sue', 'Last', 60000)

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.e_1.email, 'FirstLast@email.com')
        self.assertEqual(self.e_2.email, 'SueLast@email.com')

        self.e_1.first = 'Second'
        self.e_2.first = 'Simon'

        self.assertEqual(self.e_1.email, 'SecondLast@email.com')
        self.assertEqual(self.e_2.email, 'SimonLast@email.com')

    def test_fullname(self):
        self.assertEqual(self.e_1.fullname, 'First Last')
        self.assertEqual(self.e_2.fullname, 'Sue Last')

        self.e_1.first = 'Second'
        self.e_2.first = 'Simon'

        self.assertEqual(self.e_1.fullname, 'Second Last')
        self.assertEqual(self.e_2.fullname, 'Simon Last')

    def test_apply_bonus(self):
        self.assertEqual(self.e_1.pay, 50000)
        self.assertEqual(self.e_2.pay, 60000)

        self.e_1.apply_bonus()
        self.e_2.bonus_amount = 555
        self.e_2.apply_bonus()

        self.assertEqual(self.e_1.pay, 70000)
        self.assertEqual(self.e_2.pay, 60555)


if __name__ == "__main__":
    unittest.main()
