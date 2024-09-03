

import fractions

float_value = -5.422

fraction_object = fractions.Fraction.from_float(float_value)

new_fraction_object = fraction_object.limit_denominator(max_denominator=1432)

print("Fraction without limit_denominator(1432) for %f - %s" % (float_value, fraction_object))
print("Fraction with limit_denominator(1432) for %f - %s" % (float_value, new_fraction_object))