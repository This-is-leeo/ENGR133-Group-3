def calcInterest(pV, i, n, cP):
  i *= 0.01; #convert percentage to decimal
  print(f"(1+(i/cp) = {(1 + (i / cP))}")
  print(f"(cP * n) = {(cP * n)}")
  print(f"pow((1+(i/cp)), (cP * n)) = {pow((1 + (i / cP)), (cP * n))}")
  return pV * (1 + (i / (cP))) ** (cP * n) - pV


print(calcInterest(10000,3,3,12))
#wtf
"""
apperently in C 1/12 = 0.01
float calcInterest(float pV, float i, int n, int cP)
{
  i *= 0.01; //convert percentage to decimal
  printf("(1+(i/cp) = %f\n", (1 + (i / (float)cP)));
  printf("(cP * n) = %d\n", (cP * n));
  printf("pow((1+(i/cp)), (cP * n)) = %f\n", pow((1 + (i / cP)), (cP * n)));
  return pV * pow((1 + (i / cP)) , (cP * n)) - pV;
}
"""