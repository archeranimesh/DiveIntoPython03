import fractions

x = fractions.Fraction(1 , 3)
print('Faction x = ', x)
print('Multiplication of fraction: x * 2: ', x * 2)
print("Fractions will reduce to lowest fraction: fractions.Fraction(6 , 4): ", fractions.Fraction(6 , 4))
try:
    print("Fractions will no create a zero denominator fraction: fractions.Fraction(0,0): ", fractions.Fraction(1, 0))
except ZeroDivisionError as error:
    print("error: ", error)
