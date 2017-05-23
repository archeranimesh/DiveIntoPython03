import fractions
from boolcontext import is_it_true


print("Check if number 1 is true, is_it_true(1): ", is_it_true(1))
print("-1: is_it_true(-1): ", is_it_true(-1))
print("0: is_it_true(0): ", is_it_true(0))
print("0.1: is_it_true(0.1): ", is_it_true(0.1))
print("0.0: is_it_true(0.0): ", is_it_true(0.0))
print("0.1: is_it_true(0.1): ", is_it_true(0.1))
print("is_it_true(fractions.Fraction(1,2)): ", is_it_true(fractions.Fraction(1 , 2)))
print("is_it_true(fractions.Fraction(0,2)): ", is_it_true(fractions.Fraction(0 , 2)))
