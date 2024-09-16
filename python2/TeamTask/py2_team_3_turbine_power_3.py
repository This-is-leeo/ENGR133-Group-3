from math import pi

def turbine_power(bladeLength, airDensity, windVelocity, powerCoeffcient):
    area = pi * bladeLength ** 2
    if windVelocity > 20:
        print("Error, velocity is too high, no power generated")
        return 0
    elif windVelocity < 4:
        print("Error, velocity is too low, no power generated")
        return 0
    return 0.5*airDensity*area*(windVelocity ** 3)*powerCoeffcient

