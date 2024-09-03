import math

a = 5

#calculation 2
#excel:
#Cell A1: =POWER($A$1,1/3)
b = a ** (1/3)
print(f"calculation 1: {b}")

#calculation 3 
#excel:
#Cell A3: =SIN(SQRT($A$2))
c = math.sin(math.sqrt(b))
print(f"calculation 2: {c}")

#calculation 4
#excel:
#Cell A4: =FLOOR(-90.5,1)
d = math.floor(-90.5)
print(d)

#calculation 5
#excel:
#Cell A5: Cell A5: =MOD(254, 66)
e = 254%66
print(e)

testList = [1,2,3,4,5,6,7,8,9]
#problem 6
import statistics
#excel:
# =AVERAGE()
avg = statistics.mean(testList)
print(avg)

#problem 7
#excel:
# =MEDIAN()
median = statistics.median(testList)
print(median)

#problem 8
#excel:
# =MAX()
maxNum = max(testList)
print(maxNum)

#problem 9
#excel:
# =RANGE()
range = max(testList)-min(testList)
print(range)

#problem 10
#excel:
# =STDEV.S()
standard_deviation = statistics.stdev(testList)
print(standard_deviation)