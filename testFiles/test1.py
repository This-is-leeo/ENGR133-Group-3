import fractions

x = 0.0123124

y = fractions.Fraction.from_float(x)

newY = y.limit_denominator(20)

print(y)
print(newY)