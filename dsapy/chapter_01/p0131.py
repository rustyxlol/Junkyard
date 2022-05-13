"""
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible
"""
CURRENCY = (100, 50, 20, 10, 5, 2, 1)


def make_change(charged, given):
    total = given - charged
    bills = {i: 0 for i in CURRENCY}

    for i in CURRENCY:
        if total // i != 0:
            bills[i] += (total // i)
            total -= (i * (total//i))

    for bill, cnt in bills.items():
        if cnt == 0:
            continue
        print(f"{cnt} {bill}")


if __name__ == "__main__":
    make_change(1, 100)
