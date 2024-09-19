from math import pi, sqrt
ft3toGallons = 7.48

def standard(L1, L2, Ds, Dd): 
    if L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0:
        print("Please enter valid dimensions.")
        return None
    return ft3toGallons * L2 * ((L1 * Ds) + (1/3 * (Dd - Ds) * L1))
    #comments1
def ramp(L1, L2, Ds, Dd):
    if L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0:
        print("Please enter valid dimensions.")
        return None
    return ft3toGallons * L2 * ((5/6 * L1 * Ds) + ((Dd - Ds) * (L1 / 6)))
    #comments
def round(L1, L2, Ds, Dd):
    if L1 < 0 or L2 < 0 or Ds < 0 or Dd < 0:
        print("Please enter valid dimensions.")
        return None
    return ft3toGallons * ((pi * L1 ** 2 * Ds) +  (pi * (Dd - Ds) /3) * (L1 ** 2 + L1*L2 + L2 ** 2))

    #more comments!
#Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#Nullam sit amet suscipit sem, non hendrerit lorem. 
#Integer ut lacus augue. Maecenas dignissim erat ligula, eu viverra libero mollis ut. 
#Ut id hendrerit dui, at auctor est. 
#Ut felis lacus, vulputate vel lorem eget, viverra suscipit leo. 
