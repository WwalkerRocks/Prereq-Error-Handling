# exceptions_user_division_calc_try_this.py

from microbit import *

sleep(1000)

print("Division Calculations")

while True:
    try:
        text = input("Enter numerator n: ")
        n = float(text)
    
        text = input("Enter denominator d: ")
        d = float(text)

        q = n / d

    except Exception as e:
        print("Exception = ", e)
        et = type(e)
        print("Exception type = ", et)

    else:
        print("Quotient q: ")
        print("q = n / d")
        print("  = ", n, " / ", d)
        print("  = ", q)

    finally:
        print("Try again!")
        print()
